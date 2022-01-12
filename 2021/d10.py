"""
Day 10 - Syntax Scoring

Check the syntax of a mini-language consisting of various types of braces.
All opening braces must be matched by the corresponding closing brace. Out of order
braces indicate a syntax error.

Keep a stack, adding opening tokens, and removing opening tokens as the correct
closing token is found. 
If the closing token does not match the opening one, stop and report
the out-of-sequence token.

Part 2 deals with chunks that are in the correct sequence, but are not complete.
The "completion" sequence is found by reversing the stack, and substituting each
token with its matching closing token.
"""
from typing import Dict, List, Tuple

matches: Dict[str, str] = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

error_scores: Dict[str, int] = {
    '': 0,
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

completion_scores: Dict[str, int] = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}


# make a reverse mapping
rmatches: Dict[str, str] = dict()
for key, value in matches.items():
    rmatches[value] = key


def check_syntax(chunk: str) -> Tuple[str, List[str]]:
    """Return the first invalid token, and the current stack.
       If everything balances, there will be no invalid token, so the first
       element will be an empty string.
    """
    stack: List[str] = list()
    for token in chunk:
        if token in rmatches.keys():  # push to our stack
            stack.append(token)
        else:
            if stack[-1] == matches[token]:  # good close - pop it off the stack
                _ = stack.pop()
            else:
                return token, stack
    return "", stack  # all tokens balanced


def solve_part1(program: List[str]) -> int:
    syntax_errors: List[str] = [check_syntax(line)[0] for line in program]
    score: List[int] = [error_scores[t] for t in syntax_errors]
    return sum(score)


def score_completion(completion: str) -> int:
    score: int = 0
    for token in completion:
        score *= 5
        score += completion_scores[token]
    return score


def solve_part2(program: List[str]) -> int:
    scores: List[int] = list()
    for line in program:
        errors, stack = check_syntax(line)
        if errors == "" and len(stack) > 0:
            completion: str = "".join([rmatches[t] for t in reversed(stack)])
            scores.append(score_completion(completion))
    return sorted(scores)[len(scores)//2]



if __name__ == "__main__":
    with open('d10.input', 'r') as f:
        program = [line.rstrip() for line in f.readlines()]
    print(f"{len(program)} lines of program code")
    print(f"[Part 1] Total syntax error score is {solve_part1(program)}")
    print(f"[Part 2] Autocorrect score is {solve_part2(program)}")
