from d06 import parse_input_anyone, parse_input_everyone
from typing import List, Set

example_data: str = """abc

a
b
c

ab
ac

a
a
a
a

b"""


def test_part1_anyone():
    groups: List[Set[str]] = parse_input_anyone(example_data.splitlines())
    assert len(groups) == 5

    set_sizes: List[int] = [len(g) for g in groups]
    assert set_sizes == [3, 3, 3, 1, 1]

    assert sum(set_sizes) == 11


def test_part2_everyone():
    groups: List[Set[str]] = parse_input_everyone(example_data.splitlines())
    assert len(groups) == 5

    set_sizes: List[int] = [len(g) for g in groups]
    assert set_sizes == [3, 0, 1, 1, 1]

    assert sum(set_sizes) == 6
