import pytest
from d05 import bisect, identify_seat


def test_example_seats():
    assert identify_seat("FBFBBFFRLR") == 357
    assert identify_seat("BFFFBBFRRR") == 567
    assert identify_seat("FFFBBBFRRR") == 119
    assert identify_seat("BBFFBBFRLL") == 820


def test_bad_seat_values():
    with pytest.raises(ValueError):
        assert identify_seat("FBFBFB")
        assert identify_seat("FFFFFFFFFF") == 100