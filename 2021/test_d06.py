from d06 import Lanternfish, iterate, lightweight_iterate, iterate_counter
from typing import List
from collections import Counter
import pytest

initial_ages: List[int] = [3,4,3,1,2]
day_18: List[int] = [6,0,6,4,5,6,0,1,1,2,6,0,1,1,1,2,2,3,3,4,6,7,8,8,8,8]

def test_part1_example():
    lf: List[Lanternfish] = list()
    for age in initial_ages:
        lf.append(Lanternfish(timer=age))
    # Cycle through 18 days of simulation
    for i in range(18):
        iterate(lf)
    assert len(lf) == 26
    ages: List[int] = [l.timer for l in lf]
    assert ages == day_18


def test_part1_80_days():
    lf: List[Lanternfish] = list()
    for age in initial_ages:
        lf.append(Lanternfish(timer=age))
    # Cycle through 80 days of simulation
    for i in range(80):
        iterate(lf)
    assert len(lf) == 5934


def test_heavy_vs_light_iteration():
    # Use the original Class-based implementation
    heavy_lf: List[Lanternfish] = list()
    for age in initial_ages:
        heavy_lf.append(Lanternfish(timer=age))
    # Cycle through 80 days of simulation
    for i in range(80):
        iterate(heavy_lf)
    # Now try the lighter, simple list
    light_lf: List[int] = [i for i in initial_ages]
    for i in range(80):
        lightweight_iterate(light_lf)
    assert len(heavy_lf) == 5934
    assert len(light_lf) == 5934
    heavy_ages: List[int] = [l.timer for l in heavy_lf]
    assert heavy_ages == light_lf


def test_counter_iteration_18_days():
    lf: Counter = Counter(initial_ages)
    # Cycle through 18 days
    for i in range(18):
        lf = iterate_counter(lf)
    assert sum(lf.values()) == 26
    day_18_counter: Counter = Counter(day_18)
    assert lf == day_18_counter


def test_counter_iteration_80_days():
    lf: Counter = Counter(initial_ages)
    # Cycle through 80 days
    for i in range(80):
        lf = iterate_counter(lf)
    assert sum(lf.values()) == 5934


@pytest.mark.skip()
def test_part2_lightweight():
    """This uses the lightweight iteration method,
       but still produces a gigantic list of 26 billion items.
       I got it to run to 180 iteration in 42s.
    """
    lf: List[int] = [i for i in initial_ages]
    # Cycle through 256 days of simulation
    for i in range(256):
        lightweight_iterate(lf)
    assert len(lf) == 26984457539


def test_part2_counter():
    lf: Counter = Counter(initial_ages)
    # Cycle through 256 days
    for i in range(256):
        lf = iterate_counter(lf)
    assert sum(lf.values()) == 26984457539
