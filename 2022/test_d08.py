from d08 import (
    Grid,
    parse_puzzle_input,
    get_east,
    get_west,
    get_north,
    get_south,
    is_visible,
    solve_part1,
)
from pytest import fixture, raises


example_input = """30373
25512
65332
33549
35390
"""


@fixture
def example_grid() -> Grid:
    return parse_puzzle_input(example_input.splitlines())


def test_get_west(example_grid):
    assert get_west(example_grid, 2, 3) == [3, 3]
    assert get_west(example_grid, 0, 0) == []
    assert get_west(example_grid, 4, 0) == [3, 0, 3, 7]
    with raises(IndexError):
        get_west(example_grid, 0, 5)


def test_get_east(example_grid):
    assert get_east(example_grid, 0, 4) == [5, 3, 9, 0]
    with raises(IndexError):
        get_east(example_grid, -1, 4)


def test_get_north(example_grid):
    assert get_north(example_grid, 0, 4) == [3, 2, 6, 3]
    with raises(IndexError):
        get_north(example_grid, 0, 5)


def test_get_south(example_grid):
    assert get_south(example_grid, 0, 0) == [2, 6, 3, 3]
    with raises(IndexError):
        get_south(example_grid, 0, 5)


def test_visible(example_grid):
    assert is_visible(example_grid, 0, 0) == True  # on the edge
    assert is_visible(example_grid, 1, 1) == True  # from puzzle description
    assert is_visible(example_grid, 3, 1) == False  # from puzzle description



def test_part_1_with_example(example_grid):
    """Part 1"""
    answer: int = solve_part1(example_grid)
    assert answer == 21
