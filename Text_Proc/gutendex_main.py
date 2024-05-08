import argparse
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pandas as pd
import requests
import string
import sys
import wget
from wordcloud import WordCloud
#####
nltk.download('punkt')
nltk.download('stopwords')
#####
data_results = []
#####
def FindBooks(language, year_start, year_end):
    global data_results
    url = f"https://gutendex.com/books?author_year_start={year_start}&author_year_end={year_end}&languages={language}" # year start and end instead of one variable

    # Make the API request
    response = requests.get(url)
    if response.status_code == 200: # Check if request was successful
        data = response.json()
        # value of 'results' is a LIST of dicts; each dict contains info about 1 book;
        data_results = data['results'] # data_results is now a LIST of dicts
        print("Books found:\n")
        for item in data_results:
            print(f"ID: {item['id']}\tTitle: {item['title']}")

        return data_results
    else:
        print("Failed to fetch books. Status code:", response.status_code)

def DownloadBook(id, file_type):
    url = f'https://www.gutenberg.org/ebooks/{id}.{file_type}' # file type needs to be defined by user
    book_file = wget.download(url)
    return book_file

def PlotTheWordCloud():
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

"""
remove this and use argparse flags instead
# Prompt the user for language and year:
language = input("Enter the language code, e.g. 'en': ")
year = input("Enter the year: ")
"""

parser = argparse.ArgumentParser(description='Download books from Project Gutenberg')
parser.add_argument('--language', type=str, required=True, help='Specify a desired language for looked books')
parser.add_argument('--year_start', type=int, required=True, help='Specify a year for the start range of looked books')
parser.add_argument('--year_end', type=int, required=True, help='Specify a year for the end range of looked books')
args = parser.parse_args()

language = args.language
year_start = args.year_start
year_end = args.year_end
file_type = args.file_type

# Find all the matching books:
FindBooks(language, year_start, year_end)

# Download the chosen book:
chosen_id = input("Enter chosen book's ID to download it: ")
book_file = DownloadBook(chosen_id, file_type)

"""
How to handle choosing a file format? look up example.json
"""

# Tokenize the text and remove punctuation and stop words
with open(book_file, 'r') as file:
    lines = [line.strip() for line in file if line.strip()]
    data = '\n'.join(lines)
    list_of_words = word_tokenize(data.lower())  # Convert to lowercase
    stoplist = stopwords.words('english')
    # string.punctuation is a string containing all the punctuation characters defined in the Python standard library string
    stripped_list = [word.strip(string.punctuation) for word in list_of_words if word.strip(string.punctuation) not in stoplist]

# Count occurrences of each word
words_counted = {}
for word in stripped_list:
    if word in words_counted:
        words_counted[word] += 1
    else:
        words_counted[word] = 1

# Convert the dictionary to a DataFrame
df = pd.DataFrame(words_counted.items(), columns=['WORD', 'COUNT'])

# Sort the DataFrame by count in descending order
df = df.sort_values(by='COUNT', ascending=False)

# Write the DataFrame to a TSV file
# output_file = f"{book_file.split(sep='.')[1]}_word_count.tsv"
output_file = f"{chosen_id}.txt"
df.to_csv(output_file, sep='\t', index=False)

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(words_counted)

#####

PlotTheWordCloud()