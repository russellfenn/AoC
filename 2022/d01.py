"""
Day 01 - Counting Calories

Puzzle input is a list of numbers in groups.

The first part asks us to sum the numbers in a group, then find the largest sum.
The second part sums the top n=3 values.

Built-ins `sum`, `sorted`, `reversed` and list slicing did most of the work.


"""
from typing import List


def parse_puzzle_input(puzzle: List[str]) -> List[List[int]]:
    """Each group separated by a blank line represents an elf.
       Return a list of lists, where the inner list represents
       one elf.
    """
    all_elves: List[List[int]] = list()
    an_elf: List[int] = list()
    for line in puzzle:
        if line == "":
            all_elves.append(an_elf)
            an_elf = list()
        else:
            an_elf.append(int(line))
    all_elves.append(an_elf)  # Ensure we get the last line(s)!
    return all_elves


def solve_part_1(elf_list: List[List[int]]) -> int:
    """Sum each list and return the highest value"""
    sums = [sum(elf) for elf in elf_list]
    return max(sums)


def solve_part_2(elf_list: List[List[int]]) -> int:
    """Sum the top three values"""
    sums = [sum(elf) for elf in elf_list]
    return sum(list(reversed(sorted(sums)))[:3])


if __name__ == "__main__":
    with open('d01.input', 'r', encoding="UTF-8") as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
    puzzle = parse_puzzle_input(puzzle_input)
    print(f"[Part 1] The elf with the most calories has {solve_part_1(puzzle)}.")
    print(f"[Part 2] The top three elves have {solve_part_2(puzzle)} calories between them.")
