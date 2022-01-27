"""
Day 10 - Joltage Adapters

# Part 1

Given a list of 'joltages', put the list in order, then determine the
differences between each one.
For this part, simply sorting numerically seems to be ok. It's hard to
believe they went through such an elaborate set-up for something this 
simple, so I expect part 2 will throw a big twist.
"""

from typing import List
from collections import Counter
from functools import reduce
from operator import mul


def solve_part1(adapters: List[int]) -> Counter:
    chain: List[int] = sorted(adapters)
    chain.insert(0, 0)  # add the charging outlet
    chain.append(max(chain) + 3)  # add your device

    joltage_diffs: List[int] = [chain[i + 1] - chain[i] for i, _ in enumerate(chain[:-1])]
    c = Counter()
    c.update(joltage_diffs)
    return c


if __name__ == "__main__":

    with open('d10.input', 'r') as f:
        puzzle: List[int] = [int(i) for i in f]
    s1: Counter = solve_part1(puzzle)
    print(f"[Part 1] {s1[1]} one-jolt deltas, {s1[3]} three-jolt deltas. Solution is {reduce(mul, s1.values())}")
