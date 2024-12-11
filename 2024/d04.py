"""
Day 04 - Ceres Search - XMAS Word Search

A grid puzzle.

Since we are looking just for the word 'XMAS' in any direction,
I think it makes sense to scan over the grid looking for 'X' and
ignoring any other letter.
"""

from dataclasses import dataclass
from enum import StrEnum
from typing import Self

type Coordinate = tuple[int, int]  # a coordinate on a 2d plane
Directions = StrEnum('Directions', ['E', 'SE', 'S', 'SW', 'W', 'NW', 'N', 'NE'])


@dataclass(frozen=True)
class Cell:
    "A simple cell with x,y coordinates and a value"
    x: int = 0
    y: int = 0
    value: str = ''

    def neighbor(self, direction: str) -> Coordinate:
        """Return the coordinates of a neighbor cell in the given direction
        """
        if direction not in Directions:
            raise ValueError(f"{direction} is not a valid direction")
        neighbor_x: int = self.x
        neighbor_y: int = self.y
        if 'n' in direction:
            neighbor_y = self.y - 1
        if 'e' in direction:
            neighbor_x = self.x + 1
        if 's' in direction:
            neighbor_y = self.y + 1
        if 'w' in direction:
            neighbor_x = self.x - 1
        return (neighbor_x, neighbor_y)

    def is_neighbor(self, c: Self) -> bool:
        """Is the Cell my neighbor?
           The distance between neighbor Cells is 0 or 1 in either direction.
        """
        if (abs(c.x - self.x) <= 1) and (abs(c.y - self.y) <= 1):
            return True
        return False

    def coordinate(self) -> Coordinate:
        """Return the coordinates of this Cell as a tuple"""
        return (self.x, self.y)


class Grid:
    """A grid of cells"""

    def __init__(self):
        self.cells: list[list[Cell]] = []
        self.x_max: int = 0
        self.y_max: int = 0

    def load_grid(self, puzzle_str: list[str]):
        """Convert the raw puzzle input into a grid
        """
        y: int = 0
        for line in puzzle_str:
            x: int = 0
            row: list[Cell] = []
            for character in line:
                row.append(Cell(x=x, y=y, value=character))
                x += 1
            self.cells.append(row)
            self.x_max = x -1  # we already incremented
            y += 1
        self.y_max = y -1  # we already incremented

    def get(self, x: int, y: int) -> Cell:
        """Get the cell at the given coordinates"""
        if x < 0 or x > self.x_max or y < 0 or y > self.y_max:
            raise ValueError(f"Out of bounds ({self.x_max}, {self.y_max})")
        return self.cells[y][x]  # remember they look 'backwards' here

    def gett(self, coorinate: Coordinate) -> Cell:
        """Allows us to pass a tuple we get from Cell"""
        return self.get(coorinate[0], coorinate[1])


if __name__ == "__main__":
    with open("d04.input", "r", encoding="UTF-8") as f:
        puzzle_grid: Grid = Grid()
        puzzle_grid.load_grid(f.read().splitlines())

