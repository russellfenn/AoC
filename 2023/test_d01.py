from d01 import (
    find_digits,
    replace_spelled_out_digits,
)

PART_1_EXAMPLE_INPUT = """1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet"""


def test_part_1_parse_example_input():
    """Part 1 - looking for digits only."""
    digits: list[int] = find_digits(PART_1_EXAMPLE_INPUT.splitlines())
    print(digits)
    assert len(digits) == 4
    assert digits[3] == 77  # this one had only one number in the string
    assert sum(digits) == 142


EXAMPLE_INPUT_WITH_STRING_NUMS = """two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
"""


def test_part_2_example_with_string_nums():
    converted_puzzle: list[str] = []
    for line in EXAMPLE_INPUT_WITH_STRING_NUMS.splitlines():
        converted_puzzle.append(replace_spelled_out_digits(line))
    digits: list[int] = find_digits(converted_puzzle)
    assert len(digits) == 7
    assert digits == [29, 83, 13, 24, 42, 14, 76]
    assert sum(digits) == 281
