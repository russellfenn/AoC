"""Day 9
Smoke Flows / Basins

We are given a grid of numbers (that represent height). The goal of part 1 is to find local minima,
by comparing to the adjacent values (up, down, left, right). On edges and corners, there are fewer
values to compare.

Model the input data as a list of lists.
"""

from typing import List, Set, Tuple
from collections import namedtuple

Grid = List[List[int]]
# Point = Tuple[int, int]
Point = namedtuple('Point', ['x','y'])


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


def find_local_minima(grid: Grid) -> List[Point]:
    """Return a list of low points in the grid."""
    minima: List[Point] = list()
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if is_minima(grid, x, y):
                minima.append(Point(x, y))
    return minima


def solve_part1(grid: Grid) -> int:
    # find all the minima
    minima: List[Point] = find_local_minima(grid)
    print(f"Found {len(minima)} minima.")
    # risk_level is height of a minima + 1
    # find the sum of risk_levels
    risk_level: int = 0
    for m in minima:
        risk_level += grid[m[1]][m[0]] + 1
    return risk_level


class MapGrid:
    """Class with some access methods to simplify getting depth readings."""
    def __init__(self, grid: Grid):
        self.grid = grid
        self.max_x = len(self.grid[0]) - 1
        self.max_y = len(self.grid) -1

    def depth(self, p: Point) -> int:
        """Return the depth at the given point."""
        if p.x < 0 or p.x > self.max_x:
            raise ValueError(f"Point x value {p.x} out of range [0, {self.max_x}]")
        if p.y < 0 or p.y > self.max_y:
            raise ValueError(f"Point y value {p.y} out of range [0, {self.max_y}]")
        return self.grid[p.y][p.x]


def get_basin(mg: MapGrid, start_point: Point) -> Set[Point]:
    """Given a starting point in a MapGrid, return all points that
      lead down to that point.

      I.O.W. All points in the MapGrid surrounding the start_point whose
      depth is less than 9.
    """
    basin: Set[Point] = set([start_point])
    basin_size: int = 0
    test_point: Point   
    while True:
        basin_size = len(basin)
        for p in list(basin):  # copy to a list so we can add points without raising an exception
            # start by going left
            test_point = Point(p.x - 1, p.y)
            try:
                if mg.depth(test_point) < 9:
                    basin.add(test_point)
            except ValueError:
                pass
            # then right
            test_point = Point(p.x + 1, p.y)
            try:
                if mg.depth(test_point) < 9:
                    basin.add(test_point)
            except ValueError:
                pass
            # up
            test_point = Point(p.x, p.y - 1)
            try:
                if mg.depth(test_point) < 9:
                    basin.add(test_point)
            except ValueError:
                pass
            # down
            test_point = Point(p.x, p.y + 1)
            try:
                if mg.depth(test_point) < 9:
                    basin.add(test_point)
            except ValueError:
                pass
        # recalculate the basin size to see if we added any points
        if basin_size == len(basin):
            break
    return basin


def solve_part2(grid: Grid) -> int:
    minima: List[Point] = find_local_minima(grid)
    mg: MapGrid = MapGrid(grid)
    basins: List[Set[Point]] = list()
    for m in minima:
        basins.append(get_basin(mg, m))
    basin_sizes = [len(b) for b in basins]
    top_three_basins = sorted(basin_sizes)[-3:]
    return top_three_basins[0] * top_three_basins[1] * top_three_basins[2]


if __name__ == "__main__":
    from test_d09 import example_input
    example_puzzle: Grid = parse_puzzle_input(example_input.splitlines())
    print(f"[Example] Sum of risk levels: {solve_part1(example_puzzle)}")
    with open("d09.input", "r") as f:
        puzzle: Grid = parse_puzzle_input([l.rstrip() for l in f.readlines()])

    print(f"[Part 1] Sum of risk levels: {solve_part1(puzzle)}")
    print(f"[Part 2] Product of top three basin sizes: {solve_part2(puzzle)}")
