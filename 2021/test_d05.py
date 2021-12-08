from d05 import Point, LineSegment, Grid, read_puzzle_input
from typing import List
import itertools

"""
0,9 -> 5,9 H
8,0 -> 0,8 D
9,4 -> 3,4 H
2,2 -> 2,1 V
7,0 -> 7,4 V
6,4 -> 2,0 D
0,9 -> 2,9 H
3,4 -> 1,4 H
0,0 -> 8,8 D
5,5 -> 8,2 D

4 horizontal, 2 vertical, 4 diagonal
"""

puzzle_input: str = """0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""


def test_read_puzzle_input():
    input_str: List[str] = [l.rstrip() for l in puzzle_input.splitlines()]
    puzzle: List[LineSegment] = read_puzzle_input(input_str)

    orientations: List[str] = [ls.orientation() for ls in puzzle]
    assert orientations == ['Horizontal', 'Diagonal', 'Horizontal', 'Vertical',
                            'Vertical', 'Diagonal', 'Horizontal',
                            'Horizontal', 'Diagonal', 'Diagonal']
    hv_lines: List[LineSegment] = [ls for ls in puzzle if not ls.orientation() == 'Diagonal']
    assert len(hv_lines) == 6
    lengths: List[float] = [ls.length() for ls in hv_lines]
    assert lengths == [5.0, 6.0, 1.0, 4.0, 2.0, 2.0]


def test_part1_grid():
    input_str: List[str] = [l.rstrip() for l in puzzle_input.splitlines()]
    puzzle: List[LineSegment] = read_puzzle_input(input_str)
    g: Grid = Grid(10, 10)
    for line in puzzle:
        if not line.orientation() == "Diagonal":
            g.mark_line(line)
    overlap: int = sum((1 for i in itertools.chain.from_iterable(g.list) if i >= 2))
    assert overlap == 5


def test_part2_grid():
    input_str: List[str] = [l.rstrip() for l in puzzle_input.splitlines()]
    puzzle: List[LineSegment] = read_puzzle_input(input_str)
    g: Grid = Grid(10, 10)
    for line in puzzle:
        g.mark_line(line)
    overlap: int = sum((1 for i in itertools.chain.from_iterable(g.list) if i >= 2))
    assert overlap == 12


def test_long_line_segment():
    puzzle: List[LineSegment] = read_puzzle_input(["734,895 -> 29,190"])
    segment: LineSegment = puzzle[0]
    assert segment.orientation() == "Diagonal"
    line_points: List[Point] = segment.enumerate_points()
    assert line_points[0] == Point(x=734, y=895)
    assert line_points[1] == Point(x=733, y=894)
    assert line_points[-1] == Point(x=29, y=190)
    assert line_points[-2] == Point(x=30, y=191)
    assert len(line_points) == 706
