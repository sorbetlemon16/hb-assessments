"""Tests for functions.py"""

from dicts import (
    count_words,
    get_melons_at_price,
    translate_to_pirate_talk,
    create_word_chain,
)


##
# Tests for count_words


def test_count_words_returns_a_dictionary():
    """Test that the return value of count_words is a dictionary."""

    assert type(count_words("")) is dict


def test_count_words_returns_words_and_counts():
    """Test that count_words returns the words of a phrase and the number of times they appear."""

    assert count_words("how are you") == {"how": 1, "are": 1, "you": 1}


def test_sum_of_counts_is_equal_to_num_words():
    """Test that the sum of counts returned by count_words is equal to the number of words in the phrase."""

    phrase = "rose is a rose is a rose"
    num_words = len(phrase.split(" "))

    counts = count_words(phrase)
    sum_counts = sum(counts.values())

    assert sum_counts == num_words


def test_punctuation_ok():
    """Test that count_words doesn't handle punctuation."""

    assert count_words("hello! hello") == {"hello!": 1, "hello": 1}


def test_capitalization_ok():
    """Test that count_words doesn't handle capitalization."""

    assert count_words("python Python") == {"python": 1, "Python": 1}


##
# Tests for get_melons_at_price


def test_get_melons_at_price_returns_a_set():
    """Test that the return value of get_melons_at_price is a set."""

    assert type(get_melons_at_price(0)) is set


def test_get_melon_names_from_MELONS():
    """Test that get_melon_names returns a set of melon names from MELONS."""

    assert get_melons_at_price(2.5) == set(["honeydew", "cantaloupe"])


def test_get_melon_names_when_no_melons_found():
    """Test that get_melon_names returns an emtpy set when no melons match a given price."""

    assert get_melons_at_price(550) == set()


##
# Test translate_to_pirate_talk


def test_translate_to_pirate_talk_returns_string():
    """Test that the return value of translate_to_pirate_talk is a string."""

    assert type(translate_to_pirate_talk("")) is str


def test_translate_to_pirate_talk_uses_ENG_PIRATE_LOOKUP():
    """Test that translate_to_pirate_talk translates words in ENG_PIRATE_LOOKUP."""

    assert (
        translate_to_pirate_talk("professor excuse your students")
        == "foul blaggart arr yer swabbies"
    )


def test_translate_to_pirate_talk_passthrough_words():
    """Test that words not included in ENG_PIRATE_LOOKUP pass through unchanged."""

    assert (
        translate_to_pirate_talk("the restroom is a hotel for germs")
        == "the head be a fleabag inn for germs"
    )


##
# Tests for create_word_chain


def test_create_word_chain_returns_list():
    """Test that create_word_chain returns a list."""

    assert type(create_word_chain(["a"])) is list


def test_create_word_chain_correct_sequence():
    """Test that create_word_chain starts with the first word in the list and the next word starts with the last letter of the first word."""

    assert create_word_chain(["env", "at", "end", "vital"]) == [
        "env",
        "vital",
    ]


def test_create_word_return_if_no_possible_next_word():
    """Test that create_word_chain returns a list with the first word if it can't find the next one."""

    assert create_word_chain(["barry", "apple", "coco"]) == ["barry"]


def test_create_word_chain_multiple_candidates_for_next():
    """Test that create_word_chain will continue building the sequence until there are no words left."""

    assert create_word_chain(["nathan", "noon", "neem"]) == [
        "nathan",
        "noon",
        "neem",
    ]
