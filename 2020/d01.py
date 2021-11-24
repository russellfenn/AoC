"""
Day 01
Given a list of numbers, find a pair that sums to 2020. Return the product of those numbers.
"""

import itertools
from typing import List


target_value = 2020

# Use itertools.combinataions to produce a list of all pairs

def solve_two(input_list: List[int],
              target: int = target_value,
              ) -> int:
    for c in itertools.combinations(input_list, 2):
        if c[0] + c[1] == target_value:
            print(f"{c[0]} + {c[1]} == {target_value}")
            print(f"{c[0]} * {c[1]} => {c[0] * c[1]}")
            return c[0] * c[1]


def product(inputs: List[int]) -> int:
    """We can use the built-in `sum` to sum a list,
       but there is no corresponding function for product.
    """
    accumulator = 1  # safe for multipliction
    for i in inputs:
        accumulator *= i
    return accumulator


def solve_generic(input_list: List[int],
                  target: int = target_value,
                  num_elements: int = 2,
                  ) -> int:
    """Solve in a more generic way that lets us specify
       how many elements to use in our solution.
    """
    for c in itertools.combinations(input_list, num_elements):
        if sum(c) == target_value:
            print(c)
            return product(c)


if __name__ == "__main__":
    with open('d01.input', 'r') as f:
        puzzle_input: List[int] = [int(s) for s in f.readlines()]

    # print(solve_two(puzzle_input))
    print(solve_generic(puzzle_input, target_value, 2))
    print(solve_generic(puzzle_input, target_value, 3))
