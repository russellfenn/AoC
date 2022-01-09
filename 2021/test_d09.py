from d09 import Grid, parse_puzzle_input, is_minima, solve_part1
import pytest


example_input = """2199943210
3987894921
9856789892
8767896789
9899965678
"""


def test_grid_bounds():
    grid: Grid = parse_puzzle_input(example_input.splitlines())

    for x in [-1, 40, len(grid[0]) + 1, len(grid[0])]:
        with pytest.raises(ValueError):
            is_minima(grid, x, 0)


def test_example_minima():
    """Problem text tells us (1,0), (9,0), (2,2) and (6, 4) should be minima.
    """
    grid: Grid = parse_puzzle_input(example_input.splitlines())
    for point in [(1, 0), (9, 0), (2, 2), (6, 4)]:
        assert is_minima(grid, point[0], point[1])

    # Try some other points that should NOT be minima
    for point in [(1, 1), (8, 4), (4, 3)]:
        assert not is_minima(grid, point[0], point[1])


def test_part1_example():
    grid: Grid = parse_puzzle_input(example_input.splitlines())
    assert solve_part1(grid) == 15
