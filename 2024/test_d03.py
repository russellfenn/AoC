from d03 import (
    PuzzleLine,
    Puzzle,
    parse_part_1_input,
    solve_part_1,
    parse_part_2_input,
    solve_part_2,
)

from pytest import fixture


PART_1_EXAMPLE: str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
PART_2_EXAMPLE: str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"


@fixture
def part_1_puzzle():
    return [PART_1_EXAMPLE]


@fixture
def part_2_puzzle():
    return [PART_2_EXAMPLE]


def test_parse_part_1(part_1_puzzle):
    puzzle: Puzzle = parse_part_1_input(part_1_puzzle)
    assert isinstance(puzzle, list)
    assert puzzle[0] == [(2, 4), (5, 5), (11, 8), (8, 5)]


def test_solve_part_1(part_1_puzzle):
    puzzle: Puzzle = parse_part_1_input(part_1_puzzle)
    assert solve_part_1(puzzle) == 161


def test_parse_part_2(part_2_puzzle):
    puzzle: Puzzle = parse_part_2_input(part_2_puzzle)
    assert isinstance(puzzle, list)
    assert puzzle == [[(2, 4)], [(8, 5)]]


def test_solve_part_2(part_2_puzzle):
    puzzle: Puzzle = parse_part_2_input(part_2_puzzle)
    assert solve_part_2(puzzle) == 48
