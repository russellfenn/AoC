import pytest
from d05 import bisect, identify_seat


def test_part1_example_seats():
    assert identify_seat("FBFBBFFRLR") == 357
    assert identify_seat("BFFFBBFRRR") == 567
    assert identify_seat("FFFBBBFRRR") == 119
    assert identify_seat("BBFFBBFRLL") == 820


def test_part1_bad_seat_values():
    with pytest.raises(ValueError):
        assert identify_seat("FBFBFB")
        assert identify_seat("FFFFFFFFFF") == 100


def test_part1_as_int():
    """The RealPython article about AoC (See README) pointed out that F and R are just 0 and 1
       by other names. It's obvious now that I think about it! (I already figured out that F==L and B==R;
       my bisect method matched on either value).

       It also mentioned that the [int](https://docs.python.org/3/library/functions.html#int) function accepts
       a string value and a base.

       Together with [str.translate()](https://docs.python.org/3/library/stdtypes.html#str.translate) we can
       easily map our seats to binary numbers.

       Also, the multiplying the row by 8 is the same as shifting left 3 bits (the same 3 bits as our row encoding).

       Knowing this, we should get the same values by translating and converting binary to int.
    """
    seat_to_binary = str.maketrans({'F':'0', 'L':'0', 'B':'1', 'R':'1'})
    assert int("FBFBBFFRLR".translate(seat_to_binary), base=2) == 357
    assert int("BFFFBBFRRR".translate(seat_to_binary), base=2) == 567
    assert int("FFFBBBFRRR".translate(seat_to_binary), base=2) == 119
    assert int("BBFFBBFRLL".translate(seat_to_binary), base=2) == 820

