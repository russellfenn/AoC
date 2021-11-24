from d03 import *
from collections import Counter

example_grid = """..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#"""

def test_load_and_expand():
    grid = load_grid(example_grid)
    expanded_grid = expand_grid(grid, 3)
    # Grid should remain same number of rows
    assert len(expanded_grid) == len(grid)
    # Each row should be longer
    assert len(expanded_grid[0]) == len(grid[0]) * 3


def test_traversal():
    grid = load_grid(example_grid)
    # How many times do we need to expand?
    factor = len(grid) // 3  + 1  # our rule says right 3
    expanded = expand_grid(grid, factor)
    result = traverse_grid_2(expanded, 3, 1)
    # Use a counter to see how many trees we hit
    c = Counter(result)
    assert c['#'] == 7
    assert c['.'] == 4

def test_traversal_3():
    grid = load_grid(example_grid)
    # How many times do we need to expand?
    factor = len(grid) // 3  + 1  # our rule says right 3
    expanded = expand_grid(grid, factor)
    result = traverse_grid_3(expanded, 3, 1)
    # Use a counter to see how many trees we hit
    c = Counter(result)
    assert c['#'] == 7
    assert c['.'] == 4


def test_narrow_traversal():
    grid = load_grid(example_grid)
    result = traverse_narrow_grid(grid, 3, 1)
    # Use a counter to see how many trees we hit
    c = Counter(result)
    assert c['#'] == 7
    assert c['.'] == 4


def test_alternate_slopes():
    """Try alternate slopes to see if we hit fewer trees"""
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2),
    ]

    grid = load_grid(example_grid)
    results: List = list()
    for slope in slopes:
        c = Counter(traverse_narrow_grid(grid, *slope))
        results.append(c['#'])  # Number of trees hit
    assert results == [2, 7, 3, 4, 2]
    