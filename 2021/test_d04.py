from d04 import BingoCard, read_puzzle_input, game
from typing import List

example_puzzle = """7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""


def test_reading_puzzle_input():
    puzzle: List[str] = [l.rstrip() for l in example_puzzle.splitlines()]
    numbers: List[int]
    cards: List[BingoCard]
    numbers , cards = read_puzzle_input(puzzle)
    assert len(numbers) == 27
    assert len(cards) == 3


def test_part1():
    puzzle: List[str] = [l.rstrip() for l in example_puzzle.splitlines()]
    numbers: List[int]
    cards: List[BingoCard]
    numbers , cards = read_puzzle_input(puzzle)
    winning_card: BingoCard
    last_called_number: int
    winning_card, last_called_number = game(numbers, cards)
    assert winning_card.is_good_bingo()
    # 10 will be called after the winning number 24, so should still exist on the card
    assert winning_card[1][0] == 10
    assert winning_card.compute_score() == 188
    assert last_called_number == 24
