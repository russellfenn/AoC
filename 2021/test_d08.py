from d08 import parse_puzzle_input_line, Puzzle
from typing import List, Tuple
from collections import Counter

example_input = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""

example_part_2_answers = ["8394", "9781", "1197", "9361", "4873", "8418", "4548", "1625", "8717", "4315"]


def test_parsing_puzzle_input():
    puzzles: List[Tuple] = list()
    for input_str in example_input.splitlines():
        puzzles.append(parse_puzzle_input_line(input_str))
    # We should have 10 puzzles, each with 2 parts (input_str and output_str)
    # Each input_str should be a list of 10 uniqe signal patterns
    # Each output_str should be a list of 4 digit outputs
    assert len(puzzles) == 10
    assert len(puzzles[0]) == 2
    assert len(puzzles[0][0]) == 10
    assert len(puzzles[0][1]) == 4


def test_part1_counting_easy_outputs():
    puzzles: List[Tuple] = list()
    for input_str in example_input.splitlines():
        puzzles.append(parse_puzzle_input_line(input_str))

    c: Counter = Counter()
    for inputs, outputs in puzzles:
        for o in outputs:
            c[len(o)] += 1

    # len(1)==2, len(4)==4, len(7)==3, len(8)==7
    lengths_list: List[int] = [c[2], c[4], c[3], c[7]]
    assert sum(lengths_list) == 26


part2_example_input = "acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf"


def test_part2():
    puzzle: Puzzle = parse_puzzle_input_line(part2_example_input)
    return puzzle

