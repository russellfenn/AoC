"""
Day 07 - Crab Submarines and Whales

This seems like an optimization problem.
With a small input, it's probably practical to test all options, but
we'll see if that continues (I doubt it).

Solving all possible positions, then finding the minimum is slow, but still practical,
even with the Part 2 problem (which in my method involves summing large sets of numbers, rather than a
straight calculation).
A couple ideas for optimization are:

- "memoize" the sums, rather then calculating them each time
- pre-compute the table so the movement calculation is a simple lookup
- derive a formula for cost

"""

from typing import Callable, List, Tuple


def cost_constant_fuel(target: int, positions: List[int]) -> List[int]:
    """Compute the cost of moving each crab in [positions]
       to the target point.
    """
    return [abs(target - i) for i in positions]


def cost_generic_fuel(target: int, positions: List[int], cost_table: List[int]) -> List[int]:
    """Introduce a cost table - cost to move N positions is the value
       at position N in the table.
    """
    return [sum(cost_table[0:abs(target-i)]) for i in positions]


def compute_all_costs(crabs: List[int], cost_func: Callable) -> List[int]:
    """Compute the cost for each position.
    """
    return [sum(cost_func(c, crabs)) for c in range(1, len(crabs)+1)]


def solve_part1(crabs: List[int]) -> Tuple[int, int]:
    all_costs: List[int] = compute_all_costs(crabs, cost_constant_fuel)
    min_cost: int = min(all_costs)
    min_pos: int = all_costs.index(min_cost) + 1
    return (min_cost, min_pos)


def solve_part2(crabs: List[int], cost_function: Callable) -> Tuple[int, int]:
    all_costs: List[int] = compute_all_costs(crabs, cost_function)
    min_cost: int = min(all_costs)
    min_pos: int = all_costs.index(min_cost) + 1
    return (min_cost, min_pos)


if __name__ == "__main__":
    with open('d07.input', 'r') as f:
        puzzle_input: List[int] = [int(i) for i in f.readline().split(',')]

    part_1_solution: Tuple[int, int] = solve_part1(puzzle_input)
    print(f"[Part1] Minimum cost is {part_1_solution[0]} at position {part_1_solution[1]}.")

    cost_table: List[int] = list(range(1, max(puzzle_input)))

    def my_cost_func(target: int, positions: List[int]):
        return cost_generic_fuel(target, positions, cost_table)

    part_2_solution: Tuple[int, int] = solve_part2(puzzle_input, my_cost_func)
    print(f"[Part 2] Minimum cost (using crab engines) is {part_2_solution[0]} at position {part_2_solution[1]}.")

    better_cost_table: List[int] = list()
    better_cost_table.append(1)
    for i in range(2, max(puzzle_input)):
        better_cost_table.append(i + better_cost_table[-1])
