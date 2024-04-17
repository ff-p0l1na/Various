import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import pandas as pd
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt

nltk.download('punkt')
nltk.download('stopwords')

# Read the input file from the command line argument
input_file = sys.argv[1]

# Tokenize the text and remove punctuation and stop words
with open(input_file, 'r') as file:
    data = file.read()
    list_of_words = word_tokenize(data.lower())  # Convert to lowercase
    stoplist = set(stopwords.words('english'))
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
output_file = f"{input_file.split(sep='.')[0]}_word_count.tsv"
df.to_csv(output_file, sep='\t', index=False)

# Create a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(words_counted)

# Plot the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
