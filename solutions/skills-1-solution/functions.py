"""Skills 1: functions.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_functions.py.
"""


def is_all_berries(fruits):
    """Return True if all items in fruits are valid berries."""

    for fruit in fruits:
        if not is_berry(fruit):
            return False

    return True


def is_berry(fruit):
    """Return True if fruit is a valid berry.

    Valid berries are "strawberry", "raspberry", "blackberry", and "currant".
    There are no other valid berries. For example, "berry" is not a valid berry.
    """

    return fruit in set(["strawberry", "raspberry", "blackberry", "currant"])


def create_intro_note(profile1, profile2):
    """Given 2 tuples of user profile data, return contents of an intro note."""

    fullname1 = create_fullname(profile1)
    fullname2 = create_fullname(profile2)

    note_contents = [f"{fullname1}, meet {fullname2}."]

    if has_same_hometown(profile1, profile2):
        note_contents.append(f"Looks like y'all are from the same hometown!")

    return "\n".join(note_contents)


def create_fullname(profile):
    """Given a tuple of user profile data, return a full name.

    Tuples that represent user profile data are 3 items long. The first item is
    the user's first name, the second is the user's last name, and the third is
    the user's hometown. Ex.: ("Hack", "Bright", "San Francisco").
    """

    # Note: we unpack the 3 values in profile to create 3 variables. Since we
    # only need the profile's first name and last name, notice how we named
    # the third variable "_" to communicate that we'll never use it in this
    # function. This is just a code style thing though --- to Python, "_" is
    # a regular variable.
    first_name, last_name, _ = profile

    return f"{first_name} {last_name}"


def has_same_hometown(profile1, profile2):
    """Return True if the hometowns in each profile match.

    Tuples that represent user profile data are 3 items long. The first item is
    the user's first name, the second is the user's last name, and the third is
    the user's hometown. Ex.: ("Hack", "Bright", "San Francisco").
    """

    hometown1, hometown2 = profile1[-1], profile2[-1]
    return hometown1 == hometown2


def get_sqrt(x):
    """Return the square root of x."""

    guess = 1

    while True:
        div_result = div(x, guess)

        # is_close_enough needs to return True or False. However, since the
        # function is incomplete, it will return None. This will cause the
        # while loop to continue infinitely. So, we raise a
        # ValueError if we don't get a boolean to prevent
        # an infinite loop.
        if type(is_close_enough(div_result, guess)) is not bool:
            raise ValueError(f"is_close_enough did not return a boolean.")

        if is_close_enough(div_result, guess) is not True:
            guess = avg(div_result, guess)
        else:
            return guess


def div(x, y):
    """Return the quotient of x and y.

    In other words, return the result of dividing x by y.
    """

    return x / y


def avg(x, y):
    """Return the average of x and y.

    Here, the average of x and y is the mean of x and y. In other words, it's
    computed by dividing the sum of x and y by 2.
    """

    return (x + y) / 2


def is_close_enough(x, y):
    """Return True if x and y are mostly equivalent up to a tolerance of 0.0001.

    In other words, return True if the absolute value of x minus y is less than
    0.0001.
    """

    return abs(x - y) < 0.0001


def concat_all(items, *additional_items):
    """Add all arguments to the end of items and return None."""

    items.extend(additional_items)


if __name__ == "__main__":
    from pathlib import Path
    import sys
    import pytest

    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        pytest.main([f"test_{Path(__file__).name}"])