import requests

def FindBooks(language, year):

    url = f"https://gutendex.com/books?author_year_start={year}&languages={language}"

    # Make the API request
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the JSON response
        data = response.json()
        print(data['results']) # results is a list of dicts; each dict contains info about 1 book
        data_res = data['results'] # data_res is now a LIST of dicts
        for item in data_res:
            print(f"ID: {item['id']} TITLE: {item['title']}")
    else:
        print("Failed to fetch books. Status code:", response.status_code)

# Example usage
FindBooks(language='en', year=2023)
