from d05 import (
    OrderingRules,
    PagesToProduce,
    parse_puzzle_input,
)
from chunk import chunk_list

from pytest import fixture

PART_1_EXAMPLE = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""


def test_chunk():
    chunks = chunk_list(PART_1_EXAMPLE.splitlines())
    assert len(chunks) == 2
    assert len(chunks[0]) == 21
    assert chunks[0][-1] == "53|13"
    assert len(chunks[1]) == 6
