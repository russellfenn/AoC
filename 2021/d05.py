"""
Day 05 Lines on a Grid

Implement a grid, and mark lines on the grid. Only horizontal and verical in part 1 (but I expect)
that to change...
If the grid is made of ints, we can count the number of lines that cross a given point with the int value
(initialize with all 0); mark the line with 1111, etc. (Marking is +=1 for each grid square we cross).


Part 2 - as expected, we now need to consider Diagonal lines, but they have simplified it for us
to only include ones at 45 degree angles. That helps!
"""

from typing import List, NamedTuple
import math
import itertools


class Point(NamedTuple):
    x: int
    y: int


class LineSegment(NamedTuple):
    start: Point
    end: Point

    def length(self) -> int:
        return math.sqrt(((self.end.y - self.start.y) ** 2) + ((self.end.x - self.start.x) ** 2))

    def orientation(self) -> str:
        if self.start.y == self.end.y:
            return "Horizontal"
        elif self.start.x == self.end.x:
            return "Vertical"
        else:
            return "Diagonal"

    def enumerate_points(self) -> List[Point]:
        """For a Horizontal or Vertical line, list all the point that
           make up the line.
           If the line segment is defined as decreasing, return the inverse.
        """
        if self.orientation() == "Diagonal":
            return self.enumerate_diagonal_points()
        if (self.start.x > self.end.x) or (self.start.y > self.end.y):
            return LineSegment(self.end, self.start).enumerate_points()
        l: List[Point] = list()
        l.append(self.start)
        if self.orientation() == "Horizontal":
            l.extend([Point(i, self.start.y) for i in range(self.start.x + 1, self.end.x)])
        elif self.orientation() == "Vertical":
            l.extend([Point(self.start.x, i) for i in range(self.start.y + 1, self.end.y)])
        l.append(self.end)
        return l

    def enumerate_diagonal_points(self) -> List[Point]:
        """Our line segment can be any of 4 directions.
           Find the delta in each direction to determine how to iterate.
        """
        delta_x: int = 0
        delta_y: int = 0
        steps: int = 0
        if self.end.x > self.start.x:
            delta_x = 1
            steps = self.end.x - self.start.x
        else:
            delta_x = -1
            steps = self.start.x - self.end.x
        if self.end.y > self.start.y:
            delta_y = 1
        else:
            delta_y = -1
        l: List[Point] = list()
        for i in range(steps):
            l.append(Point(self.start.x + (i * delta_x), self.start.y + (i * delta_y)))
        l.append(self.end)
        return l


class Grid:

    def __init__(self, x_size: int, y_size: int):
        self.x_size: int = x_size
        self.y_size: int = y_size
        self.list = list()
        for y in range(y_size):
            self.list.append([0 for i in range(x_size)])

    def mark_line(self, line: LineSegment):
        """Increment every grid square along the LineSegment."""
        if (line.start.x > self.x_size) \
            or (line.end.x > self.x_size) \
            or (line.start.y > self.y_size) \
            or (line.end.y > self.y_size):
            raise ValueError(f"{line} exceeds grid dimensions ({self.x_size},{self.y_size})")
        point: Point
        for point in line.enumerate_points():
            self.list[point.y][point.x] += 1

    def pprint(self) -> str:
        buf = ""
        for row in self.list:
            for col in row:
                buf += f"{col:02d}"
            row += "\n"
        print(buf)


def read_puzzle_input(puzzle_str: List[str]) -> List[LineSegment]:
    puzzle: List[LineSegment] = list()
    for line in puzzle_str:
        start_str, sep, end_str = line.split()
        puzzle.append(
            LineSegment(
                        Point(*[int(i) for i in start_str.split(',')]),
                        Point(*[int(i) for i in end_str.split(',')])
            )
        )
    return puzzle


def solve_part1(puzzle: List[LineSegment]):
    g: Grid = Grid(1000, 1000)
    for line in puzzle:
        if not line.orientation() == "Diagonal":
            g.mark_line(line)
    # itertools.chain.from_iterable makes all the grid rows into one long list
    return sum((1 for i in itertools.chain.from_iterable(g.list) if i >= 2))


def solve_part2(puzzle: List[LineSegment]):
    g: Grid = Grid(1000, 1000)
    for line in puzzle:
        g.mark_line(line)
    # itertools.chain.from_iterable makes all the grid rows into one long list
    return sum((1 for i in itertools.chain.from_iterable(g.list) if i >= 2))


if __name__ == "__main__":
    with open('d05.input', 'r') as f:
        puzzle: List[LineSegment] = read_puzzle_input((l.rstrip() for l in f.readlines()))

    print(f"[Part 1] {solve_part1(puzzle)} overlapping horizontal or vertical lines.")
    print(f"[Part 2] {solve_part2(puzzle)} including diagonal lines.")
