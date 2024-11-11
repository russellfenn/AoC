"""
Day 04 - Scratch Cards

This appears to be a set problem - the input is two sets of numbers.
For part 1 you need to find their intersection and score points.
"""


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
    return sum([c.score() for c in puzzle])


if __name__ == "__main__":

    cards: list[Puzzle] = list()
    with open("d04.input", "r", encoding="UTF-8") as f:
        for card in f.readlines():
            puzzle: Puzzle = Puzzle()
            puzzle.parse_puzzle_string(card.strip())
            cards.append(puzzle)

    print(f"[Part 1] Total Points: {solve_part_1(cards)}")
