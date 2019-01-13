"""Given int, print each digit in reverse order, starting with the ones place.

For example::

    >>> print_digits(1)
    1

    >>> print_digits(413)
    3
    1
    4

    >>> print_digits(7331)
    1
    3
    3
    7

"""


def print_digits(num):
    """Given int, print digits in reverse order, starting with the ones place."""

    num_str = str(num)
    reverse_num_str = num_str[::-1]
    for digit in reverse_num_str:
        print(digit)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. WOWZA!\n")
