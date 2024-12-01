"""
Day 01 - Historian Hysteria

The puzzle input is two of lists of integers.
First sort each list, then pair up the numbers and find their differences.

The part 1 answer is the sum of the differences. It's not clear yet if we need to 
find the absolute value of the differences, but we probably do.
"""

type Locations = list[int]


def parse_puzzle_input(puzzle: list[[str]]) -> tuple[Locations, Locations]:
    """Read the puzzle input as a list of strings"""
    left: Locations = []
    right: Locations = []
    for line in puzzle:
        l, r = line.split()
        left.append(int(l))
        right.append(int(r))
    return (left, right)


def distance(left: int, right: int) -> int:
    """absolute value of the difference"""
    return abs(left - right)


def compute_distances(left: Locations, right: Locations) -> list[int]:
    """Return the distances between pairs"""
    return [distance(pair[0], pair[1]) for pair in zip(sorted(left), sorted(right))]


def solve_part_1(left: Locations, right: Locations) -> int:
    """Solve Part 1 by summing the distance between sorted pairs"""
    return sum(compute_distances(left, right))


if __name__ == "__main__":
    left: Locations
    right: Locations
    with open("d01.input", "r", encoding="UTF-8") as f:
        left, right = parse_puzzle_input(f.read().splitlines())
    print(f"[Part 1] Sum of distances is {solve_part_1(left, right)}")