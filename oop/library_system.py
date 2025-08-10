#!/usr/bin/env python3

class Book:
    """
    A base class to represent a generic book.
    It has a title and an author.
    """
    def __init__(self, title, author):
        """
        Initializes the Book with a title and author.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns a string representation of the book.
        This method is used by the list_books() method in the Library class.
        """
        return f"Title: {self.title}, Author: {self.author}"


class EBook(Book):
    """
    A derived class representing an electronic book.
    It inherits from Book and adds a file_size attribute.
    """
    def __init__(self, title, author, file_size):
        """
        Initializes the EBook by calling the base class constructor
        and then initializing its own file_size attribute.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Overrides the __str__ method to include the file_size.
        """
        return f"{super().__str__()}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    A derived class representing a physical print book.
    It inherits from Book and adds a page_count attribute.
    """
    def __init__(self, title, author, page_count):
        """
        Initializes the PrintBook by calling the base class constructor
        and then initializing its own page_count attribute.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Overrides the __str__ method to include the page_count.
        """
        return f"{super().__str__()}, Page Count: {self.page_count}"


class Library:
    """
    A class to represent a library using composition.
    It manages a collection of various types of books.
    """
    def __init__(self):
        """
        Initializes the Library with an empty list to store books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a Book, EBook, or PrintBook instance to the library's collection.
        """
        self.books.append(book)
        print(f"Added '{book.title}' to the library.")

    def list_books(self):
        """
        Prints the details of each book in the library.
        """
        print("\nLibrary Contents:")
        if not self.books:
            print("The library is empty.")
        else:
            for book in self.books:
                print(book)