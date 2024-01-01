"""Test Day 02"""
from d02 import (
    Game,
    parse_game_line,
    is_game_valid,
    PART_1_LIMITS,
    cube_power,
    solve_part_2,
)

from pytest import fixture

PART_1_EXAMPLE_PUZZLE = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""


@fixture
def part_1_example() -> list[str]:
    """Simple fixture"""
    return PART_1_EXAMPLE_PUZZLE.splitlines()


def test_parse_game_line(part_1_example):
    """Just test the parser"""
    games: list[Game] = []
    for line in part_1_example:
        games.append(parse_game_line(line))
    assert len(games) == 5

    game1: Game = games[0]
    assert game1.id == 1
    assert len(game1.rounds) == 3
    assert game1.rounds[0].cubes == {'blue': 3, 'red': 4}


def test_part_1_examples_for_valid_games(part_1_example):
    """In this example, games 1, 2, and 5 are valid"""
    games: list[Game] = []
    for line in part_1_example:
        games.append(parse_game_line(line))
    valid_games: list[Game] = []
    for game in games:
        if is_game_valid(game, PART_1_LIMITS):
            valid_games.append(game)
    game_sum: int = sum([g.id for g in valid_games])
    assert game_sum == 8


def test_cube_powers(part_1_example):
    games: list[Game] = []
    for line in part_1_example:
        games.append(parse_game_line(line))

    assert cube_power(games[0]) == 48
    assert cube_power(games[1]) == 12
    assert cube_power(games[2]) == 1560
    assert cube_power(games[3]) == 630
    assert cube_power(games[4]) == 36


def test_part_2_example(part_1_example):
    games: list[Game] = []
    for line in part_1_example:
        games.append(parse_game_line(line))
    assert solve_part_2(games) == 2286
