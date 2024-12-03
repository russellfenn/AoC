from d02 import (
    Report,
    Deltas,
    parse_puzzle_input,
    calc_deltas,
    is_part_1_safe,
    solve_part_1,
)
from pytest import fixture


part_1_example = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
"""


@fixture
def part_1_puzzle() -> list[Report]:
    return parse_puzzle_input(part_1_example.splitlines())


def test_puzzle_input(part_1_puzzle: list[Report]):
    assert len(part_1_puzzle) == 6


def test_part_1(part_1_puzzle: list[Report]):
    deltas: list[Deltas] = [calc_deltas(r) for r in part_1_puzzle]
    assert len(deltas[0]) == len(part_1_puzzle[0]) - 1
    assert deltas[0] == [-1, -2, -2, -1]
    safety: list[bool] = [is_part_1_safe(d) for d in deltas]
    assert safety == [True, False, False, False, False, True]


def test_solve_part_1(part_1_puzzle: list[Report]):
    assert solve_part_1(part_1_puzzle) == 2
