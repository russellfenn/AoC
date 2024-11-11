"""
Day 04 - Scratch Cards

This appears to be a set problem - the input is two sets of numbers.

## Part 1

For part 1 you need to find their intersection and score points.

## Part 2

For part 2, the card numbers become important: if card C has a N matches,
then you add copies of cards C+1..C+N. Four matches on card 10 means you
get copies of cards 11..14.

## Part 2 Example

Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53 => 4 matches
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19 => 2 matches
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1 => 2 matches
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83 => 1 matches
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36 => 0 matches
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11 => 0 matches

4 matches for card 1 earns us another copy of cards 2..4. Maybe a counter would help keep track?
"""

from collections import Counter

class Puzzle:
    """A puzzle consists of two parts:
       - a set of winning numbers
       - a set of your numbers
    """

    def __init__(self):
        self.card_number: int
        self.winning_numbers: set[int] = set()
        self.my_numbers: set[int] = set()

    def parse_puzzle_string(self, puzzle_str: str):
        """A puzzle string has two sets, separated by a pipe
        """
        card_number, card_parts = puzzle_str.split(':')
        self.card_number = int(card_number.split()[-1])
        winning_str, my_str = card_parts.split('|')
        self.winning_numbers = set([int(i) for i in winning_str.split()])
        self.my_numbers = set([int(i) for i in my_str.split()])

    def score(self) -> int:
        """The puzzle score is one point for the first
           number in the winning set, then double for
           each number after that.
        """
        intersection: int = self.matches()
        if intersection:
            return 2 ** (intersection - 1)
        else:
            return 0

    def matches(self) -> int:
        """Return the count of matching numbers"""
        return len(self.winning_numbers & self.my_numbers)


def solve_part_1(puzzle: list[Puzzle]) -> int:
    """Solve the part 1 puzzle"""
    return sum(c.score() for c in puzzle)


def puzzle_dict(puzzle: list[Puzzle]) -> dict:
    """Return a dict of [card_number, card] to simplify accounting
    """
    return {card.card_number: card for card in puzzle}


def count_part_2_cards(puzzle: list[Puzzle]) -> Counter:
    """Matches win more copies of a card.
       This does the funny algorithm to figure out how many copies of each
       card we end up with.
    """

    cnt: Counter = Counter()
    for i in range(1, len(puzzle) + 1):
        cnt[i] = 1  # add one for each of or original cards

    cardd = puzzle_dict(puzzle)  # a dict with card numbers

    for c in range(1, len(puzzle) + 1):
        card_count: int = cnt[c]  # how many copies of this card do I have?
        matches: int = cardd[c].matches()  # match count for this card
        for i in range(1, matches + 1):  # I get copies of the next #match cards
            cnt[c+i] += card_count  # add for every instance I already have
    return cnt


def solve_part_2(puzzle: list[Puzzle]) -> int:
    """Sum up the number of copies of each card.
    """
    card_stack: Counter = count_part_2_cards(puzzle=puzzle)
    return sum(card_stack.values())


if __name__ == "__main__":

    cards: list[Puzzle] = list()
    with open("d04.input", "r", encoding="UTF-8") as f:
        for card in f.readlines():
            puzzle: Puzzle = Puzzle()
            puzzle.parse_puzzle_string(card.strip())
            cards.append(puzzle)

    print(f"[Part 1] Total Points: {solve_part_1(cards)}")
    print(f"[Part 2] Total Cards: {solve_part_2(cards)} ")
