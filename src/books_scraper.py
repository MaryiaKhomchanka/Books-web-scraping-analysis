import requests 
import pandas as pd 
from bs4 import BeautifulSoup 

def scrape_books(url): 
    data = requests.get(url).text  
    soup = BeautifulSoup(data, 'html.parser')
    books = soup.find_all('article', class_ = 'product_pod')
    return books  


def books_to_dataframe(books):
    books_dict = {"Title": [], "Price": [], "Rating": [], "Availability":[]}
    for book in books: 
        books_dict["Title"].append(book.find('h3').text)
        books_dict["Price"].append(book.find('p', class_ = 'price_color').text)
        books_dict["Rating"].append(book.find('p', class_ = 'star-rating')['class'][1])
        books_dict["Availability"].append(book.find('p', class_ = 'availability').text.strip())
    
    books_dataframe = pd.DataFrame.from_dict(books_dict)
    return books_dataframe


def get_all_books(first_page, last_page):
    all_books = []
    for i in range (first_page, last_page + 1):
        url = "https://books.toscrape.com/catalogue/page-" + str(i) + ".html"
        books = scrape_books(url)
        all_books.extend(books)
    all_books_dataframe = books_to_dataframe(all_books)
    return all_books_dataframe


def save_to_csv(dataframe):
    dataframe.to_csv("data/books.csv")


def get_books_csv(first_page, last_page):
    books = get_all_books(first_page, last_page)
    save_to_csv(books)


def main(): 
    get_books_csv(1, 51)


if __name__ == "__main__": 
    main()












