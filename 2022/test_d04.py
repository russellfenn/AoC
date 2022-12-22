from d04 import split_string_into_sets, Assignment, contains
from typing import List

example_puzzle = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""


def test_string_splitting():
    """Ensure our string split method works."""
    assert split_string_into_sets('2-4,6-8') == [{2, 3, 4}, {6, 7, 8}]
    assert split_string_into_sets('2-8,3-7') == [{2, 3, 4, 5, 6, 7, 8}, {3, 4, 5, 6, 7}]


def test_contains():
    """Just test a couple examples for the contains method."""
    assignment_1: Assignment = split_string_into_sets('2-4,6-8')
    assert contains(assignment_1) is False
    assignment_2: Assignment = split_string_into_sets('2-8,3-7')
    assert contains(assignment_2) is True


def test_examples_contains():
    """Test the example set to see if one range contains the other."""
    expected: List[bool] = [False, False, False, True, True, False]
    assignments: List[Assignment] = [split_string_into_sets(s) for s in example_puzzle.splitlines()]
    fully_contains: List[bool] = [contains(pair) for pair in assignments]
    assert fully_contains == expected
    assert sum(fully_contains) == 2


def test_non_empty_intersections():
    """Part 2 asks how many ranges overlap.
       The set intersection operator `&` should make this easy.
    """
    expected: List[bool] = [False, False, True, True, True, True]
    assignments: List[Assignment] = [split_string_into_sets(s) for s in example_puzzle.splitlines()]
    # Changed the comparison to len(inter) > 0 because
    # just getting the intersection produces `set{}` which is not "Falsey"
    intersections: List[bool] = [len(assignment[0] & assignment[1]) > 0 for assignment in assignments]
    assert intersections == expected
