from d05 import (
    Crates,
    Instructions,
    parse_puzzle_initial_condition,
    parse_instructions,
    break_on_blank_lines,
    move_boxes_one_at_a_time,
    move_multiple_boxes,
)


example_puzzle: str = """    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2 
"""

expected_puzzle: Crates = [
    ['Z', 'N'],
    ['M', 'C', 'D'],
    ['P'],
]


def test_parse_example_puzzle():
    """parse out just the puzzle portion into stacks of crates"""
    raw_crates: list[str]
    raw_instructions: list[str]
    raw_crates, raw_instructions = break_on_blank_lines(example_puzzle.splitlines())
    crates: Crates = parse_puzzle_initial_condition(raw_crates)
    print(crates)
    assert crates == expected_puzzle


expected_instructions: Instructions = [
    (1, 2, 1),
    (3, 1, 3),
    (2, 2, 1),
    (1, 1, 2),
]


def test_parse_example_instructions():
    """parse just the instructions part of our example"""
    example_lines: list[str] = [line.rstrip() for line in example_puzzle.splitlines()]
    example_instructions: list[str] = example_lines[-4:]
    parsed_instructions: Instructions = parse_instructions(example_instructions)

    assert parsed_instructions == expected_instructions


def test_split_puzzle_from_instructions():
    """Just ensure the split works properly."""
    raw_crates: list[str]
    raw_instructions: list[str]
    raw_crates, raw_instructions = break_on_blank_lines(example_puzzle.splitlines())

    assert len(raw_crates) == 4
    assert len(raw_instructions) == 4


expected_part_1_final_crates = [
    ['C'],
    ['M'],
    ['P', 'D', 'N', 'Z'],
]

expected_part_1_solution: str = "CMZ"


def test_follow_part_1_instructions():
    """Follow the example."""
    raw_crates: list[str]
    raw_instructions: list[str]
    raw_crates, raw_instructions = break_on_blank_lines(example_puzzle.splitlines())
    crates: Crates = parse_puzzle_initial_condition(raw_crates)
    instructions: Instructions = parse_instructions(raw_instructions)
    for instruction in instructions:
        count, from_stack, to_stack = instruction
        move_boxes_one_at_a_time(count, from_stack, to_stack, crates)
    assert crates == expected_part_1_final_crates

    # find the top item on each stack
    top_crates = [crate[-1] for crate in crates]
    assert ''.join(top_crates) == expected_part_1_solution


expected_part_2_final_crates = [
    ['M'],
    ['C'],
    ['P', 'Z', 'N', 'D'],
]


expected_part_2_solution: str = "MCD"


def test_follow_part_2_instructions():
    """Follow the example, moving crates in groups of count."""
    raw_crates: list[str]
    raw_instructions: list[str]
    raw_crates, raw_instructions = break_on_blank_lines(example_puzzle.splitlines())
    crates: Crates = parse_puzzle_initial_condition(raw_crates)
    instructions: Instructions = parse_instructions(raw_instructions)
    for instruction in instructions:
        count, from_stack, to_stack = instruction
        move_multiple_boxes(count, from_stack, to_stack, crates)
    assert crates == expected_part_2_final_crates

    # find the top item on each stack
    top_crates = [crate[-1] for crate in crates]
    assert ''.join(top_crates) == expected_part_2_solution
