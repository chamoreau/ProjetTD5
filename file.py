#!/usr/bin/env python3

from book import Book

def main():
    book = Book("TEST")
    book.insert_order(10, 10.0, 0)
    book.insert_order(120, 12.0, 1)
    book.insert_order(5, 10.0, 0)
    book.insert_order(2, 11.0, 0)
    book.insert_order(1, 11.0, 1)
    book.insert_order(10, 10.0, 1)
    
    print(book.tabular_print())
    if __name__ == "__main__":
        main()
    

