"""
Day 04 - Giant Squid Bingo

From the puzzle description, it looks like we could use a BingoCard class and a few methods:

BingoCard -> The simplest is probably a List of 5 Lists of 5 ints. Marking a number is done by
replacing it with a None value. This leaves ints in the unmarked spaces, so summing them to
compute the score should be relatively easy (have to filter out the None values).

check_bingo_card -> Iterate over the rows and columns to find any that are all None values.
Return True of we find one.

mark_bingo_card -> Find any instance of the number drawn and repalce with None.

read_puzzle_input -> First line are the numbers called. Remainder are bingo cards, in groups
of 5 lines, 5 numbers per line. A blank line separates lines.

This all seems straight forward. My only concern at Part 1 is that replacing the drawn numbers with
None values will make Part 2 more difficult.
"""

import collections
from typing import List, Tuple, Union
from dataclasses import dataclass


class BingoCard(List):
    
    def __init__(self, data: List = None):
        if isinstance(data, List):
            if not len(data) == 5:
                raise ValueError("Expecting 5 lists of 5 items")
            for row in data:
                if not len(row) == 5:
                    raise ValueError("Expecting 5 lists of 5 items")
                self.append(row)
    
    def is_good_bingo(self) -> bool:
        # Rows are easier, check them first
        for row in self:
            if not any(row):
                return True
        # Check columns
        for i in range(5):
            column = [row[i] for row in self]
            if not any(column):
                return True
        return False

    def mark_number(self, number: int) -> bool:
        # We have to try each row separately
        row: int
        for row in range(5):
            try:
                i:int = self[row].index(number)
                if i >=0:
                    self[row][i] = None
                    return True
            except ValueError as e:
                pass  #
        return False
    
    def compute_score(self) -> int:
        row_scores: List[int] = list()
        row: List[int]
        for row in self:
            row_scores.append(sum([i for i in row if i]))
        return sum(row_scores)


def read_puzzle_input(puzzle: List[str]) -> Tuple[List[int], List[BingoCard]]:
    # The first line is the list of drawn numbers
    drawn: List[int] = [int(i) for i in puzzle.pop(0).split(',')]

    # The remainder is a series of Bingo cards
    bingo_cards: List[BingoCard] = list()
    card: BingoCard = BingoCard()
    for line in puzzle:
        if len(line) == 0:
            if card:
                bingo_cards.append(card)
                card = BingoCard()
            continue
        card.append([int(i) for i in line.split(' ') if i])
    if card:
        bingo_cards.append(card)  # catch last one if it does not have a blank line
    return (drawn, bingo_cards)


def game(numbers: List[int], cards: List[BingoCard]) -> Tuple[BingoCard, int]:
    for number in numbers:
        for card in cards:
            card.mark_number(number)
            if card.is_good_bingo():
                return card, number


def solve_part1(numbers: List[int], cards: List[BingoCard]):
    winning_card: BingoCard
    last_number: int
    winning_card, last_number = game(numbers, cards)
    return last_number * winning_card.compute_score()


if __name__ == "__main__":
    with open('d04.input', 'r') as f:
        numbers: List[int]
        cards: List[BingoCard]
        numbers, cards = read_puzzle_input([l.rstrip() for l in f.readlines()])

    print(f"[Part 1] Winning score is {solve_part1(numbers, cards)}")
