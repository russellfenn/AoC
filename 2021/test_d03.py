from d03 import bit_counter, calc_gamma_rate, calc_epsilon_rate, co2_scrubber_rating, oxygen_generator_rating, solve_part2
from typing import List
from collections import Counter

example_bytes = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""


def test_part1_example():
    byte_strings: List[str] = example_bytes.splitlines()
    c_list: List[Counter] = bit_counter(byte_strings)
    assert len(c_list) == 5

    gamma: int = calc_gamma_rate(c_list)
    epsilon: int = calc_epsilon_rate(c_list)
    assert gamma == 22
    assert epsilon == 9


def test_part2_example():
    puzzle_input: List[str] = example_bytes.splitlines()
    oxygen:int = oxygen_generator_rating(puzzle_input)
    assert oxygen == 23
    co2: int = co2_scrubber_rating(puzzle_input)
    assert co2 == 10
    assert solve_part2(puzzle_input) == 230