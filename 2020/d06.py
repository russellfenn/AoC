"""
Day 06 - Customs Questions / More Set Ops

Part 1 - how many questions did _anyone_ in the group answer

Part 2 - how many questions dis _everyone_ in the group answer
"""

from typing import List, Set
from collections import Counter

def parse_input_anyone(data: List[str]) -> List[Set[str]]:
    """Put the letters into a Set to eliminate duplicates."""
    groups: List[Set[str]] = list()
    # Each group is separated by a blank line
    s: Set[str] = set()
    for line in data:
        if len(line) == 0:
            groups.append(s)
            s = set()
        else:
            s.update(list(line))
    if s:  # include any left over
        groups.append(s)
    return groups


#def answered_all(c: Counter, size: int) -> [List[str]]:
#    return [q for q,i in c.items() if i == size]


def count_group_everyone(data: List[str]) -> Set[str]:
    """Similar to the last one, but here we put the letters in a Counter instead of a Set.
       Return a new set of letters where the count is the same as the group size.
    """
    c: Counter = Counter()
    for element in data:
        c.update(list(element))
    return set([q for q,i in c.items() if i == len(data)])
        

def parse_input_everyone(data: List[str]) -> List[Set[str]]:
    all_groups: List[Set[str]] = list()
    group: List[str] = list()
    for line in data:
        if len(line) == 0:
            all_groups.append(count_group_everyone(group))
            # now reset
            group = list()
        else:
            group.append(line)
    if group:
        all_groups.append(count_group_everyone(group))
    return all_groups


if __name__ == "__main__":
    with open('d06.input', 'r') as f:
        data = [l.rstrip() for l in f.readlines()]
    
    anyone_groups: List[Set[str]] = parse_input_anyone(data)
        # lines = [l.rstrip() for l in f.readlines()]
        # groups: List[Set[str]] = parse_input(lines)
    print(f"Parsed input into {len(anyone_groups)} groups.")
    anyone_group_sizes: List[int] = [len(g) for g in anyone_groups]
    print(f"[Anyone] Sum of all group counts => {sum(anyone_group_sizes)}")

    everyone_groups: List[Set[str]] = parse_input_everyone(data)
    everyone_group_sizes: List[int] = [len(g) for g in everyone_groups]
    print(f"[Everyone] Sum of all group counts => {sum(everyone_group_sizes)}")
