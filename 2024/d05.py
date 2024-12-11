"""
Day 05 - Pring Queue

Part 1 seems to be a matter of creating a list of (page) numbers in order, then checking various
other lists to see if they follow the same order.

Page numbers are given as a series of pairs: `47|53` means that page 47 must be before 53.

I think this can be solved with a list of ints, and as we get new numbers, we need to carefully
insert them into the right place on the list.

List insertion rules:

- If the first number IS NOT on the list, extend with both numbers
- If the first number IS on the list, insert the second number after it
- If both on the list

  - If first is before second, do nothing

  
The more I play with this the more it seems like a sorting problem...
But the rules are elven, meaning normal ordering does not work, so maybe we use
the input list as a table of comparisons that drives the sort function.

[Sorting HowTo](https://docs.python.org/3/howto/sorting.html#sortinghowto)
and 
"""


type OrderingRules = dict
type PagesToProduce = list[list[int]]


def parse_puzzle_input(puzzle: list[list[str]]) -> tuple[OrderingRules, PagesToProduce]:
    """Read the puzzle text input
       Ordering rules comes first as int|int
       A blank line separates
       PagesToProduce is a list if list of int
    """
    raw_rules: list[str] = puzzle[0]
    raw_pages: list[str] = puzzle[1]

    # first handle the ordering rules
    ordering_rules: dict = {}
    for line in raw_rules:
        left, right = line.split('|')
        

    # next pages to produce
    pages_to_produce: list[list[int]] = []
    for line in raw_pages:
        pages: list[int] = [int(page) for page in line.split(',')]
        pages_to_produce.append(pages)
    
    return (ordering_rules, pages_to_produce)