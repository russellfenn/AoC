"""
# Day 03 - Two-dimensional Arrays

## Given

An array representing trees (#), we need to

- expand the array: we are given a vertical slice that we need to expand horizontally
- iterate through the array with a traversal rule, like "right 3, down 1"

Part 1 is to count how many trees (#) we hit along the path.

## Strategy

Represent the grid as a List of strings: 

The example grid

```plain
..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
```

becomes `['..##.......', '#...#...#..' ...]`

"""

from typing import List
from collections import Counter


def load_grid(grid_string: str) -> List[str]:
    """Uses newlines to break the grid string into rows"""
    return grid_string.split('\n')


def expand_grid(grid: List[str], count: int) -> List[str]:
    """Return a new row with each row of the original grid copied _count_ times.
    """
    return [row * count for row in grid]


def traverse_grid(grid: List):
    x = 0
    y = 0
    for i in range(len(grid)):
        print(f"{x} {y} {grid[y][x]}")
        x += 3
        y += 1


def traverse_grid_2(grid: List[str], x: int, y:int) -> List[str]:
    result: List[str] = list()
    for i in range(len(grid)//y):
        print(f"{x*i} {y * i} {grid[y * i][x * i]}")
        result.append(grid[y * i][x * i])
    return result


def traverse_grid_3(grid: List[str], x: int, y:int) -> List[str]:
    return [grid[y * i][x * i] for i in range(len(grid)//y)]


def traverse_narrow_grid(grid: List[str], x: int, y: int) -> List[str]:
    """I realized that by using mod, there was no need to expand the grid:
       we just need to mod by the width of the grid to stay within the bounds.
    """
    width = len(grid[0])  # assume all rows are the same width
    # divide number of iterations by the y step!
    return [grid[y * i][(x * i) % width] for i in range(len(grid)//y)]


if __name__ == "__main__":

    with open('d03.input', 'r') as f:
        grid = load_grid(f.read())
    
    # See how wide we need to expand, given x=3
    expansion_factor = len(grid) // 3
    expanded_grid = expand_grid(grid, expansion_factor)

    result = traverse_narrow_grid(grid, 3, 1)
    c = Counter(result)
    print(f"We hit {c['#']} trees!")

    # Part Two - alternate slopes
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    print(f"Trying all slopes:")
    part_two: List[int] = list()
    for slope in slopes:
        c = Counter(traverse_narrow_grid(grid, *slope))
        print(f"{slope} {c['#']} trees")
        part_two.append(c['#'])
    print(part_two)
    from d01 import product
    print(f"Answer to part two: {product(part_two)}")
