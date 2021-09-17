"""Tests for oo.py"""

import pytest

from oo import Bicycle, User, Book, Library, Square

##
# Tests for 'Design a Bicycle Class'


def test_create_bicycle():
    """Test instantiating a Bicycle instance."""

    assert Bicycle("Bikes R Us", "yellow")


def test_bicycle_manufacturer():
    """Test accessing a bike's manufacturer."""

    bike = Bicycle("Razor", "green")

    assert bike.manufacturer == "Razor"


def test_bicycle_color():
    """Test accessing a bike's color."""

    bike = Bicycle("Razor", "green")

    assert bike.color == "green"


def test_bicycle_wheels():
    """Test that Bicycle.wheels is 2."""

    assert Bicycle.wheels == 2


##
# Tests for 'Define a Method for Processing Password Changes'


def test_change_password_match():
    """Test that user's password is changed if current_password matches password."""

    user = User("testuser", "test123")
    user.process_change_password("test123", "newpassword")

    assert user.password == "newpassword"


def test_change_password_nomatch():
    user = User("testuser", "test123")

    with pytest.raises(ValueError):
        user.process_change_password("nomatch", "newpassword")


##
# Tests for 'Implement Library Methods'


def test_create_and_add_book_appends_book():
    """Test that create_and_add_book appends to library.books."""

    lib = Library()
    lib.create_and_add_book("How to Python", "Hackbrighter")

    assert len(lib.books) > 0


def test_create_and_add_book_creates_book_object():
    """Test that create_and_add_book creates a Book."""

    lib = Library()
    lib.create_and_add_book("An Amazing Memoir", "Balloonicorn")

    assert type(lib.books[0]) is Book


def test_find_books_by_author_return_empty():
    """Test that find_books_by_author returns an empty list if no books are found."""

    lib = Library()

    assert lib.find_books_by_author("Test") == []


def test_find_books_by_author_return_list():
    """Test that find_books_by_author returns a list if books are found."""

    lib = Library()
    lib.create_and_add_book("Object Orientation 101", "J. Hacks")

    assert len(lib.find_books_by_author("J. Hacks")) > 0


def test_find_books_by_authors_search_book_object():
    """Test that find_books_by_author searches a list of Book objects."""

    book = Book("A Fake Book", "Ms. Che Vious")

    lib = Library()
    lib.books.append(book)

    assert lib.find_books_by_author("Ms. Che Vious") == [book]


##
# Tests for 'Subclass Rectangle to Implement Square'


def test_square_equal_length_width():
    """Test instantiating a Square and check that length and width are equal."""

    square = Square(2)

    assert square.length == square.width


def test_calculate_area():
    """Test calculate_area for a valid square."""

    square = Square(2)

    assert square.calculate_area() == 4


def test_calculate_area_invalid():
    """Test calculcate_area for an invalid square."""

    square = Square(2)
    # Intentionally change square.width to 4 to create invalid square
    square.width = 4

    with pytest.raises(ValueError):
        square.calculate_area()
