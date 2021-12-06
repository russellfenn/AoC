from d04 import BingoCard, read_puzzle_input, game, solve_part1, solve_part2
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


def test_part1_manually():
    puzzle: List[str] = [l.rstrip() for l in example_puzzle.splitlines()]
    numbers: List[int]
    cards: List[BingoCard]
    numbers , cards = read_puzzle_input(puzzle)
    index: int
    winning_card: BingoCard
    last_called_number: int
    index, winning_card, last_called_number = game(numbers, cards)
    assert winning_card.is_good_bingo()
    # 10 will be called after the winning number 24, so should still exist on the card
    assert winning_card[1][0] == 10
    # Now that we refactored to return the index as well as the card, check index
    assert index == 2
    assert winning_card.compute_score() == 188
    assert last_called_number == 24


def test_part1():
    puzzle: List[str] = [l.rstrip() for l in example_puzzle.splitlines()]
    numbers: List[int]
    cards: List[BingoCard]
    numbers , cards = read_puzzle_input(puzzle)
    assert solve_part1(numbers, cards) == 4512


def test_part2():
    puzzle: List[str] = [l.rstrip() for l in example_puzzle.splitlines()]
    numbers: List[int]
    cards: List[BingoCard]
    numbers , cards = read_puzzle_input(puzzle)
    assert solve_part2(numbers, cards) == 1924


def test_both_parts():
    """Solving part 1 mutates the cards (they are already marked),
       but we run through the numbers again -- that should be ok, as 
       re-marking a number has no effect.
       The second pass through, where we remove winning cards, likewise
       should not change the outcome of the game. Because the score is
       determined by the remaining numbers, rather than index of the card,
       we should arrive at the same answers if we play the game more than once.
    """
    puzzle: List[str] = [l.rstrip() for l in example_puzzle.splitlines()]
    numbers: List[int]
    cards: List[BingoCard]
    numbers , cards = read_puzzle_input(puzzle)
    assert solve_part1(numbers, cards) == 4512
    assert solve_part2(numbers, cards) == 1924
