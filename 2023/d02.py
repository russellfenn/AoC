"""
Day 02 - Cube Conundrum

Part 1 seems pretty straight-forward.

## Example Input

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green

## Parse input

- One game per line: Game <game_number>: <game_round>; <game_round>

  - <game_round> := <N> <color>, <N> <color>, ...
- Split rounds on semicolons, split numbers and colors on comma.
- Elements are count (int), and color (enum of red, green, blue).
- Compare the counts to the max of each color available.

## Part 2

I think the point of Part 2 is to simply account for the max number of each color in a game.
No mention of whether the game is possible/valid as discussed in Part 1.

For each game, the "Power" is the product of the maximum numbers.
To solve the puzzle, sum the powers of each game.
"""

from dataclasses import dataclass, field


@dataclass
class Round:
    cubes: dict[str, int] = field(default_factory=dict)


@dataclass
class Game:
    id: int = 0
    rounds: list[Round] = field(default_factory=list)


def parse_game_line(game_line: str) -> Game:
    """Parse the string representation of a game
    """
    game: Game = Game()

    game_number, rounds = game_line.split(':')
    _, game_number_str = game_number.split(' ')
    game.id = int(game_number_str)

    round_strings: list[str] = rounds.split(';')
    for game_round in round_strings:
        _round: Round = Round()
        for cubes in game_round.split(','):
            count, color = cubes.strip().split(' ')
            _round.cubes[color] = int(count)
        game.rounds.append(_round)
    return game


PART_1_LIMITS = {
    'red': 12,
    'green': 13,
    'blue': 14,
}


def is_game_valid(game: Game, limits: dict[str, int]) -> bool:
    """A game is valid if all rounds are valid.
       A round is valid if the number of each cube is within the limit.
    """
    for game_round in game.rounds:
        for color, amount in game_round.cubes.items():
            if amount > limits[color]:
                return False
    return True


def solve_part_1(games: list[Game], limits: dict[str, int] = PART_1_LIMITS) -> int:
    valid_games: list[Game] = []
    for game in games:
        if is_game_valid(game, limits):
            valid_games.append(game)
    return sum([g.id for g in valid_games])


def cube_power(game: Game) -> int:
    """Find the maximum number of each color (red, green, blue)
       across all rounds, and return the product.
    """
    reds: list[int] = []
    greens: list[int] = []
    blues: list[int] = []
    for game_round in game.rounds:
        # We use dict.get(key, default) here in case a color does not contain a color
        reds.append(game_round.cubes.get('red', 0))
        greens.append(game_round.cubes.get('green', 0))
        blues.append(game_round.cubes.get('blue', 0))

    return max(reds) * max(greens) * max(blues)


def solve_part_2(games: list[Game]) -> int:
    """Find the sum of the "cube powers"
    """
    return sum([cube_power(game) for game in games])


if __name__ == "__main__":
    with open("d02.input", "r", encoding="UTF-8") as f:
        puzzle_input = [line.rstrip() for line in f.readlines()]
    games: list[Game] = []
    for line in puzzle_input:
        games.append(parse_game_line(line))
    print(f"[Part 1] Sum of valid games: {solve_part_1(games=games, limits=PART_1_LIMITS)}")
    print(f"[Part 2] Sum of cube powers: {solve_part_2(games=games)}")
