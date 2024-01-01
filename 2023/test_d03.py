from d03 import (
    Grid,
)
from pytest import fixture

PART_1_EXAMPLE_PUZZLE = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


@fixture
def example_1_grid():
    grid: Grid = Grid()
    grid.load_grid(PART_1_EXAMPLE_PUZZLE.splitlines())
    return grid


def test_load_grid(example_1_grid):
    """We expect a 10x10 grid.
       Check the bounds, and a few known values.
    """
    assert len(example_1_grid.cells) == 10
    for row in example_1_grid.cells:
        assert len(row) == 10
    assert example_1_grid.x_max == 9  # zero indexed
    assert example_1_grid.y_max == 9
    assert example_1_grid.get(2, 4) == '7'
    assert example_1_grid.get(3, 4) == '*'


def test_part_1(example_1_grid):
    """Test the part 1 example"""
    found_numbers: list[int] = example_1_grid.find_numbers()
    assert found_numbers == [467, 35, 633, 617, 592, 755, 664, 598]
    assert sum(found_numbers) == 4361


# Test for numbers at the right edge. Sum=62
EDGE_CASE_GRID = """...45
12*.$
....5"""


def test_number_at_edge_of_grid():
    """My original algorithm failed to catch numbers at the right edge of the grid.
       The test sample did not contain any of these, so construct one.
    """
    grid: Grid = Grid()
    grid.load_grid(EDGE_CASE_GRID.splitlines())
    numbers = grid.find_numbers()
    assert numbers == [45, 12, 5]
