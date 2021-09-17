"""Skills 2: oo.py

Summary.
"""

##
# Design a Bicycle Class


class Bicycle:
    """A bicycle."""

    # TODO: replace this with your code


##
# Define a Method for Processing Password Changes


class User:
    """A user who can log in to a website."""

    def __init__(self, username, password):
        """Create a user with the given username and password."""

        self.username = username
        self.password = password

    def process_change_password(self, current_password, new_password):
        """Process a password change."""

        # TODO: replace this with your code


##
# Implement Library Methods


class Book:
    """A book with a title and author."""

    def __init__(self, title, author):
        """Create a book."""

        self.title = title
        self.author = author


class Library:
    """A library of books."""

    def __init__(self):
        """Create a library."""

        self.books = []

    def create_and_add_book(self, title, author):
        """Create a Book and add it to the library's list of books."""

        # TODO: replace this with your code

    def find_books_by_author(self, author):
        """Return a list of books by the given author."""

        # TODO: replace this with your code


##
# Subclass Rectangle to Implement Square


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle."""

        self.length = length
        self.width = width

    def calculate_area(self):
        """Return the area of the rectangle."""

        return self.length * self.width


class Square(Rectangle):
    """A square."""

    # TODO: replace this with your code


if __name__ == "__main__":
    import sys
    from pathlib import Path

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        try:
            import pytest

            pytest.main([f"test_{Path(__file__).name}"])
        except ModuleNotFoundError:
            print("Unable to run tests because 'pytest' wasn't found :(")
            print("Run the command below to install pytest:")
            print()
            print("    pip3 install pytest")
