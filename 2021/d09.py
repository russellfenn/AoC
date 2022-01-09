"""Day 9
Smoke Flows

We are given a grid of numbers (that represent height). The goal of part 1 is to find local minima,
by comparing to the adjacent values (up, down, left, right). On edges and corners, there are fewer
values to compare.

Model the input data as a list of lists.
"""

from typing import List, Tuple

Grid = List[List[int]]
Point = Tuple[int, int]


def parse_puzzle_input(input_lines: List[str]) -> Grid:
    grid: Grid = list()
    for line in input_lines:
        grid.append([int(i) for i in line])
    return grid


def is_minima(grid: Grid, x: int, y: int) -> bool:
    """Return true if point(x,y) is less than the minimum of adjacent locations.
       It was not clear to me from the instructions if the height of the point should
       be less than (<), or less than or equal (<=) to the surrounding points.
       With the example data set, both comparisons gave the same result!
       With the full data set, there was definitely a difference, and the correct
       answer was when the height of the point was strictly less than its neighbors.
    """
    max_x: int = len(grid[0]) - 1  # assumes all rows equal
    max_y: int = len(grid) - 1
    if x < 0 or x > max_x:
        raise ValueError(f"x value {x} out of range [0, {max_x}]")
    if y < 0 or y > max_y:
        raise ValueError(f"y value {y} out of range [0, {max_y}]")
    adjacent_points: List = list()
    # get the points left and right
    if x != 0:
        adjacent_points.append(grid[y][x-1])
    if x != max_x:
        adjacent_points.append(grid[y][x+1])
    # and points above and below
    if y != 0:
        adjacent_points.append(grid[y-1][x])
    if y != max_y:
        adjacent_points.append(grid[y+1][x])
    return grid[y][x] < min(adjacent_points)


def solve_part1(grid: Grid) -> int:
    # find all the minima
    minima: List[Point] = list()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_minima(grid, x, y):
                minima.append((x, y))
    print(f"Found {len(minima)} minima.")
    print(minima)
    # risk_level is height of a minima + 1
    # find the sum of risk_levels
    risk_level: int = 0
    for m in minima:
        risk_level += grid[m[1]][m[0]] + 1
    return risk_level


if __name__ == "__main__":
    from test_d09 import example_input
    example_puzzle: Grid = parse_puzzle_input(example_input.splitlines())
    print(f"[Example] Sum of risk levels: {solve_part1(example_puzzle)}")
    with open("d09.input", "r") as f:
        puzzle: Grid = parse_puzzle_input([l.rstrip() for l in f.readlines()])

    print(f"[Part 1] Sum of risk levels: {solve_part1(puzzle)}")
