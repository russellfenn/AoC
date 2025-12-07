"""Test 2024 Day 04"""
from d04 import (
    Cell,
    Grid,
    Directions
)
from pytest import fixture, raises


PART_1_EXAMPLE = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
"""


def test_basic_cell_functions():
    """Very basic tests of a Cell"""
    c1: Cell = Cell(0, 0, 'X')
    c2: Cell = Cell(1, 1, 'M')
    c3: Cell = Cell(1, 2, 'M')

    assert c1.is_neighbor(c2)
    assert not c1.is_neighbor(c3)
    assert c1.neighbor('e') == (1, 0)
    assert c3.neighbor('n') == (1, 1)

    with raises(ValueError):
        c3.neighbor('d')


@fixture
def example_1_grid():
    """Load the example grid"""
    grid: Grid = Grid()
    grid.load_grid(PART_1_EXAMPLE.splitlines())
    return grid


def test_load_grid(example_1_grid):
    """We expect a 10x10 grid.
       Check the bounds and a few known values.
    """
    assert len(example_1_grid.cells) == 10
    assert example_1_grid.x_max == 9
    assert example_1_grid.y_max == 9
    assert example_1_grid.cells[0][0] == Cell(x=0, y=0, value='M')


def test_get_cells(example_1_grid):
    """Basic accessor
       Test known cells from the example grid
    """
    assert example_1_grid.get(0, 0) == Cell(0, 0, 'M')
    assert example_1_grid.get(5, 0) == Cell(5, 0, 'X')


def test_find_cells(example_1_grid):
    """
    See if we can find cells with 'X' in them
    """
    x_cells: list[Cell] = []
    for y in range(example_1_grid.y_max + 1):
        for x in range(example_1_grid.x_max + 1):
            if example_1_grid.get(x, y).value == 'X':
                x_cells.append(example_1_grid.get(x, y))
    
    assert len(x_cells) == 19   # there are 19 'X's
