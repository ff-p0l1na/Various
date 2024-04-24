import requests
import wget
data_results = []

def FindBooks(language, year):
    global data_results
    url = f"https://gutendex.com/books?author_year_start={year}&author_year_end={year}&languages={language}"

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

###

language = input("Enter the language code, e.g. 'en': ")
year = input("Enter the year: ")
FindBooks(language, year)

###

def DownloadBook(id):
    url = f'https://www.gutenberg.org/ebooks/{id}.txt.utf-8'
    book_file = wget.download(url)
    return book_file

chosen_id = input("Enter chosen book's ID to download it: ")
DownloadBook(chosen_id)
