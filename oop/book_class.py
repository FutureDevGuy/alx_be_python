#!/usr/bin/env python3

class Book:
    """
    A class to represent a book with its title, author, and publication year.
    This class demonstrates the use of Python's magic methods.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize a new Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year
        print(f"Book '{self.title}' created.")

    def __del__(self):
        """
        Destructor to perform cleanup when the object is deleted.
        Prints a message indicating the book is being deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns a human-readable string representation of the object.
        This is what is displayed by the print() function.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the object.
        This should be an unambiguous string that could be used to recreate the object.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
