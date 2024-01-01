"""
Day 03 - Gear Ratios

## Part 1 - identify part numbers in a grid

The grid consists of numbers, periods, and other symbols.

- Part Numbers are a group of digits in consecutive cells.
- We need to identify the numbers that are adjacent to a symbol,
  but ignore ones that are NOT adjacent.

Here is an example engine schematic:

467..114..      0----->  x
...*......      |
..35..633.      |
......#...      v
617*......      y
.....+.58.
..592.....
......755.
...$.*....
.664.598..

On the first row, 467 is adjacent to the * on row 2, so we want to count 467.
But 114 is not adjacent to any other symbols, so does NOT count.
Number 58 on row 6 is the also not adjacent.

My first strategy is to treat the numbers simply as a group of digits,
only by position, and see if they are adjacent to any symbols. Once identified,
then I can convert to an int.
Eventually, we need to sum up the identified numbers.

As with most Grid puzzles, start by representing the grid as a list of lists of strings.

Decided to make a grid class to help simplify looking at the cells around a given cell.
Grid coordinates start with zero in the upper left and proceed right (x) and down (y).

Puzzle Part 1:
Sum the part numbers (numbers that are adjacent to a symbol only).
"""


class Grid:
    """A grid of cells"""

    def __init__(self):
        self.cells: list[list[str]] = []
        self.x_max: int = 0
        self.y_max: int = 0

    def load_grid(self, puzzle_str: list[str]):
        """Convert the raw puzzle input to a grid.
        No attempt to group digits into numbers.
        """
        for line in puzzle_str:
            # grid.append(line.split('')) ## This does not work! Can't split on empty string!
            self.cells.append([c for c in line])
        # Now update the size. Assume the grid is regular.
        self.y_max = len(self.cells) - 1
        self.x_max = len(self.cells[0]) -1

    def get(self, x: int, y: int) -> str:
        """Return the character at the given grid coordinates"""
        if x > self.x_max or y > self.y_max:
            raise ValueError(f"Out of bounds ({self.x_max}, {self.y_max})")
        return self.cells[y][x]

    def identify_cell(self, x: int, y: int) -> str:
        """Does the cell contain a Digit, symbol or none of those."""
        # first do some bounds checking
        if x < 0 or y < 0:
            return 'out of bounds'
        if x > self.x_max or y > self.y_max:
            return 'out of bounds'
        char: str = self.cells[y][x]
        if char.isdigit():
            return 'digit'
        if char == '.':
            return 'none'
        return 'symbol'

    def neighbors(self, x: int, y: int) -> list[str]:
        """List the cells surrounding the given cell"""
        neighbors: list[str] = []
        # The three above us
        for i in range(x-1, x+2):
            neighbors.append(self.identify_cell(i, y-1))
        # Now left and right of us
        neighbors.append(self.identify_cell(x-1, y))
        neighbors.append(self.identify_cell(x+1, y))
        # And the three below us
        for i in range(x-1, x+2):
            neighbors.append(self.identify_cell(i, y+1))
        return neighbors
    
    def check_candidates(self, candidates: list[tuple[str, bool]]) -> int:
        if True in [cn[1] for cn in candidates]:
            value = int(''.join([cn[0] for cn in candidates]))
            return value
        return 0

    def find_numbers(self) -> list[int]:
        """Scan through the grid looking for numbers.
           Our strategy will be to test each cell, starting at (0,0).
           If the cell contains a digit, remember the digit, then look
           in the neighboring cells for a symbol, remembering if one is found.
           Next look at the cell to the right - if it is a digit, then store
           and repeat the process until the cell on the right is no longer
           a digit. The Number will be valid if any of the neighbor cells contains
           a symbol, and it's value will be the accumulation of the digits.
        """
        found_numbers: list[int] = []
        for y in range(self.y_max + 1):
            candidate_numbers: list[tuple[str,bool]] = []  # tuple(number_as_str, bool_has_symbol)
            for x in range(self.x_max + 1):
                if self.identify_cell(x, y) == 'digit':
                    candidate_numbers.append(
                        (self.get(x, y), 'symbol' in self.neighbors(x, y))
                    )
                else:
                    if not candidate_numbers:
                        continue  # not in a group of candidate numbers
                    # We just moved past a group of candidates,
                    # so check for valid and calculate it's value
                    value: int = self.check_candidates(candidate_numbers)
                    if value > 0:
                        found_numbers.append(value)
                    candidate_numbers = []  # reset our candidate list
            # if we are at the last cell in a row, see if we still have candidates
            if candidate_numbers:
                value: int = self.check_candidates(candidate_numbers)
                if value > 0:
                    found_numbers.append(value)
        return found_numbers


def solve_part_1(grid: Grid) -> int:
    numbers: list[int] = grid.find_numbers()
    return sum(numbers)


if __name__ == "__main__":
    with open("d03.input", "r", encoding="UTF-8") as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
    grid: Grid = Grid()
    grid.load_grid(puzzle_input)
    print(f"[Part 1] Sum of part numbers: {solve_part_1(grid=grid)}")
