"""
Day 08 - Treetop Tree House

Given a (rectangular or square) grid of trees, with numbers 0-9 to represent tree height.

- All trees on the edge of the grid are visible.
- Interior trees are visible if all trees in a cardinal direction (N, S, E, W) are less than its height.

The goal is to count the number of visible trees on the grid.

- All perimeter trees, so 2X + 2(Y-2)
- Any interior trees


## Our Grid
  ------------------> X
  | (0,0) (1,0) (2,0)
  | (0,1)
  | (0,2)       (2,2)
  v
  Y
Remember that we reference this as grid[Y][X] or grid[row][column]
"""

Grid = list[list[int]]


def parse_puzzle_input(input_lines: list[str]) -> Grid:
    grid: Grid = []
    for line in input_lines:
        grid.append([int(i) for i in line])
    return grid


def get_west(grid: Grid, x: int, y: int) -> list[int]:
    """Get a list of all trees West of given tree at x,y.
       This is simply row Y from 0 to position X.
    """
    if x < 0 or y < 0:
        raise IndexError("All values must be positive")
    return grid[y][0:x]


def get_east(grid: Grid, x: int, y: int) -> list[int]:
    """Get a list of all trees East of given tree at x,y.
       This is simply row Y from position X+1 to the end.
    """
    if x < 0 or y < 0:
        raise IndexError("All values must be positive")
    return grid[y][x+1:]


def get_north(grid: Grid, x: int, y: int) -> list[int]:
    """North and South are a bit more tricky.
    """
    if x < 0 or y < 0:
        raise IndexError("All values must be positive")
    max_x: int = len(grid[0]) - 1
    max_y: int = len(grid) - 1
    if x > max_x or y > max_y:
        raise IndexError("list index out of range")
    north: list[int] = []
    for i in range(0, y):
        north.append(grid[i][x])
    return north


def get_south(grid: Grid, x: int, y: int) -> list[int]:
    """North and South are a bit more tricky.
    """
    if x < 0 or y < 0:
        raise IndexError("All values must be positive")
    max_x: int = len(grid[0]) - 1
    max_y: int = len(grid) - 1
    if x > max_x or y > max_y:
        raise IndexError("list index out of range")
    south: list[int] = []
    for i in range(y+1, max_y + 1):
        south.append(grid[i][x])
    return south


def is_visible(grid: Grid, x: int, y: int) -> bool:
    """"Return True if the tree is visible.
        Trees in the perimeter are always visible.
    """
    if x == 0 or y == 0:  # on the north or west edge
        return True
    max_x: int = len(grid[0]) - 1
    max_y: int = len(grid) - 1
    if x == max_x or y == max_y:  # on the south or east edge
        return True
    if x < 0 or y < 0:
        raise IndexError("All values must be positive")
    if x > max_x or y > max_y:
        raise IndexError("list index out of range")
    if grid[y][x] > max(get_east(grid, x, y)) \
        or grid[y][x] > max(get_west(grid, x, y)) \
        or grid[y][x] > max(get_north(grid, x, y)) \
        or grid[y][x] > max(get_south(grid, x, y)):
            return True
    return False


def viewing_distance(height: int, trees: list[int]) -> int:
    """Return the number of trees until one our height or greater"""
    for i, t in enumerate(trees):
        if t >= height:
           return i + 1
    return len(trees)


def calc_scenic_score(grid: Grid, x: int, y: int) -> int:
    """Compute the viewing distance in each direction for the
       given tree. Multiply all four values for a "scenic score".
       Remember when looking west or north, reverse the order
       of the tree list, because our reference is _from the tree_
       rather than from outside the grid.
    """
    height: int = grid[y][x]  # swap x,y
    score: int = viewing_distance(height, get_east(grid, x, y))
    score *= viewing_distance(height, get_south(grid, x, y))
    # now we have to check the list length and reverse
    trees: list[int] = get_west(grid, x, y)
    if len(trees) > 1:
        trees = list(reversed(trees))
    score *= viewing_distance(height, trees)
    trees: list[int] = get_north(grid, x, y)
    if len(trees) > 1:
        trees = list(reversed(trees))
    score *= viewing_distance(height, trees)
    return score


def solve_part1(grid: Grid) -> int:
    """Count visible trees"""
    visibility_list: list = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            visibility_list.append(is_visible(grid, x, y))
    return sum(visibility_list)


def solve_part2(grid: Grid) -> int:
    """Calculate all the scenic scores, and return the highest one"""
    all_scores: list[int] = []
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            all_scores.append(calc_scenic_score(grid, x, y))
    return max(all_scores)


if __name__ == "__main__":
    with open("d08.input", "r") as f:
        puzzle: Grid = parse_puzzle_input([l.strip() for l in f.readlines()])
    print(f"[Part 1] Visible trees: {solve_part1(puzzle)}")
    print(f"[Part 2] Max Scenic Score: {solve_part2(puzzle)}")
