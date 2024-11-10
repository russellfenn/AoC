"""
Day 04 - Scratch Cards

This appears to be a set problem - the input is two sets, and you need to find their intersection.
"""


class Puzzle:
    """A puzzle consists of two parts:
       - a set of winning numbers
       - a set of your numbers
    """

    def __init__(self):
        self.winning_numbers: set[int] = set()
        self.my_numbers: set[int] = set()

    def parse_puzzle_string(self, puzzle: str):
        """A puzzle string has two sets, separated by a pipe
        """
        _, puzzle_str = puzzle.split(':')  # remove the card number
        winning_str, my_str = puzzle_str.split('|')
        self.winning_numbers = set([int(i) for i in winning_str.split()])
        self.my_numbers = set([int(i) for i in my_str.split()])
    
    def score(self) -> int:
        """The puzzle score is one point for the first
           number in the winning set, then double for
           each number after that.
        """
        intersection: int = len(self.winning_numbers & self.my_numbers)
        if intersection:
            return 2 ** (intersection - 1)
        else:
            return 0


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
