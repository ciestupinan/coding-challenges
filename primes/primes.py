"""Return count number of prime numbers, starting at 2.

For example::

    >>> primes(0)
    []

    >>> primes(1)
    [2]

    >>> primes(5)
    [2, 3, 5, 7, 11]

"""


def primes(num_primes):
    """Return count number of prime numbers, starting at 2.
    Assume list of integers for potential prime numbers goes to 100."""

    if num_primes == 0:
        return []

    list_of_primes = []
    
    for i in range(2,101):
        if is_prime(i):
            list_of_primes.append(i)

        if len(list_of_primes) == num_primes:
            return list_of_primes


def is_prime(num):
    """Returns True if number is prime"""
    factors = []

    for i in range(1,num+1):
        if num % i == 0:
            factors.append(i)

    if len(factors) > 2:
        return False
    return True



if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")
