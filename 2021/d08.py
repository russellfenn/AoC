"""
Day 08 - Seven Segment Display

This puzzle has a lot going on in the description, but I think the first part mainly comes down
to counting the length of each input or output.

Part 2 is a bit harder

| Digit | Segments Lit | Unique? |                  Original Segments
|=======|==============|=========|
|   0   |  6           | No      |                   aaaa
|   1   |  2           | Yes     |                  b    c
|   2   |  5           | No      |                  b    c
|   3   |  5           | No      |                   dddd
|   4   |  4           | Yes     |                  e    f
|   5   |  5           | No      |                  e    f
|   6   |  6           | No      |                   gggg
|   7   |  3           | Yes     |
|   8   |  8           | Yes     |
|   9   |  6           | No      |

The 8 digit is the only one with a length of 7. It can't tell us anything about how
the jumbled signals map to the digit segments.

The difference between 1 (cf) and 7 (acf) is the top "a" segment. So knowing the len(2) outupt is "1",
we know the len(3) output is "7" AND the extra segment is "a". But we still don't know which are the "c"
or "f" segments. After removing the 1 and 7 from our list of unknowns,
the "c" segment appears in 6/8 output digits, and the "f" segment is in 7/8.

The 4 gives us the "c" and "f" segments (already known), and the "b" and "d" segments.
Again after removing the 4, the "d" is in 6/7 and "b" is in 5/7, so we can use the same technique to get those two.

So at this point, we can identify digits 1,4,7,8 and segments "abcdf".

The 0 is the only unidentified digit that does not contain segment d. The "e" segment will be in
only 3 of the remaining 7 unknowns.


The more I think about this, the more it looks like set operations, so will change the "unknowns" to be a
list of sets instead of list of lists.


Example:

Signal  acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
Length     8      5     5     5    3    6      6     4     6     2
Digit      8                       7                 4           1

"""
from typing import Dict, List, Set, Tuple
from collections import Counter

# Segments lit for each "correct" output digit
segment_map: Dict[str, Set[str]] = {
    "0": set("abcefg"),
    "1": set("cf"),
    "2": set("acdeg"),
    "3": set("acdfg"),
    "4": set("bcdf"),
    "5": set("abdfg"),
    "6": set("abdefg"),
    "7": set("acf"),
    "8": set("abcdefg"),
    "9": set("abcdfg"),
}


# Some type aliases
PuzzleLine = Tuple[List[str]]
Signal = Set[str]
Puzzle = Tuple[List[Signal], List[Signal]]
Segments = Dict[str, str]  # Maps output segments -> original segments
segments: Segments = dict()



def parse_puzzle_input_line(puzzle_str: str) -> Puzzle:
    """Each entry consists of ten unique signal patterns, a | delimiter,
       and finally the four digit output value.
    """
    input_str: str
    output_str: str
    input_str, output_str = puzzle_str.split('|')
    input_signals = [''.join(sorted(i)) for i in input_str.split()]
    output_signals = [''.join(sorted(o)) for o in output_str.split()]
    return [set(i) for i in input_signals], [set(o) for o in output_signals]


def solve_part1(puzzles: List[Tuple[str]]) -> int:
    # The 1, 4, 7, 8 digits all have a unique number of segments lit,
    # so we simply count them
    c: Counter = Counter()
    for inputs, outputs in puzzles:
        for o in outputs:
            c[len(o)] += 1

    # len(1)==2, len(4)==4, len(7)==3, len(8)==7
    lengths_list: List[int] = [c[2], c[4], c[3], c[7]]
    return sum(lengths_list)


def map_wires(signals: List[Signal]) -> Segments:
    unknown_digits: List[Signal] = signals[:]
    known_digits: Dict[str, Signal] = dict()
    lengths: List[int]
    lengths = [len(s) for s in unknown_digits]
    # one has length 2
    one_i = lengths.index(2)
    known_digits['1'] = unknown_digits.pop(one_i)
    lengths = [len(s) for s in unknown_digits]
    # seven has length 3
    seven_i = lengths.index(3)
    known_digits['7'] = unknown_digits.pop(seven_i)
    # eight has length 8
    eight_i = lengths.index(7)
    known_digits['8'] = unknown_digits.pop(eight_i)
    # Now start to identify segments
    known_segments: Segments = dict()
    known_segments['a'] = list(known_digits['7'] - known_digits['1'])[0]
    one_parts: List[str] = list(known_digits['1'])
    for part in one_parts:
        count: int = sum([part in s for s in unknown_digits])
        if count == 6:
            known_segments['f'] = part
        if count == 5:
            known_segments['c'] = part
    lengths = [len(s) for s in unknown_digits]
    # 4 has length 4
    four_i = lengths.index(4)
    known_digits['4'] = unknown_digits.pop(four_i)
    for part in list(known_digits['4'] - known_digits['1']):
        count: int = sum([part in s for s in unknown_digits])
        print(f"{part} {count} {len(unknown_digits)}")
        if count == 5:
            known_segments['d'] = part
        if count == 4:
            known_segments['b'] = part
    
    print(f"{unknown_digits=}")
    return known_segments

  



if __name__ == "__main__":
    puzzle_inputs: List[Tuple[str]] = list()
    with open('d08.input', 'r') as f:
        for line in f.readlines():
            puzzle_inputs.append(parse_puzzle_input_line(line))

    print(f"[Part 1] Easy digits 1, 4, 7, 8 appear {solve_part1(puzzle_inputs)} times.")
