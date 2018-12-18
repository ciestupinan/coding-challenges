"""Decode a string.

A valid code is a sequence of numbers and letter, always starting with a number
and ending with letter(s).

Each number tells you how many characters to skip before finding a good letter.
After each good letter should come the next next number.

For example, the string "hey" could be encoded by "0h1ae2bcy". This means
"skip 0, find the 'h', skip 1, find the 'e', skip 2, find the 'y'".

A single letter should work::

    >>> decode("0h")
    'h'

    >>> decode("2abh")
    'h'

Longer patterns should work::

    >>> decode("0h1ae2bcy")
    'hey'
"""


def decode(str):
    """Decode a string."""

    i = 0
    decoded = ''

    while i < len(str):
        if str[i].isdigit():
            n_to_skip = int(str[i]) + 1
            decoded = decoded + str[i+n_to_skip]
        i += 1

    return decoded 
            
            

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; 0G1ar0e1ba0t2ab! ***\n")
