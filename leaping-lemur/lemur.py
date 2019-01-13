"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5

    >>> lemur([0,0,1,0,0,0,0,1,0,0])
    6

    >>> lemur([0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,0,1,0,1,0,0])
    28
"""


def  lemur(branches):
    """Return number of jumps needed.

    Assume first and last branch will always be alive, and there
    will never be two dead branches in a row.
    Dead branches = 1, alive branches = 0
    """

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"

    path = set()
    for i in range(len(branches)):
        if branches[i] == 1:
            pass
        elif (i+1) in range(len(branches)) and (i+2) in range(len(branches)):
            if branches[i+2] == 0 and not (i+2) in path and not (i+1) in path:
                # jump to this branch
                path.add(i+2)
            elif branches[i+2] == 1 and not (i+1) in path:
                # jump to previous branch
                path.add(i+1)

        elif (i+1) in range(len(branches)):
            if branches[i+1] == 0 and not (i+1) in path:
                path.add(i+1)

    return len(path)






if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. NICE JUMPING!\n")