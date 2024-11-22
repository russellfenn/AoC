from d05 import (
    Range,
    ElfMap,
    chunk_puzzle_input,
    parse_puzzle_input,
    solve_part_1,
)
from pytest import fixture
import sys

EXAMPLE_1_PUZZLE = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""


def test_range():
    """Now that we have a Range class, we need to test it"""
    r: Range = Range(98, 100, 98-50)
    assert not r.in_range(79)
    r2: Range = Range(50, 50+48, 52-50)
    assert r2.in_range(79)
    assert 79 + r2.offset == 81


def test_basic_elfmap():
    """Just manually test the seed_to_soil map given in the problem description"""
    seed_to_soil = ElfMap()
    seed_to_soil.add(50, 98, 2)
    seed_to_soil.add(52, 50, 48)
    assert seed_to_soil.get(79) == 81
    assert seed_to_soil.get(14) == 14
    assert seed_to_soil.get(55) == 57
    assert seed_to_soil.get(13) == 13


@fixture
def example_puzzle() -> list[str]:
    return EXAMPLE_1_PUZZLE.splitlines()


def test_chunk_puzzle(example_puzzle):
    assert len(example_puzzle) == 33
    chunks = chunk_puzzle_input(example_puzzle)
    assert len(chunks) == 8


def test_parse_puzzle(example_puzzle):
    pd = parse_puzzle_input(example_puzzle)
    assert pd["seeds"] == [79, 14, 55, 13]
    seed_to_soil = pd["seed-to-soil"]
    assert seed_to_soil.get(79) == 81
    assert seed_to_soil.get(14) == 14
    assert seed_to_soil.get(55) == 57
    assert seed_to_soil.get(13) == 13


def test_solve_part_1(example_puzzle):
    """Test the real part 1 solver"""
    puzzle_map: dict = parse_puzzle_input(example_puzzle)
    seeds: list[int] = puzzle_map['seeds']
    best_location: int = solve_part_1(puzzle_map, seeds)
    assert best_location == 35


def test_seed_ranges(example_puzzle):
    """Just test that the part 2 seed ranges
       are split properly
    """
    puzzle_map: dict = parse_puzzle_input(example_puzzle)
    seeds: list[int] = puzzle_map['seeds']  # just the plain list
    assert len(seeds) == 4


def test_solve_with_ranges(example_puzzle):
    """Solve the example in the Part 2 way"""
    puzzle_map: dict = parse_puzzle_input(example_puzzle)
    seeds: list[int] = puzzle_map['seeds']  # just the plain list
    lowest_value: int = sys.maxsize
    for i in range(0, len(seeds), 2):  # first of each pair
        for seed in range(seeds[i], seeds[i] + seeds[i+1]):
            value: int = solve_part_1(puzzle_map, [seed])
            print(f"{seed=} {value=}")
            lowest_value = min(value, lowest_value)

    assert lowest_value == 46
