"""
Day 01 - Trebuchet

## Part 1

Given a series of strings, find the first and last digit in each string
to form a 2-digit number. The puzzle answer is the sum of all the 2-digit
numbers.

Note that if a string has a single digit, it is both the first and last digit.

## Part 2

Those elves have mixed spelled out words 'one' 'two' 'three' etc into the input.
This time, iterate over the
"""


def find_digits(puzzle: list[str]) -> list[int]:
    """
    For each string in the input, find first and last digits.
    """
    output: list[int] = []
    for line in puzzle:
        digits: list[int] = [int(i) for i in line if str.isdigit(i)]
        # since we are expecting 2-digit numbers, we can
        # multiply the first by 10, then add the last
        if len(digits) > 0:
            output.append(10 * digits[0] + digits[-1])
        else:
            print(f"No digits found in '{line}'")
    return output


def solve_part_1(puzzle: list[str]) -> int:
    """Convert the input to ints, then sum"""
    return sum(find_digits(puzzle))


spelled_out_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def replace_spelled_out_digits(line: str) -> str:
    """Replace spelled out digits with their string equivalents.
       Be careful! Some values are tricky:
          "eightwothree" should be "823" -> 83,
          but of you replace the strings
          in numerical order, you end up with 23.
    """
    for digit_word, digit_str in spelled_out_digits.items():
        line = line.replace(digit_word, digit_str)
    return line


def solve_part_2(puzzle: list[str]) -> int:
    """Convert the input (words and digits) to ints, then sum"""
    converted_puzzle: list[str] = []
    for line in puzzle:
        converted_puzzle.append(replace_spelled_out_digits(line))
    return sum(find_digits(converted_puzzle))


if __name__ == "__main__":
    with open("d01.input", "r", encoding="UTF-8") as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
    print(f"[Part 1] Sum of calibration values: {solve_part_1(puzzle_input)}")
    print(f"[Part 2] Sum of calibration values: {solve_part_2(puzzle_input)}")
