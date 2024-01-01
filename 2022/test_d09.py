from d09 import (
    Point,
    Puzzle,
    parse_puzzle_input,
)
from pytest import fixture


example_motions = """R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
"""

example_visited: set[tuple[int, int]] = set(
    [
        (0, 0),
        (1, 0),
        (2, 0),
        (3, 0),
        (4, 1),
        (1, 2),
        (2, 2),
        (3, 2),
        (4, 2),
        (3, 3),
        (4, 3),
        (2, 4),
        (3, 4)
    ]
)


@fixture
def example_puzzle() -> Puzzle:
    return parse_puzzle_input(example_motions.splitlines())


def test_puzzle_parser(example_puzzle):
    """Make sure we parse the input correctly"""
    assert len(example_puzzle) == 8
    assert example_puzzle[0] == ('R', 4)


def test_part_1_example_puzzle(example_puzzle):
    """Test the motions"""
    head: Point = Point(0, 0)
    tail: Point = Point(0, 0)
    for direction, distance in example_puzzle:
        head.move(direction, distance, tail)
    assert head.x == 2
    assert head.y == 2
    assert tail.x == 1
    assert tail.y == 2
    assert len(tail.visited) == 13
    assert tail.visited == example_visited
