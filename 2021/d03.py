"""
Day 03 - Binary

It should be simpler to treat the binary numbers as strings, then convert to int later.

"""

from collections import Counter
from typing import List, Tuple
from copy import deepcopy

def bit_counter(byte_str: List[str]) -> List[Counter]:
    """Count values in each byte_string with a counter.
       The list of counters will be as wide as the byte string
       itself, i.o.w. a 5-bit byte will produce a list of 5 Counters.
    """
    c_list: List[Counter] = list()
    for i in range(len(byte_str[0])):  # assume all bytes are the same length
        c_list.append(Counter())
    for bs in byte_str:
        for bit in range(len(bs)):
            c_list[bit].update(bs[bit])
    return c_list


def calc_gamma_rate(c_list: List[Counter]) -> int:
    """Gamma rate uses the most common bit values.
       Use Counter.most_common() to get the binary bits,
       then convert to decimal.

       most_common() returns a List of Tuples, where each
       tuple is (bit_value, count). The list is in descending order.
    """
    # grab the most common bit value from each counter. Count is not important here.
    gamma_bits: List[str] = [c.most_common()[0][0] for c in c_list]
    gamma_byte: str = ''.join(gamma_bits)
    return int(gamma_byte, base=2)


def calc_epsilon_rate(c_list: List[Counter]) -> int:
    """Epsilon rate is calculated similar to Gamma,
       but uses the least common value - i.o.w. the last
       tuple in the Counter.most_common() list.
    """
    epsilon_bits: List[str] = [c.most_common()[-1][0] for c in c_list]
    epsilon_byte: str = ''.join(epsilon_bits)
    return int(epsilon_byte, base=2)


def solve_part1(data: List[str]) -> int:
    bit_counts: List[Counter] = bit_counter(data)
    gamma: int = calc_gamma_rate(bit_counts)
    epsilon: int = calc_epsilon_rate(bit_counts)
    return gamma * epsilon


def bit_filter(data: List[str], offset: int, target: str) -> List[str]:
    """Return strings where the bit (a string) at offset matches target"""
    return [b for b in data if b[offset] == target]

MostCommon = List[Tuple[str, int]]

def oxygen_generator_rating(data: List[str]) -> int:
    d: List[str] = deepcopy(data)
    target_bit_value: str
    for bit in range(len(d)):
        # Find the most common bit value
        mc: MostCommon = bit_counter(d)[bit].most_common()
        if mc[0][1] == mc[1][1]:  # tie goes to '1'
            target_bit_value = '1'
        else:
            target_bit_value = mc[0][0]
        # Then filter by that value
        d = bit_filter(d, bit, target_bit_value)
        if len(d) == 1:
            break
    return int(d[0], base=2)


def co2_scrubber_rating(data: List[str]) -> int:
    d: List[str] = deepcopy(data)
    target_bit_value: str
    for bit in range(len(d)):
        # Find the least common bit value
        mc: MostCommon = bit_counter(d)[bit].most_common()
        if mc[0][1] == mc[1][1]:  # tie goes to '0'
            target_bit_value = '0'
        else:
            target_bit_value = mc[-1][0]
        # Then filter by that value
        d = bit_filter(d, bit, target_bit_value)
        if len(d) == 1:
            break
    return int(d[0], base=2)


def solve_part2(data: List[str]) -> int:
    oxygen: int = oxygen_generator_rating(data)
    co2: int = co2_scrubber_rating(data)
    return oxygen * co2


if __name__ == "__main__":
    with open('d03.input', 'r') as f:
        puzzle_input: List[str] = [l.rstrip() for l in f.readlines()]

    print(f"[Part 1] Power consumption: {solve_part1(puzzle_input)}")
    print(f"[Part 2] Life support rating: {solve_part2(puzzle_input)}")
