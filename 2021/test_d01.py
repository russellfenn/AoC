from d01 import Depths, count_increases, solve_part1, sum_sliding_window, solve_part2
from typing import List


example_depths_str: str = """199
200
208
210
200
207
240
269
260
263
"""

def test_part1_count_increases():
    depths: Depths = [int(i) for i in example_depths_str.splitlines()]
    assert count_increases(depths) == 7
    assert solve_part1(depths) == 7


def test_part2_sliding_window_increases():
    depths: Depths = [int(i) for i in example_depths_str.splitlines()]
    window_depths: Depths = sum_sliding_window(depths, window_size=3)
    assert window_depths == [607, 618, 618, 617, 647, 716, 769, 792]
    assert count_increases(window_depths) == 5
    assert solve_part2(depths) == 5
