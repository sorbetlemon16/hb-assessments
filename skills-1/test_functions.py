"""Tests for functions.py"""

from functions import (
    is_all_berries,
    create_intro_note,
    get_sqrt,
    concat_all,
)
import inspect


##
# Tests for is_all_berries


def test_is_all_berries():
    """Test that is_all_berries returns True if all items are berries."""

    assert (
        is_all_berries(["strawberry", "raspberry", "blackberry", "currant"])
        is True
    )


def test_is_all_berries_return_false_if_not_all():
    """Test that is_all_berries returns False if not all items are berries."""

    assert is_all_berries(["apple", "berry", "cherry"]) is False


def test_is_all_berries_has_not_been_modified():
    """Test that the body of is_all_berries has not been modified."""

    original_src = 'def is_all_berries(fruits):\n    """Return True if all items in fruits are valid berries."""\n\n    for fruit in fruits:\n        if not is_berry(fruit):\n            return False\n\n    return True\n'

    assert inspect.getsource(is_all_berries) == original_src


##
# Tests for create_intro_note


def test_create_intro_note_same_hometown():
    """Test create_intro_note for profiles with the same hometown."""

    profile1 = ("Hack", "Bright", "San Francisco")
    profile2 = ("Bodhi", "Hacks", "San Francisco")

    assert (
        create_intro_note(profile1, profile2)
        == "Hack Bright, meet Bodhi Hacks.\nLooks like y'all are from the same hometown!"
    )


def test_create_intro_note_different_hometown():
    """Test create_intro_note for profiles with different hometowns."""

    profile1 = ("Hack", "Bright", "San Francisco")
    profile2 = ("Bodhi", "Hacks", "Boston")

    assert (
        create_intro_note(profile1, profile2)
        == "Hack Bright, meet Bodhi Hacks."
    )


def test_create_intro_note_has_not_been_modified():
    """Test that the body of create_intro_note has not been modified."""

    original_src = 'def create_intro_note(profile1, profile2):\n    """Given 2 tuples of user profile data, return contents of an intro note."""\n\n    fullname1 = create_fullname(profile1)\n    fullname2 = create_fullname(profile2)\n\n    note_contents = [f"{fullname1}, meet {fullname2}."]\n\n    if has_same_hometown(profile1, profile2):\n        note_contents.append(f"Looks like y\'all are from the same hometown!")\n\n    return "\\n".join(note_contents)\n'

    assert inspect.getsource(create_intro_note) == original_src


##
# Tests for get_sqrt


def test_get_sqrt():
    """Test that get_sqrt returns the square root of 1."""

    assert get_sqrt(1) == 1


def test_get_sqrt_float():
    """Test that get_sqrt returns the square root of 9 as a floating point number."""

    assert round(get_sqrt(9), 1) == 3.0


def test_get_sqrt_has_not_been_modified():
    """Test that the body of get_sqrt has not been modified."""

    original_src = 'def get_sqrt(x):\n    """Return the square root of x."""\n\n    guess = 1\n\n    while True:\n        div_result = div(x, guess)\n\n        # is_close_enough needs to return True or False. However, since the\n        # function is incomplete, it will return None. This will cause the\n        # while loop to continue infinitely. So, we raise a\n        # ValueError if we don\'t get a boolean to prevent\n        # an infinite loop.\n        if type(is_close_enough(div_result, guess)) is not bool:\n            raise ValueError(f"is_close_enough did not return a boolean.")\n\n        if is_close_enough(div_result, guess) is not True:\n            guess = avg(div_result, guess)\n        else:\n            return guess\n'

    assert inspect.getsource(get_sqrt) == original_src


##
# Tests for concat_all


def test_concat_all_modify_in_place():
    """Test that concat_all modifies the given list in place."""

    test_list = []
    concat_all(test_list, "apple", "berry")

    assert test_list == ["apple", "berry"]


def test_concat_all_returns_none():
    """Test that concat_all returns None."""

    assert concat_all([], "apple") is None