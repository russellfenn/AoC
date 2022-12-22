"""
Day 06 - Tuning Trouble

Look for the `start-of-packet-marker` which is a set of four
characters that are all different.
My initial thought is to use a set() and ensure the length is 4,
but that may be inefficient (is that a big deal?)

Example:

mjqjpqmgbljsphdztnvjfqwrcgsmlb
   ^  ^
   4  7

Characters 4-7 are unique "jpqm", so we report that 7 is the _end_ of the start-of-packet-marker.

I used a set, and it wasn't terribly slow. My method solved all of the examples,
and the puzzle input on the first try. Sweet!

I suspected the length of the marker may change in part 2, which was a good hunch,
since it changed from 4 to 14. Since I made that a parameter, I should be able
to reuse the find_start_of_packet_marker method.
"""


def find_start_of_packet_marker(signal: str, packet_len: int = 4) -> int:
    """Find the first sequence of 4 unique characters.
       Return the index (starts with 1) of the last character.
    """
    for i in range(len(signal)):
        if len(set(signal[i:i+packet_len])) == packet_len:
            return i + packet_len
    raise ValueError("Could not find start-of-packet-marker")


def solve_part_1(puzzle: str) -> int:
    """This is kind of a waste, since it's really just a call to 
       a separate method, but this fits my project conventions.
    """
    return find_start_of_packet_marker(puzzle)


def solve_part_2(puzzle: str) -> int:
    """Change the packet_len to 14"""
    return find_start_of_packet_marker(puzzle, packet_len=14)


if __name__ == "__main__":
    # This puzzle is only one line
    with open("d06.input", "r", encoding="utf-8") as f:
        puzzle = f.readline()
    print(f"[Part 1] The first start-of-packet-marker ends at character {solve_part_1(puzzle)}")
    with open("d06.input", "r", encoding="utf-8") as f:
        puzzle = f.readline()
    print(f"[Part 2] The first start-of-message-marker ends at character {solve_part_2(puzzle)}")
