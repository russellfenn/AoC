from d01 import parse_puzzle_input, solve_part_1, solve_part_2

example_puzzle: str = """1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
"""


def test_read_example_puzzle():
    """Just test we parse the puzzle input correctly"""
    elves = parse_puzzle_input(example_puzzle.splitlines())
    assert len(elves) == 5
    assert elves[0] == [1000, 2000, 3000]
    assert elves[4] == [10000]


def test_solve_part_1():
    """Find the highest value of a group"""
    elves = parse_puzzle_input(example_puzzle.splitlines())
    solution: int = solve_part_1(elves)
    assert solution == 24000


def test_solve_part_2():
    """Find the sum of the top 3 values"""
    elves = parse_puzzle_input(example_puzzle.splitlines())
    solution: int = solve_part_2(elves)
    assert solution == 45000
