from d01 import (
    Locations,
    parse_puzzle_input,
    compute_distances,
    solve_part_1,
    similarity_score,
    solve_part_2,
)
from pytest import fixture


part_1_example = """3   4
4   3
2   5
1   3
3   9
3   3
"""


@fixture
def part_1_puzzle():
    return parse_puzzle_input(part_1_example.splitlines())


def test_reading_puzzle_input(part_1_puzzle):
    left, right = part_1_puzzle
    assert len(left) == len(right)
    assert sorted(left) == [1, 2, 3, 3, 3, 4]
    assert sorted(right) == [3, 3, 3, 4, 5, 9]


def test_distances(part_1_puzzle):
    left, right = part_1_puzzle
    distances: list[int] = compute_distances(left, right)
    assert distances == [2, 1, 0, 1, 2, 5]


def test_part_1(part_1_puzzle):
    left: Locations
    right: Locations
    left, right = part_1_puzzle

    assert solve_part_1(left, right) == 11


def test_similarities(part_1_puzzle):
    left: Locations
    right: Locations
    left, right = part_1_puzzle
    similarities: list[int] = similarity_score(left, right)
    assert similarities == [9, 4, 0, 0, 9, 9]


def test_solve_part_2(part_1_puzzle):
    left: Locations
    right: Locations
    left, right = part_1_puzzle
    assert solve_part_2(left, right) == 31
