"""
Day 04 - Camp Cleanup

This is starting to look like set operations.

Use a range to define a set

ex. given 2-4,6-8
    make sets {2, 3, 4} and {6, 7, 8}

Part 1 asks us to determine if one set fully contains the other.
The 2-4,6-8 example does not, but example 2-8,3-7 does.
We can do this by finding the intersection of the sets, and if the
size of the intersection matches the size of one set, it must be 
completely contained in the other set. (Probably works if the sets are the same...)

Part 2 asks us how many pairs overlap at all, so we just need to count the number
of non-empty intersections.
"""

from typing import List, Set

Assignment = List[Set[int]]  # Type Alias


def split_string_into_sets(pair_str: str) -> Assignment:
    """Convert from a string of ranges in a List if Sets
       Ex. '2-4,6-8' -> [{2, 3, 4}, {6, 7, 8}]
    """
    return_list: Assignment = []
    range_strings: List[str] = pair_str.split(',')  # should be 2 range_strings
    for range_str in range_strings:
        low, high = range_str.split('-')
        return_list.append(set(range(int(low), int(high) + 1)))
    return return_list


def contains(pairs: Assignment) -> bool:
    """If the size if the intersection is the same as the size
       of the smaller set, that set must be completely 
       contained within the larger set.
    """
    sizes: List[int] = [len(s) for s in pairs]
    intersect_size: int = len(pairs[0] & pairs[1])
    return intersect_size in sizes


def solve_part_1(puzzle: List[Assignment]) -> int:
    """Count the number of pairs where one range
       completely contains the other.
    """
    assignments: List[Assignment] = (split_string_into_sets(s) for s in puzzle)
    fully_contains: List[bool] = [contains(pair) for pair in assignments]
    return sum(fully_contains)


def solve_part_2(puzzle: List[Assignment]) -> int:
    """Count the number of intersecting pairs."""
    assignments: List[Assignment] = (split_string_into_sets(s) for s in puzzle)
    intersections: List[bool] = [len(assignment[0] & assignment[1]) > 0 for assignment in assignments]
    return sum(intersections)


if __name__ == "__main__":
    with open("d04.input", "r", encoding="UTF-8") as f:
        puzzle = (line.rstrip() for line in f.readlines())
    print(f"[Part 1] Count of the completely contained ranges is {solve_part_1(puzzle)}")
    with open("d04.input", "r", encoding="UTF-8") as f:
        puzzle = (line.rstrip() for line in f.readlines())
    print(f"[Part 2] Count of intersecting ranges is {solve_part_2(puzzle)}")
