from d09 import Grid, MapGrid, find_local_minima, get_basin, parse_puzzle_input, is_minima, solve_part1, Point
from typing import List, Set
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


def test_example_basins():
    grid: Grid = parse_puzzle_input(example_input.splitlines())
    mg: MapGrid = MapGrid(grid)
    minima: List[Point] = find_local_minima(grid)

    # for each minima, get it's basin
    basins: List[Set[Point]] = list()
    for m in minima:
        basins.append(get_basin(mg, m))
    basin_sizes = [len(b) for b in basins]
    assert basin_sizes == [3, 9, 14, 9]
    top_three_basins = sorted(basin_sizes)[-3:]
    assert top_three_basins == [9, 9, 14]
    assert top_three_basins[0] * top_three_basins[1] * top_three_basins[2] == 1134
