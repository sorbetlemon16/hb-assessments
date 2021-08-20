"""Skills 2: dicts.py

Complete the following functions. To get a better idea of how each function
should behave, see the examples in test_dicts.py.
"""


def count_words(phrase):
    """Count the words in a string.

    This function doesn't handle punctuation so 'hello!' and 'hello'
    are two different words. It also doesn't handle captialization so
    'Hello' and 'hello' are two different words as well.
    """

    words_and_counts = {}
    for word in phrase.split(" "):
        if word not in words_and_counts:
            words_and_counts[word] = 0

        words_and_counts[word] += 1

    return words_and_counts


MELONS = [
    ("honeydew", 2.5),
    ("cantaloupe", 2.5),
    ("watermelon", 2.95),
    ("musk", 3.25),
    ("crenshaw", 3.25),
    ("christmas", 14.25),
]


def get_melons_at_price(price):
    """Return a set with the names of melons being sold at the given price.

    This will return the names of melons from MELONS. MELONS is a list
    of tuples that have (melon_name, price).

    If there are no melons being sold at the given price it returns an
    empty set.
    """

    # Process MELONS into dictionary so it's easier to lookup melons
    # by their price
    melons_price_lookup = {}
    for melon_name, melon_price in MELONS:
        if melon_price not in melons_price_lookup:
            melons_price_lookup[melon_price] = set()

        melons_price_lookup[melon_price].add(melon_name)

    return melons_price_lookup.get(price, set())


ENG_PIRATE_LOOKUP = {
    "sir": "matey",
    "hotel": "fleabag inn",
    "student": "swabbie",
    "man": "matey",
    "professor": "foul blaggart",
    "restaurant": "galley",
    "your": "yer",
    "excuse": "arr",
    "students": "swabbies",
    "are": "be",
    "restroom": "head",
    "my": "me",
    "is": "be",
}


def translate_to_pirate_talk(phrase):
    """Return a phrase in pirate talk.

    Given an English phrase, use ENG_PIRATE_LOOKUP to translate
    words to pirate talk. Words that aren't listed in ENG_PIRATE_LOOKUP
    should not be translated and should pass through unchanged.

    The given phrase will be normalized so it will never contain punctuation
    and will only consist of lowercased letters.
    """

    translated_words = []
    for word in phrase.split(" "):
        translated_words.append(ENG_PIRATE_LOOKUP.get(word, word))

    return " ".join(translated_words)


def create_word_chain(words):
    """Return a sequence of words arranged according to the rules below.

    The sequence starts with the first word in the given list. The
    next word will start with the last letter of the preceding word.
    For example, these are all valid sequences of words:

        zoo, octos, sour, racket
        cute, etcetera, antsy, yak, karat

    Sometimes you'll get a word where there are multiple candidates
    for the next word. For example, if our list of words contains:

        noon, naan, nun

    ...then the first word in the sequence is 'noon':

        noon

    ...the next word should be the *first* word that starts with 'n'.
    So, even though 'naan' and 'nun' both start with 'n', the next
    word should be 'naan' because 'naan' appears before 'nun'. The
    final sequence of words will be:

        noon, naan, nun

    The sequence will continue in this fashion until it runs out of
    words or it can't find words that'll fit the pattern.
    """

    # Handle edge case where words is an empty list
    if not words:
        return []

    # Separate the first word in words from the rest of the words so
    # we can use first_word to start the sequence and process
    # rest_words later
    first_word = words[0]
    rest_words = words[1:]
    # You can also do this in one line with:
    # first_word, *rest_words = words

    sequence = [first_word]

    # Process the rest of the words into a dictionary that'll be used
    # as a lookup table. We want to look for words that start with a
    # certain letter so the keys of this dictionary will be first letters
    # and values will be list of words that start with that letter.
    words_lookup = {}
    for word in rest_words:
        first_letter = word[0]

        if first_letter not in words_lookup:
            words_lookup[first_letter] = []

        words_lookup[first_letter].append(word)

    while True:
        # Find the next word using the last char of the latest
        # item added to sequence
        next_word_key = sequence[-1][-1]

        next_words = words_lookup.get(next_word_key)
        if next_words:
            # next_words.pop(0) will remove and return the
            # element at index 0
            sequence.append(next_words.pop(0))
        else:
            # We're finished building the sequence when next_words
            # is None (because next_word_key doesn't exist in
            # words_lookup) or when next_words is [] (when we've
            # used up all words that start with next_word_key).
            return sequence


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
