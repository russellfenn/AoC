"""
Day 01 - Historian Hysteria

The puzzle input is two of lists of integers.
First sort each list, then pair up the numbers and find their differences.

The part 1 answer is the sum of the differences. It's not clear yet if we need to 
find the absolute value of the differences, but we probably do.

Part 2 asks us to do some counting. No need to sort this time.
A Counter seems perfect for this part.
"""
from collections import Counter

type Locations = list[int]


def parse_puzzle_input(puzzle: list[str]) -> tuple[Locations, Locations]:
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


def similarity_score(left: Locations, right: Locations) -> list[int]:
    """Similarity is the number from the left list,
       multiplied by the it's count in the right list.
    """
    counts: Counter = Counter()
    for number in right:
        counts[number] += 1
    similarities: list[int] = []
    for number in left:
        similarities.append(number * counts[number])
    return similarities


def solve_part_2(left: Locations, right: Locations) -> int:
    """Just sum the similarity scores"""
    return sum(similarity_score(left, right))


if __name__ == "__main__":
    left_in: Locations
    right_in: Locations
    with open("d01.input", "r", encoding="UTF-8") as f:
        left_in, right_in = parse_puzzle_input(f.read().splitlines())
    print(f"[Part 1] Sum of distances is {solve_part_1(left_in, right_in)}")
    print(f"[Part 2] Similarity score is {solve_part_2(left_in, right_in)}")
