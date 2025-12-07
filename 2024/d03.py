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

Part 2 tells us to look at the `do()` and `don't()` instructions, which tells us
to enable or disable the `mul` instructions.

If we use a regex to split AND capture the `do()` and `don't()` instructions,
we end up with a list of fragments that also contain the `do()` and `don't()`.
With this, we can iterate over the list to enable only the right fragments.
The enabled fragments can be parsed with the part_1 parser.

I kept getting part 2 wrong (my number was too high). I finally realized
that the line breaks ARE NOT significant, and the do/don't enable/disable
carries over from one line to the next (I had been enabling it at the start
of each line, instead of just at the start of the puzzle). Fortunately,
it was pretty easy to fix, and that produced the right answer.
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


do_dont_rx = re.compile(r"(do\(\))|(don't\(\))")


def parse_part_2_input(puzzle: list[str]) -> Puzzle:
    """This time we first split on do() and don't()
    """
    instruction_list: list = []
    enabled: bool = True  # always enabled at the start of the input
    for line in puzzle:
        fragments: list[str] = do_dont_rx.split(line)

        for fragment in fragments:
            if fragment is None:
                continue
            if enabled and "mul(" in fragment:
                instruction_list.append(fragment)
                # print(f"Adding {fragment=}")
            elif fragment == "don't()":
                enabled = False
            elif fragment == "do()":
                enabled = True
            # print(f"Instructions {enabled=}")

    # feed into the part_1 parser
    return parse_part_1_input(instruction_list)


def solve_part_2(puzzle: Puzzle) -> int:
    """After parsing, the input is just a subset
       of the part 1 puzzle, so we can use that solver.
    """
    return solve_part_1(puzzle)


if __name__ == "__main__":
    with open("d03.input", "r", encoding="UTF-8") as f:
        puzzle_input: Puzzle = parse_part_1_input(f.read().splitlines())
    print(f"[Part 1] Multiplication results: {solve_part_1(puzzle_input):15d}")
    # read the input again and use the other parser
    with open("d03.input", "r", encoding="UTF-8") as f:
        puzzle_input: Puzzle = parse_part_2_input(f.read().splitlines())
    print(f"[Part 2] Use do/don't instructions: {solve_part_2(puzzle_input):12d}")
