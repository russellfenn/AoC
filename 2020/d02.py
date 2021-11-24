"""
Day 02
Validate password rules to password database.

| Rule  | Password  | Valid? |
|=======|===========|========|
| 1-3 a | abcde     | Yes    |
| 1-3 b | cdefg     | No     |
| 2-9 c | ccccccccc | Yes    |

Rule: <min>-<max> <char>
The given character must appear in the password at least <min>
times, and at most <max> times.

I think a Python [Counter](https://docs.python.org/3/library/collections.html#collections.Counter) 
may be useful.
"""

from collections import Counter
from typing import List, Tuple
import re

def validate_password(minimum: int,
                      maximum: int,
                      target_char: str,
                      password: str,
                      ) -> bool:
    c = Counter()
    c.update(password)
    if target_char not in c:
        return False  # Assume zero is invalid?
    if c[target_char] >= minimum and c[target_char] <= maximum:
        return True
    return False


password_rx = re.compile(r'^([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)')
def parse_password_entry(entry: str) -> Tuple:
    res = password_rx.match(entry)
    if res:
        g = res.groups()
        return (int(g[0]), int(g[1]), g[2], g[3])
    raise ValueError("Invalid password entry")


def validate_position_rule(position_1: int,
                           position_2: int,
                           target_char: str,
                           password: str,
                           ) -> bool:
    """In this method, the positions must be checked for the target_char.
       Exactly one of the given positions must contain that char.
    """
    if target_char not in password:
        return False  # Assume zero is invalid?
    # we need to subtract 1 from each position (not zero indexed)
    result = (password[position_1 - 1] == target_char,
              password[position_2 - 1] == target_char,
              )
    return sum(result) == 1  # True if 1 match


if __name__ == "__main__":

    # Read the input to make a list of rules
    with open('d02.input', 'r') as f:
        rules: List[Tuple] = [parse_password_entry(e) for e in f.readlines()]
    
    # Make a list of [True, True, False] etc where each value
    # is True if the password matches the rule
    count_valids = [validate_password(*r) for r in rules]
    # Python quirk, but [True, False] is equivalent to [1, 0], so we can sum it
    print(f"Using 'Count' rule: There were {sum(count_valids)} valid rules.")
    position_valids = [validate_position_rule(*r) for r in rules]
    print(f"Using 'Position' rule: There were {sum(position_valids)} valid rules.")
    