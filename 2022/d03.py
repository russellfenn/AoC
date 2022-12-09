"""
# Day 03 - Rucksack Reorg

## Part 1

Rucksacks container a number of items, `vJrwpWtwJgWrhcsFMMfFFhFp`.

Split the list in half to get `vJrwpWtwJgWr` and `hcsFMMfFFhFp`.
Letter `p` appears in both halves.

Lower case letters are numbered 1-26, and upper case are 27-52. Since we
have a letter `p`, the 16th letter, we count it as 16.

We can use [string.ascii_letters](https://docs.python.org/3/library/string.html#string.ascii_letters) to
figure out the position (just remember that python indexes from zero, and the puzzle
starts with 1, so we need to add 1 to the value `ascii_letters.find()` gives us)
"""

from functools import reduce
from itertools import islice
from math import floor
from string import ascii_letters
from typing import List, Iterable


def find_duplicate(sack: str) -> str:
    """Split the sack in half and return the letter
       that appears in both halves.
    """
    s1: set = set(sack[:floor(len(sack)/2)])
    s2: set = set(sack[floor(len(sack)/2):])
    return (s1 & s2).pop()


def find_intersection(sacks: List[str]) -> str:
    """Solve in a more generic way"""
    intersecting_set: set = reduce(set.intersection, [set(s) for s in sacks])
    return intersecting_set.pop()


def solve_part_1(sacks: List[str]) -> int:
    """Sum the values of the duplicate letter in each sack.
    """
    score: int = 0
    for sack in sacks:
        bottom_half: set = set(sack[:floor(len(sack)/2)])
        top_half: set = set(sack[floor(len(sack)/2):])
        score += ascii_letters.find(find_intersection([top_half, bottom_half])) + 1
    return score


def batched(iterable: Iterable, batch_size: int) -> List:
    """Batch data into lists of length batch_size.
       The last batch may be shorter.
       From [itertools recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes)
    """
    if batch_size < 1:
        raise ValueError("batch_size must be at least one")
    it = iter(iterable)
    while (batch := list(islice(it, batch_size))):
        yield batch


def solve_part_2(sacks: List[str]) -> int:
    """Split into groups of 3, then find the common letter.
       Return the sum of the indexes of the common letter,
       similar to part_1.
    """
    score: int = 0
    for group in batched(sacks, 3):
        score += ascii_letters.find(find_intersection(group)) + 1
    return score


if __name__ == "__main__":
    with open("d03.input", "r", encoding="UTF-8") as f:
        # added rstrip - 
        puzzle = (line.rstrip() for line in f.readlines())
    print(f"[Part 1] Sum of the rucksack priorities (singles) is {solve_part_1(puzzle)}")
    with open("d03.input", "r", encoding="UTF-8") as f:
        puzzle = (line.rstrip() for line in f.readlines())
    print(f"[Part 2] Sum of priorities (groups of 3) is {solve_part_2(puzzle)}")
