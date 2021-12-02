"""
2021 Day 01

Given a list of numbers, determine if a number is larger than the prior number.

Will implement as a List[int] and do a list comprehension. Like one of the 2020 puzzles,
we can use the hack that sum([True]) == 1 to count the number of increases.
"""

from typing import List

Depths = List[int]  # Type Alias


def count_increases(depths: Depths) -> int:
    increases: List[bool] = [depths[i] > depths[i-1] for i in range(1, len(depths))]
    return sum(increases)


def sum_sliding_window(depths: Depths, window_size: int = 3) -> List[int]:
    """Make a new list, where each value is the sum of [window_size] successive entries.
       The returned list will be shorter than the original by window_size-1.
    """
    return [sum(depths[i:i+window_size]) for i in range(len(depths) - window_size + 1)]


def solve_part1(depths: Depths) -> int:
    return count_increases(depths)


def solve_part2(depths: Depths) -> int:
    window_depths: Depths = sum_sliding_window(depths, window_size=3)
    return count_increases(window_depths)


if __name__ == "__main__":
    with open('d01.input', 'r') as f:
        depths: Depths = [int(i) for i in f.readlines()]
   
    print(f"[Part 1] There were {solve_part1(depths)} increases in depth.")
    print(f"[Part 2] With sliding window=3, {solve_part2(depths)} increases in depth.")
