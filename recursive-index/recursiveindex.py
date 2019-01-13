"""Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.

For example:

    >>> recursive_index(5, [1, 3, 5, 2, 4])
    2

    >>> recursive_index("hey", ["hey", "there", "you"])
    0

    >>> recursive_index("you", ["hey", "there", "you"])
    2

    >>> recursive_index("zork", ["foo", "bar", "baz"]) is None
    True

"""


def recursive_index(item, lst):
    """Given list, return index (0-based) of item in the list.

    Return None if item is not in list.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """

    def find_index_of_item(item,lst,index):
        if lst:
            if item == lst[0]:
                return index
            else:
                return find_index_of_item(item,lst[1:],index+1)

    return find_index_of_item(item,lst,0)




if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GO GO GO!\n")
