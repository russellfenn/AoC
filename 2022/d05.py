"""
Day 05 - Supply Stacks

        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3

Parsing may be a bit tricky, given the lack of separators for empty slots.
Maybe it will be simpler to find the stack numbers (digits) from the last
row of input, then use those positions to pluck the crate values out.


Seems like using a List as a stack with insert() and pop() may help.
"""

Crates = list[list[str]]
Instructions = list[tuple[int, int, int]]  # (Count, From, To)


def break_on_blank_lines(input: list[str]) -> list[str]:
    """Our puzzle inputs are separated by blanks"""
    output: list[str] = list()
    buffer: list[str] = list()
    for line in input:
        if line.rstrip() == "":
            output.append(buffer)
            buffer = list()
        else:
            buffer.append(line.rstrip())
    if buffer:
        output.append(buffer)
    return output


def split_puzzle_from_instructions(input: list[str]) -> tuple[list[list[str]], list[list[str]]]:
    """The puzzle initial condition and the instructions are separated by a blank line.
    """
    puzzle_list: list[str] = list()
    instructions_list: list[str] = list()

    # lines up to the blank line should be the puzzle
    # remaining lines should be instructions
    return puzzle_list, instructions_list


def parse_puzzle_initial_condition(puzzle: list[str]) -> Crates:
    """Take a puzzle given as
        [D]    
    [N] [C]    
    [Z] [M] [P]
     1   2   3

    and return a list of lists of letters
    [
        ['Z', 'N'],
        ['M', 'C', 'D'],
        ['P']
    ]
    """
    # start by popping the stack numbers off the list
    stack_line = puzzle.pop()
    stack_offsets: list[int] = [offset for offset, num in enumerate(stack_line) if num.isdigit()]
    crates: Crates = list()
    # make the empty crates
    for offset in stack_offsets:  # here we don't care aboiut values, just the count
        crates.append(list())
    # next reverse the list so we start from the bottom of each stack
    rev_puzzle: list[str] = list(reversed(puzzle))
    # now fill the stacks
    for line in rev_puzzle:
        for index, offset in enumerate(stack_offsets):
            if len(line) >= offset and line[offset] != ' ':
                crates[index].append(line[offset])
    return crates


def parse_instructions(raw_instructions: list[str]) -> Instructions:
    """The remainder of the puzzle input are the instructions.
    An instruction line is "move <Count> from <From> to <To>"
    We should be able to simply split the line, and convert each of the numbers to int.

    move 1 from 2 to 1
    move 3 from 1 to 3

    becomes => [(1, 2, 1), (3, 1, 3)]
    """
    instructions: Instructions = list()
    for raw_instruction in raw_instructions:
        parts = raw_instruction.split(' ')
        instructions.append(
            (int(parts[1]), int(parts[3]), int(parts[5]))
        )
    return instructions


def move_boxes_one_at_a_time(count: int, from_stack: int, to_stack: int, crates: Crates):
    """Move boxes one at a time from one stack to another"""
    for i in range(count):
        box = crates[from_stack - 1].pop()
        crates[to_stack - 1].append(box)


def solve_part_1(puzzle: list[str]) -> str:
    """Rearrange the given crates according to the puzzle instructions.
       Return a string with the top crates.
    """
    raw_crates: list[str]
    raw_instructions: list[str]
    raw_crates, raw_instructions = break_on_blank_lines(puzzle)
    crates: Crates = parse_puzzle_initial_condition(raw_crates)
    instructions: Instructions = parse_instructions(raw_instructions)
    for instruction in instructions:
        count, from_stack, to_stack = instruction
        move_boxes_one_at_a_time(count, from_stack, to_stack, crates)
    top_crates: list[str] = [crate[-1] for crate in crates]
    return ''.join(top_crates)


def move_multiple_boxes(count: int, from_stack: int, to_stack:int, crates: Crates):
    """This time, move count boxes at a time.
       Unfortunately, we cannot pop more than one item from a list,
       but we can slice out N items, then delete N.
       And remember to use .extend() rather than .append()!
    """
    boxes: list[str] = crates[from_stack -1 ][- count:]
    crates[to_stack - 1].extend(boxes)
    del crates[from_stack - 1][- count:]


def solve_part_2(puzzle: list[str]) -> str:
    """Rearrange the given crates according to the puzzle instructions,
       this time moving groups of _count_ boxes at a time.
       Return a string with the top crates.
    """
    raw_crates: list[str]
    raw_instructions: list[str]
    raw_crates, raw_instructions = break_on_blank_lines(puzzle)
    crates: Crates = parse_puzzle_initial_condition(raw_crates)
    instructions: Instructions = parse_instructions(raw_instructions)
    for instruction in instructions:
        count, from_stack, to_stack = instruction
        move_multiple_boxes(count, from_stack, to_stack, crates)
    top_crates: list[str] = [crate[-1] for crate in crates]
    return ''.join(top_crates)


if __name__ == "__main__":
    with open("d05.input", "r", encoding="UTF-8") as f:
        puzzle = (line.rstrip() for line in f.readlines())
    print(f"[Part 1] The top items on the stacks are: {solve_part_1(puzzle)}")
    with open("d05.input", "r", encoding="UTF-8") as f:
        puzzle = (line.rstrip() for line in f.readlines())
    print(f"[Part 2] The top items on the stacks are: {solve_part_2(puzzle)}")
