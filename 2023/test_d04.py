"""Test Day 04"""
from d04 import Puzzle, solve_part_1
from pytest import fixture

example_cards = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""


@fixture
def part_1_example_puzzle() -> list[Puzzle]:
    cards: list[Puzzle] = list()
    for card_str in example_cards.splitlines():
        puzzle: Puzzle = Puzzle()
        puzzle.parse_puzzle_string(card_str)
        cards.append(puzzle)
    return cards


def test_parse_and_score_cards():
    cards: list[Puzzle] = list()
    for card in example_cards.splitlines():
        puzzle: Puzzle = Puzzle()
        puzzle.parse_puzzle_string(card)
        cards.append(puzzle)
    assert len(cards) == 6
    scores: list[int] = [c.score() for c in cards]
    assert scores == [8, 2, 2, 1, 0, 0]
    assert sum(scores) == 13


def test_solve_part_1(part_1_example_puzzle):
    """Solve with the real method this time"""
    assert solve_part_1(part_1_example_puzzle) == 13


def test_card_numbers(part_1_example_puzzle):
    """Verify that we parse card numbers correctly.
       These will be important for part 2...
    """
    card_numbers: list[int] = [c.card_number for c in part_1_example_puzzle]
    assert card_numbers == [1, 2, 3, 4, 5, 6]
