from d09 import XmasStream, solve_part1, solve_part2
from typing import List

example_data_str = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def test_part1_example():
    series: XmasStream = [int(i) for i in example_data_str.splitlines()]
    assert solve_part1(series, 5) == 127


def test_part2_example():
    series: XmasStream = [int(i) for i in example_data_str.splitlines()]
    target: int = solve_part1(series, 5)  # should still be 127
    weak_set: List[int] = solve_part2(series, target)
    assert weak_set == [15, 25, 47, 40]
    weakness: int = min(weak_set) + max(weak_set)
    assert weakness == 62

