class Book:
    """
    Represents a book in the library with a title, author, and checkout status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author
        # Private attribute to track checkout status, defaults to False (available)
        self._is_checked_out = False

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as available (returned).
        """
        self._is_checked_out = False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if the book is not checked out, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        # Private list to store Book objects
        self._books = []

    def add_book(self, book):
        """
        Adds a Book instance to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        self._books.append(book)
        # print(f"'{book.title}' added to the library.") # Optional: for immediate feedback

    def check_out_book(self, title):
        """
        Checks out a book from the library by its title.

        Args:
            title (str): The title of the book to check out.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if book.is_available():
                    book.check_out()
                    print(f"'{title}' has been checked out.")
                else:
                    print(f"'{title}' is already checked out.")
                return # Exit after finding and processing the book
        if not found:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Returns a book to the library by its title.

        Args:
            title (str): The title of the book to return.
        """
        found = False
        for book in self._books:
            if book.title == title:
                found = True
                if not book.is_available(): # If it's currently checked out
                    book.return_book()
                    print(f"'{title}' has been returned.")
                else:
                    print(f"'{title}' is already in the library.")
                return # Exit after finding and processing the book
        if not found:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books that are currently available in the library.
        """
        available_count = 0
        for book in self._books:
            if book.is_available():
                print(book) # Uses the __str__ method of the Book object
                available_count += 1
        
        if available_count == 0:
            print("No books available.")
