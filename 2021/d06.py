"""
Day 06 - Exponential Lanternfish. An exercise in really big numbers.

Will try a Lanterfish class... which works fine for a small school of fish, or over a short simulation period.

But when the numbers get big, the overhead of classes becomes huge.

For part 2, let's make this lighter weight by simply using a list of ints.

Well, this works a lot better, and a test on the sample data for 80 days gets the same result with each method.

But our full 256 day simulation, even for the initial sample of 5 fish grows to 26 billion. I tested with a list that grew
to 35 _million_, and while it worked, it took a while. There must be a better way.

So instead of tracking each individual fish, instead we will keep a Counter of how many fish are at timer 5, 3, 0, etc.
Iterating per day would simply mean taking the number of '5's and making them 4. The zeros become 6, and we add that number of 8s.
Our counter will have at most 9 items to track.
"""

from typing import Any, List, Optional
from collections import Counter

class Lanternfish:

    def __init__(self, timer: int = 8):
        self.timer = timer
    
    def age(self) -> Optional[Any]:
        if self.timer == 0:  # Spawn a new Lanternfish
            self.timer = 6
            return Lanternfish()
        # Otherwise just decrement our timer
        self.timer -= 1

    def __repr__(self):
        return f"Lanternfish(timer={self.timer})"


def iterate(lf: List[Lanternfish]):
    """Iterate a day in our simulation. Mutates the List of Lanterfish.

       Note: we do not want to use enumerate() (a generator) to sequence through our list
       of Lanternfish, because new fish are added to the end of the list, and the generator
       returns those new fish as well. The game expects new fish to have timer=8.
    """
    for i in range(len(lf)):
        new_fish: Optional[Lanternfish] = lf[i].age()
        if new_fish:
            lf.append(new_fish)


def lightweight_iterate(lf: List[int]):
    for i in range(len(lf)):
        if lf[i] == 0:
            lf[i] = 6
            lf.append(8)
        else:
            lf[i] -= 1


def iterate_counter(c: Counter) -> Counter:
    new_counter: Counter = Counter()
    for timer, count in c.items():
        if timer == 0:
            new_counter[6] += count
            new_counter[8] += count
        else:
            new_counter[timer-1] += count
    return new_counter


def read_puzzle_input(initial_ages: List[int]) -> List[Lanternfish]:
    lf: List[Lanternfish] = list()
    for age in initial_ages:
        lf.append(Lanternfish(timer=age))
    return lf


def solve_part1(lf: List[Lanternfish], days: int) -> int:
    for i in range(days):
        iterate(lf)
    return len(lf)


def solve_part2(lf: Counter, days: int) -> int:
    for i in range(days):
        lf = iterate_counter(lf)
    return sum(lf.values())


if __name__ == "__main__":
    with open('d06.input', 'r') as f:
        puzzle_input = [int(i) for i in f.read().split(',')]
    
    lanternfish: List[Lanternfish] = read_puzzle_input(puzzle_input)
    print(f"[Part 1] After 80 days, there are {solve_part1(lanternfish, 80)} lanternfish.")

    lanternfish_counter: Counter = Counter(puzzle_input)
    print(f"[Part 2] After 256 days, there are {solve_part2(lanternfish_counter, 256)} lanternfish!")
