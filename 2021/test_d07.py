from d07 import cost_constant_fuel, compute_all_costs, cost_generic_fuel
from typing import List

puzzle_input = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]


def test_part1_constant_cost_function():
    all_costs: List[int] = cost_constant_fuel(2, puzzle_input)
    assert all_costs == [14, 1, 0, 2, 2, 0, 5, 1, 0, 12]
    assert sum(all_costs) == 37


def test_part1_constant_cost_to_all_positions():
    all_costs: List[int] = compute_all_costs(puzzle_input, cost_constant_fuel)
    minimum_cost = min(all_costs)
    assert minimum_cost == 37
    assert all_costs.index(minimum_cost) == 1
    assert all_costs[0] == 41
    assert all_costs[9] == 71


def test_part2_generic_fuel_table():
    cost_table: List[int] = list(range(1, max(puzzle_input)))

    all_costs: List[int] = cost_generic_fuel(5, puzzle_input, cost_table)
    assert all_costs == [66, 10, 6, 15, 1, 6, 3, 10, 6, 45]
    assert sum(all_costs) == 168


def test_part2_cost_to_all_positions():
    cost_table: List[int] = list(range(1, max(puzzle_input)))

    def my_cost_func(target: int, positions: List[int]):
        return cost_generic_fuel(target, positions, cost_table)

    all_costs: List[int] = compute_all_costs(puzzle_input, my_cost_func)
    minimum_cost: int = min(all_costs)
    assert minimum_cost == 168
    assert all_costs[1] == 206
