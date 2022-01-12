from d10 import check_syntax, error_scores, rmatches, score_completion, solve_part2
from typing import List, Tuple


example_puzzle: str = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""


def test_example_puzzle():
    lines: List[str] = example_puzzle.splitlines()
    syntax_errors: List[str] = [check_syntax(line)[0] for line in lines]
    assert syntax_errors == ["", "", "}", "", ")", "]", "", ")", ">", ""]
    score: List[int] = [error_scores[t] for t in syntax_errors]
    assert score == [0, 0, 1197, 0, 3, 57, 0, 3, 25137, 0]
    assert sum(score) == 26397


incomplete_examples: List[Tuple[str, str, int]] = [
    ("[({(<(())[]>[[{[]{<()<>>", "}}]])})]", 288957),
    ("[(()[<>])]({[<{<<[]>>(", ")}>]})", 5566),
    ("(((({<>}<{<{<>}{[]{[]{}", "}}>}>))))", 1480781),
    ("{<[[]]>}<{[{[{[]{()[[[]", "]]}}]}]}>", 995444),
    ("<{([{{}}[<[[[<>{}]]]>[]]", "])}>", 294),    
]


def test_completions():
    for incomplete, correct_completion, _ in incomplete_examples:
        error, stack = check_syntax(incomplete)
        assert error == ""
        # for each remaining element in the stack,
        # find it's match, and reverse the order
        completions: List[str] = [rmatches[t] for t in reversed(stack)]
        assert completions == list(correct_completion)
        # Adding the completion to the given chunk should
        # produce a valid sequence with no leftovers
        complete_sequence = incomplete + "".join(completions)
        error, stack = check_syntax(complete_sequence)
        assert error == ""
        assert len(stack) == 0


def test_score_completions():
    for _, correct_completion, score in incomplete_examples:
        assert score == score_completion(correct_completion)


def test_part2():
    score: int = solve_part2([c[0] for c in incomplete_examples])
    assert score == 288957
