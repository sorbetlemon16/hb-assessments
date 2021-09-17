"""Tests for lists.py"""

from lists import (
    get_words_by_first_letter,
    filter_by_length,
    words_in_common,
    every_other_item,
    smallest_n_items,
    get_index,
)

##
# Test for get_words_by_first_letter


def test_get_words_by_first_letter_is_list():
    """Test that the return value of get_words_by_first_letter is a list."""

    assert get_words_by_first_letter([], "") == []


def test_get_words_by_first_letter_returns_words():
    """Test that get_words_by_first_letter returns words that start with a certain letter."""

    assert get_words_by_first_letter(["apple", "berry"], "b") == ["berry"]


def test_get_words_by_first_letter_returns_multiple_words():
    """Test that get_words_by_first_letter can return multiple words."""

    assert get_words_by_first_letter(["apple", "and"], "a") == ["apple", "and"]


##
# Tests for filter_by_length


def test_filter_by_length_is_list():
    """Test that filter_by_length returns a list."""

    assert filter_by_length([], 0) == []


def test_filter_by_length_returns_items_that_match_length():
    """Test that filter_by_length returns all items that match the given length."""

    assert filter_by_length(["A", "BB", "CCC"], 1) == ["A"]


def test_filter_by_length_returns_multiple_items_match_length():
    """Test that filter_by_length can return multiple items."""

    assert filter_by_length(["A", "1", "BB", "CCC"], 1) == ["A", "1"]


##
# Tests for words_in_common


def test_words_in_common_is_list():
    """Test that words_in_common returns a list."""

    assert words_in_common([], []) == []


def test_words_in_common_has_common_words():
    """Test that words_in_common returns the words common between given lists."""

    assert words_in_common(["python"], ["lizard", "python"]) == ["python"]


def test_words_in_common_no_dupes():
    """Test that the return value of words_in_common doesn't contain repeats."""

    assert words_in_common(["python", "python"], ["lizard", "python"]) == [
        "python"
    ]


##
# Tests for every_other_item


def test_every_other_item_is_list():
    """Test that every_other_item returns a list."""

    assert every_other_item([]) == []


def test_every_other_item():
    """Test that every_other_item returns every other item in the given list."""

    assert every_other_item(["apple", "berry", "cherry"]) == [
        "apple",
        "cherry",
    ]


##
# Tests for smallest_n_items


def test_smallest_n_items_is_list():
    """Test that smallest_n_items returns a list."""

    assert smallest_n_items([1, 1], 0) == []


def test_smallest_n_items_length():
    """Test that the return value of smallest_n_items has the proper length."""

    assert smallest_n_items([1, 1], 2) == [1, 1]


def test_smallest_n_items_descending_order():
    """Test that the return value of smallest_n_items is in descending order."""

    assert smallest_n_items([1, 2, 3, 4], 3) == [3, 2, 1]


##
# Tests for get_index


def test_get_index_return_none_if_not_found():
    """Test that get_index returns None of nothing is found."""

    assert get_index([], "apple") is None


def test_get_index():
    """Test that get_index returns an integer if an item is found."""

    assert get_index(["apple"], "apple") == 0


def test_get_index_return_first_index_found():
    """Test that get_index returns the index of the first item that matches."""

    assert get_index(["apple", "berry", "berry"], "berry") == 1