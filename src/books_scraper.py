import requests 
import csv 
import pandas as pd 
from bs4 import BeautifulSoup 

def scrape_books(url): 
    data = requests.get(url).text  
    soup = BeautifulSoup(data, 'html.parser')
    books = soup.find_all('article', class_ = 'product_pod')
    return books  

def books_to_dataset(books):
    books_dict = {"Title": [], "Price": [], "Rating": [], "Availability":[]}
    for book in books: 
        books_dict["Title"].append(book.find('h3').text)
        books_dict["Price"].append(book.find('p', class_ = 'price_color').text)
        books_dict["Rating"].append(book.find('p', class_ = 'star-rating')['class'][1])
        books_dict["Availability"].append(book.find('p', class_ = 'availability').text)
    return books_dict 



def main(): 
    URL = "https://books.toscrape.com" 
    books = scrape_books(URL) 

    ##print(books)

    booksdict = books_to_dataset(books)
    print(booksdict)

if __name__ == "__main__": 
    main()












