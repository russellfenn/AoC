"""
Day 09 - Rope Bridge

"""
# from __future__ import annotations
from typing import Self
from collections import namedtuple

Grid = list[list[int]]  # TypeDef
Puzzle = list[tuple[str, int]]  # TypeDef

Delta = namedtuple('Delta', ['x', 'y'])

# It turns out that you cannot update the values in a namedtuple, which makes
# sense as you cannot update values in a regular tuple either (it's immutable).
# So my initial try modeling a Point with a namedtuple failed.
# Point = namedtuple('Point', ['x', 'y'])


class Point:
    """Model the point as a class"""
    x: int
    y: int
    visited: set[tuple[int, int]] = set()

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.visited.add((x, y))

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __sub__(self, p: Self) -> Delta:
        return Delta(p.x - self.x, p.y - self.y)

    def is_adjacent(self, p: Self) -> bool:
        """Are the two points next to each other, but not diagonal"""
        d: Delta = self.delta(p)
        if abs(d.x) == 0 and abs(d.y) == 1:
            return True
        if abs(d.x) == 1 and abs(d.y) == 0:
            return True
        return False

    def is_diagonal(self, p: Self) -> bool:
        """Are the two points diagonally adjacent"""
        d: Delta = self.delta(p)
        return abs(d.x) == 1 and abs(d.y) == 1

    def delta(self, p: Self) -> Delta:
        """Return the simple distance (x, y) between two Points"""
        return Delta(p.x - self.x, p.y - self.y)

    def save(self) -> None:
        """Save this point in the 'visited' set"""
        self.visited.add((self.x, self.y))

    def snap(self, p: Self) -> None:
        """If the other point is 2 steps away, move next to it."""
        if self.is_diagonal(p):
            return
        if self.is_adjacent(p):
            return
        d: Delta = self.delta(p)
        if abs(d.y) == 2:
            self.y += d.y / 2
            self.x += d.x
        if abs(d.x) == 2:
            self.x += d.x / 2
            self.y += d.y

    def move(self, direction: str, distance: int, follower: Self) -> None:
        """Move this point in the given direction"""
        if direction not in ['D', 'L', 'R', 'U']:
            raise ValueError("Invalid direction. Must be one of ['D', 'L', 'R', 'U']")
        for _ in range(distance):
            if direction == 'U':
                self.y += 1
            elif direction == 'D':
                self.y -= 1
            elif direction == 'L':
                self.x -= 1
            elif direction == 'R':
                self.x += 1
            follower.snap(self)
            follower.save()


def parse_puzzle_input(input_lines: list[str]) -> Puzzle:
    """Convert the movement instructions as a string
       to a list of direction, distance pairs
    """
    motions: Puzzle = []
    for line in input_lines:
        direction, distance = line.split(' ')
        motions.append((direction, int(distance)))
    return motions


def solve_part_1(puzzle: Puzzle) -> int:
    """Follow the puzzle motions, and return the number
       of grid locations the tail visited.
    """
    head: Point = Point(0, 0)
    tail: Point = Point(0, 0)
    for direction, distance in puzzle:
        head.move(direction, distance, tail)
    return len(tail.visited)


if __name__ == "__main__":
    with open('d09.input', 'r') as f:
        puzzle: Puzzle = parse_puzzle_input([l.strip() for l in f.readlines()])
    print(f"[Part 1] Tail visited {solve_part_1(puzzle)} locations.")
