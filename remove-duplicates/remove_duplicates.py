""" Remove duplicates in a list

For example::

    >>> remove_duplicates([6, 9, 7, 9, 2, 6, 0])
    [6, 9, 7, 2, 0]

    >>> remove_duplicates([])
    []

    >>> remove_duplicates([6, 9, 7])
    [6, 9, 7]

"""


def remove_duplicates(items):
    """Remove duplicates in the list items and return that list."""


    """Can't do this because it doesn't maintain order:
        
        return list(set(items))
    """

    existing_items = set()
    deduplicated_lst = []

    for i in range(len(items)):
        if items[i] in existing_items:
            continue
        else:
            existing_items.add(items[i])
            deduplicated_lst.append(items[i])

    return deduplicated_lst
    
if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. GREAT WORK!\n")



