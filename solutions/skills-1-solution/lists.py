"""Skills 1: lists.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_lists.py.
"""


def get_words_by_first_letter(words, letter):
    """Return a list of all words that start with the given letter."""

    result = []
    for word in words:
        if word.startswith(letter):
            result.append(word)

    return result


def filter_by_length(items, length):
    """Return a list of all items with the given length."""

    result = []
    for item in items:
        if len(item) == length:
            result.append(item)

    return result


def words_in_common(words1, words2):
    """Return strings that words1 and words2 have in common."""

    common_words = set(words1) & set(words2)

    return list(common_words)


def every_other_item(items):
    """Return a list with every other element items (start with index 0)."""

    return items[::2]


def smallest_n_items(items, n):
    """Return the n smallest values in the given list, in descending order.

    You can assume that `n` will be less than the length of the list.
    """

    smallest_items = sorted(items)[:n]

    return list(reversed(smallest_items))


def get_index(items, value):
    """Search for a value in items and return its index.

    If the value doesn't exist in items, return None. If the value appears more
    than once, return the index of the first occurrence of the value.
    """

    for index, item in enumerate(items):
        if item == value:
            return index


if __name__ == "__main__":
    from pathlib import Path
    import sys
    import pytest

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([f"test_{Path(__file__).name}"])