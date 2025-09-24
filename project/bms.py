# Book Management System
import json

# book = {
#     "title": input("Enter book title: "),
#     "author": input("Enter book author: "),
#     "year": input("Enter publication year: "),
#     "isbn": input("Enter ISBN number: "),
#     "publisher": input("Enter publisher: "),
#     "genre": input("Enter genre: "),
#     "pages": input("Enter number of pages: "),
# }

# with open("book.json", "a") as file:
#     json.dump(book, file, indent=4)
    
with open("book.json", "r") as file:
    book_details = json.load(file)
    print(book_details)