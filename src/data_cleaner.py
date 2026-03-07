import pandas as pd

def books_to_dataframe(file):
    books = pd.read_csv(file)
    return books 

def clean_price(books): 
    clean_price = books["Price"].str.replace('Â£', '')
    books["Price"] = pd.to_numeric(clean_price)
    return books

def fix_ratings(books):
    int_ratings = []
    numbers = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    books["Rating"] = books["Rating"].map(numbers)
    return books

def clean_books(file):
    books_dataframe = books_to_dataframe(file)
    clean_books_price = clean_price(books_dataframe)
    clean_books = fix_ratings(clean_books_price)
    return clean_books


def main(): 
    file = "data/books.csv"
    books = clean_books(file)

    print(books["Rating"])
    print(books["Price"])
    
   

if __name__ == "__main__": 
    main()
