"""
Day 03 - Mull it over

Given a string of instructions, we have to parse out the valid ones
and then compute some value.

Part 1 just looks for `mul(N,N)` instructions.

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))

For now, I think a regexp will pull out the mul instructions.

But notice the `do_not_mul` part... that will probably make Part 2 much harder.
I also see at the end there are two `mul` instructions inside ().

Also note that the puzzle input is 6 very long lines. I don't know yet if the
line breaks are significant.
"""
import re


type PuzzleLine = list[tuple[int, int]]
type Puzzle = list[PuzzleLine]


def parse_part_1_input(puzzle: list[str]) -> Puzzle:
    """Our regexp does most of the work"""
    rx = re.compile(r"mul\((\d+),(\d+)\)")
    # because we have 2 captures, findall() returns
    # a list of tuples, where each is a pair of strings
    mul_strings = [rx.findall(line) for line in puzzle]
    # convert the strings to ints
    puzzle_list: list = []
    for line in mul_strings:
        puzzle_list.append([(int(l),int(r)) for l,r in line])
    return puzzle_list


def solve_part_1(puzzle: Puzzle) -> int:
    """Our parser does most of the work to split out the mul
       commands into a list of lists.
       Maybe I can use a cool itertool to flatten?
    """
    line: PuzzleLine
    sums: list[int] = []
    for line in puzzle:
        sums.append(sum([l * r for l,r in line]))
    return sum(sums)


if __name__ == "__main__":
    with open("d03.input", "r", encoding="UTF-8") as f:
        puzzle_input: Puzzle = parse_part_1_input(f.read().splitlines())
    print(f"[Part 1] Multiplication results: {solve_part_1(puzzle_input)}")
