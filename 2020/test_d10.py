from d10 import solve_part1
from typing import List
from collections import Counter


small_sample: List[int] = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]


def test_part1_small():
    assert len(small_sample) == 11
    c: Counter = solve_part1(small_sample)
    assert c[1] == 7
    assert c[3] == 5


large_sample: List[int] = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47,
                           24, 23, 49, 45, 19, 38, 39, 11,  1, 32,
                           25, 35,  8, 17,  7,  9,  4,  2, 34, 10, 3]


def test_part1_large():
    assert len(large_sample) == 31
    c: Counter = solve_part1(large_sample)
    assert c[1] == 22
    assert c[3] == 10
