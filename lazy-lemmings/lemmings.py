"""Lazy lemmings.

Find the farthest any single lemming needs to travel for food.

    >>> furthest(3, [0, 1, 2])
    0

    >>> furthest(3, [2])
    2

    >>> furthest(3, [0])
    2

    >>> furthest(6, [2, 4])
    2

    >>> furthest(7, [0, 6])
    3

    >>> furthest_optimized(7, [0, 6])
    3

    >>> furthest_optimized(3, [0, 1, 2])
    0

    >>> furthest_optimized(3, [2])
    2

    >>> furthest_optimized(3, [0])
    2

    >>> furthest_optimized(6, [2, 4])
    2
"""


def furthest(num_holes, black_holes):
    """Find longest distance between a hole and a cafe."""

    """ Loop through all holes
        Count # of steps needed to get to black hole from current hole
        When you get to the black hole, save distance
        Move to next i

        Return largest distance
    """

    distances = set()
    distance = 0

    for i in range(len(num_holes)):

        for j in range(i, len(num_holes)):
            if j in black_holes:
                distances.add(distance)
                distance = 0
                break
            else:
                distance += 1

    return max(distances)


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
