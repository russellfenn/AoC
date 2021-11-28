"""
Day 05 - Boarding Passes / Binary Search

Binary search through a field until only one row.

In the puzzle, seats on an airplane are identified with a string such as `FBFBBFFRLR`,
which describes a binary search pattern that narrows down to the individual seat.

Rows 0-127 are described by the first 7 characters

- "F" front (lower half of search space)
- "B" back (upper half of search space)

Columns 0-7 are described by the last 3 characters

- "L" left (lower half of search space)
- "R" right (upper half of search space)

"""

from math import ceil, floor
from typing import List, Set, Tuple

#--- Defines ---
MAX_ROWS = 127
MAX_COLS = 8
BOARDING_PASS_LENGTH = 10

def bisect(minimum: int, maximum: int, partition: str) -> Tuple[int]:
    if minimum == maximum:
        return (minimum, maximum)
    if partition in ['F','L']:
        return (minimum, floor((maximum - minimum) / 2 + minimum))
    elif partition in ['B','R']:
        return (ceil((maximum - minimum) / 2 + minimum), maximum)
    else:
        raise ValueError("Partition value must be one character from ['B', 'F', 'L', 'R']")


def identify_seat(pattern: str) -> int:
    """Convert a seat pattern into a seat number.
       Seat number is 8*row + column.
    """
    if len(pattern) != BOARDING_PASS_LENGTH:
        raise ValueError(f"Boarding Pass must be {BOARDING_PASS_LENGTH} characters.")

    min_row: int = 0
    max_row: int = 127
    for partition in pattern[:7]:
        min_row, max_row = bisect(min_row, max_row, partition)
    if min_row != max_row:
        raise ValueError(f"Unique row not found: {min_row} != {max_row}.")
    seat_row: int = min_row

    min_col: int = 0
    max_col: int = 7
    for partition in pattern[7:]:
        min_col, max_col = bisect(min_col, max_col, partition)
    if min_col != max_col:
        raise ValueError(f"Unique column not found: {min_col} != {max_col}.")
    seat_col = min_col

    return (8 * seat_row) + seat_col


if __name__ == "__main__":
    with open('d05.input', 'r') as f:
        boarding_passes = [l.strip() for l in f.readlines()]
    
    ###
    ### Part 1 - find the highest numbered seat
    ###
    seats: List[int] = [identify_seat(p) for p in boarding_passes]
    print(f"The hihgest numbered seat is {max(seats)}")

    ###
    ### Part 2 - find the missig seat
    ###

    # use sets to find which values are missing
    full_seats: Set[int] = set(seats)
    all_seats: Set[int] = set(range(min(full_seats), max(full_seats)))
    print(f"Using Set: all_seats - full_seats => {all_seats - full_seats}")
    
    # Let's solve an alternate way => The note for part 2 says
    # > the seats with IDs +1 and -1 from yours will be in your list.
    # This means the gap between seat numbers will be 2
    print("Looking for a gap of 2...")
    seats_s = sorted(seats)
    for i in range(len(seats_s)-1):
        if seats_s[i+1] - seats_s[i] == 2:
            print(seats_s[i-3:i+3])
