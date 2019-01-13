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

    # >>> furthest_optimized(7, [0, 6])
    # 3

    # >>> furthest_optimized(3, [0, 1, 2])
    # 0

    # >>> furthest_optimized(3, [2])
    # 2

    # >>> furthest_optimized(3, [0])
    # 2

    # >>> furthest_optimized(6, [2, 4])
    # 2
"""


def furthest(num_holes, black_holes):
    """Find longest distance between a hole and a cafe."""

    distances = set()
    distance = 0

    for i in range(num_holes):

        distances_from_i_to_black_holes = set()

        for black_hole in black_holes:
            distances_from_i_to_black_holes.add(abs(black_hole - i))
            

        distances.add(min(distances_from_i_to_black_holes))

    return max(distances)






def furthest_optimized(num_holes, black_holes):
    pass

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; GREAT JOB!\n")
