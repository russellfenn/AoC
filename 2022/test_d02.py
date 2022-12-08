from d02 import parse_puzzle, solve_part_1, solve_part_2
from typing import List, Tuple


example_puzzle: str = """A Y
B X
C Z
"""


def test_puzzle_parser():
    """Just ensure our generator-baed parser works"""
    # we have to convert to a list to get the length
    throws: List[Tuple[int]] = list(parse_puzzle(example_puzzle.splitlines()))
    assert len(throws) == 3


def test_part_1_example():
    """Solve"""
    throws: List[Tuple[int]] = (parse_puzzle(example_puzzle.splitlines()))
    score = solve_part_1(throws)
    assert score == 15


def test_part_2_example():
    """Score by given outcome"""
    throws: List[Tuple[int]] = (parse_puzzle(example_puzzle.splitlines()))
    score = solve_part_2(throws)
    assert score == 12