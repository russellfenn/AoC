from d03 import solve_part_1, solve_part_2, batched, find_intersection


example_puzzle: str = """vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""


def test_solve_part_1():
    """Score each sack as two halves"""
    score = solve_part_1((example_puzzle.splitlines()))
    assert score == 157


def test_solve_part2():
    """Score groups of 3 sacks"""
    score = solve_part_2((example_puzzle.splitlines()))
    assert score == 70


def test_part_2_groups():
    """More detailed testing of the groups"""
    groups: List = list(batched(example_puzzle.splitlines(), 3))
    assert len(groups) == 2
    assert find_intersection(groups[0]) == 'r'  # from puzzle description
    assert find_intersection(groups[1]) == 'Z'


def test_split_into_groups():
    """Verify that splitting into groups of 3 works 
       the way I think it does...
       And of course, it does NOT :-) (See README.md)
    """
    sacks = example_puzzle.splitlines()
    assert len(sacks) == 6  # this works
    # But this grabs every third item, not groups of three
    for group in sacks[::3]:
        # assert len(group) == 3
        pass
