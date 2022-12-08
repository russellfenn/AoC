"""
Day 02 - Rock, Paper, Scissors

We are given a "strategy guide" for Rock, Paper, Scissors

Rock     A, X, 1
Paper    B, Y, 2
Scissors C, Z, 3

Scoring: Win=6, Draw=3, Lose=0

            Opponent  Your Play  Outcome Score
A Y         Rock      Paper      Win     2+6=8
B X         Paper     Rock       Lose    1+0=1
C Z         Scissors  Scissors   Draw    3+3=6

For part 1, let's try making a score table

    X   Y   Z
A   4   8   3
B   1   5   9
C   7   2   6

I tried to make this work with generators throughout, but it worked
with string input and failed with file input.
I would like to improve my generator game...

## Part 2

In part 2 we learn that the 2nd column tells us how the game should END:
X you need to lose, Y you need to draw, and Z means you must win.
Scoring remains the same.

Our original example input, revised:

Opponent  Outcome  Your Play  Score
A         Y  Draw  A          3
B         X  Lose  X          0
C         Z  Win   X          6

So lets make a new score table

          XLose  YDraw  ZWin
ARock     3+0    1+3    2+6
BPaper    1+0    2+3    3+6
CScissors 2+0    3+3    1+6

So our new score calculation is simply the value of the last item (X, Y, Z) and my choice (A, B, C)
X = 0, Y = 3, Z - 6

"""
from typing import Dict, List, Tuple


def parse_puzzle(puzzle: str) -> Tuple[str]:
    """Simply splits each item, and returns it as a tuple."""
    for line in puzzle:
        them, us = line.split(' ')
        yield (them, us)


part_1_score_table: Dict[str, Dict[str, int]] = {
    "A": {"X": 4, "Y": 8, "Z": 3},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 7, "Y": 2, "Z": 6},
}


def solve_part_1(throws: List[Tuple[int]]) -> int:
    """"For part one, look up each pair of throws in the score table,
        and sum the scores.
    """
    score: int = 0
    for throw in throws:
        score += part_1_score_table[throw[0]][throw[1]]
    return score


part_2_score_table: Dict[str, int] = {
    "A": {"X": 3, "Y": 4, "Z": 8},
    "B": {"X": 1, "Y": 5, "Z": 9},
    "C": {"X": 2, "Y": 6, "Z": 7},
}


def solve_part_2(throws: List[Tuple[int]]) -> int:
    score: int = 0
    for throw in throws:
        score += part_2_score_table[throw[0]][throw[1]]
    return score


if __name__ == "__main__":
    with open("d02.input", "r", encoding="UTF-8") as f:
        puzzle = (parse_puzzle((line.rstrip() for line in f.readlines())))
    print(f"[Part 1] Following the RPS strategy guide, we score {solve_part_1(puzzle)}.")
    # And this is the problem with using a generator to read the files...
    # the second time throuh, the input is empty, so we have to read it again.
    with open("d02.input", "r", encoding="UTF-8") as f:
        puzzle = (parse_puzzle((line.rstrip() for line in f.readlines())))
    print(f"[Part 2] With the XYZ respresenting outcome, our score is {solve_part_2(puzzle)}.")
