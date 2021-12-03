"""
Day 09 - Encoding Error

Given a list of numbers. The first P numbers are the _preamble_.
The next number must be the sum of two numbers in the first P.
The next number must be the sum of two in the prior P (sliding window).

"""

from typing import List, Set
from itertools import combinations

XmasStream = List[int]


def xmas_sum(series: XmasStream) -> XmasStream:
    """For the given series of ints
       compute the sum of every combination
    """
    return [sum(c) for c in combinations(series, 2)]


def solve_part1(series: XmasStream, window_size: int) -> int:
    """Return the first value NOT valid in the XmasStream"""
    window: XmasStream
    for i in range(len(series)-window_size):
        window = xmas_sum(series[i:i+window_size])
        if series[i+window_size] not in window:
            return series[i+window_size]  # found an invalid value, so quit
    raise ValueError("Not an invalid XMAS stream")


def solve_part2(series: XmasStream, target: int, max_window: int = 20) -> List[int]:
    """Find a contiguous set of values, of length _window_, where _window_ is 2, 3, 4, ... max_window.
       The sum of these values will equal the target.
    """
    window_size: int
    for window_size in range(2, max_window):
        for i in range(len(series) - window_size):
            if sum(series[i:i+window_size]) == target:
                return series[i:i+window_size]
    return list()  # We didn't find an answer

if __name__ == "__main__":

    with open('d09.input', 'r') as f:
        series: XmasStream = [int(i) for i in f.readlines()]
    invalid_value: int = solve_part1(series, 25)
    print(f"[Part 1] First invalid stream value is {invalid_value}")

    weak_set: List[int] = solve_part2(series, invalid_value)
    print(f"The weak set of values is {weak_set}")
    print(f"[Part 2] Encryption weakness: {min(weak_set) + max(weak_set)}")
