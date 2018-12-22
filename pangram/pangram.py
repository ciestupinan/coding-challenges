"""Given a string, return True if it is a pangram, False otherwise.

For example::

    >>> is_pangram("The quick brown fox jumps over the lazy dog!")
    True
    
    >>> is_pangram("I love cats, but not mice")
    False

    >>> is_pangram("is this 15 a PAngraM@?")
    False
"""

import string



def is_pangram(sentence):
    """Given a string, return True if it is a pangram, False otherwise."""

    stripped_sentence = (sentence.strip(string.punctuation)).lower()
    
    alphabet = {}
    for char in stripped_sentence:
        if char.isalpha():
            if char in alphabet:
                alphabet[char] += 1
            else:
                alphabet[char] = 1

    if len(alphabet) == 26:
        return True

    return False



if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. YAY!\n")
