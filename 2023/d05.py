"""
Day 05 - Seed Maps

We are given a series of "maps" that map numbers from one group to another.

Once the maps are built out, I think we step through the various maps
to convert an input number into an output.

seed -> soil -> fertilizer -> water -> light -> temperature -> humidity -> location

Each "map" is given as a series of 3 ints:
    dest_range_start source_range_start range_length

Start with a class that basically builds a dict of source->dest values.
Is this an efficient way to do this? Nope. But I hope it works.
Looking at the real input... the numbers are huge (hundreds of millions),
so this may not work well.

As expected the method of creating giant dictionaries failed (at least on my chromebook).
I think I saw the same issue on an earlier puzzle where my solution worked on a 
desktop, but failed on my Raspberry Pi.


"""

from typing import Any


class Range:
    """Simple model of a range"""
    def __init__(self,
                 start_value: int = 0,
                 end_value: int = 0,
                 offset: int = 0
                 ):
        self.start = start_value
        self.end = end_value
        self.offset = offset

    def in_range(self, value: int) -> bool:
        """Values are INclusive"""
        if value >= self.start and value <= self.end:
            return True
        return False


class ElfMap:
    """Model as a list of ranges, where each range is
       start_value, end_value, offset

       These can be simply calculated based on the map input
       Map: 50 98  2 => 98, 100, -48
       Map:  0 15 37 => 15, 52, -15
    """
    def __init__(self):
        self.ranges: list[Range] = []
    
    def add(self,
            dest_start: int,
            source_start: int,
            range_lentgh: int):
        """Add a range of values to the map.
           This is where we convert from the given values
           to the values in range.
        """
        self.ranges.append(Range(source_start,
                                 source_start + range_lentgh,
                                 dest_start - source_start
                                 )
                           )
        
    def get(self, value: int) -> int:
        """Get the mapped value.
           If a value is in one of this maps' ranges,
           return the value plus offset.
           If not in any range, just return the value.
        """
        r: Range
        for r in self.ranges:
            if r.in_range(value):
                return value + r.offset
        return value



class ElfMapAsDict(dict):
    """Model the seed etc. maps as dicts"""

    # def __init__(self):
    #     super().__init__()

    def add(self,
            dest_start: int,
            source_start: int,
            range_lentgh: int):
        """Add a range of values to the map"""
        for i in range(range_lentgh):
            super().__setitem__(source_start + i,
                                dest_start + i)

    def get(self, key: Any) -> Any:
        """Map a source to a destination"""
        return super().get(key, key)


def chunk_puzzle_input(input: list[str]) -> list[list[str]]:
    """Break the puzzle input into chunks
       on blank lines.
    """
    chunk_list: list[list[str]] = []
    chunk: list[str] = []
    for line in input:
        if len(line) == 0:
            chunk_list.append(chunk)
            chunk = []
        else:
            chunk.append(line)
    chunk_list.append(chunk)  # don't forget the last chunk!
    return chunk_list


def parse_puzzle_input(input: list[str]) -> dict:
    """Parse the puzzle input text into a dict
       of map_name: map_data
    """
    puzzle_dict: dict[str, list] = {}
    for chunk in chunk_puzzle_input(input):
        # the first line of a chunk is the map name
        if "map" in chunk[0]:
            map_name, _ = chunk[0].split()
            print(f"Building map: {map_name}")
            em: ElfMap = ElfMap()
            for line in chunk[1:]:
                vals: list[int] = [int(v) for v in line.split()]
                em.add(*vals)
            puzzle_dict[map_name] = em
        if chunk[0].startswith("seeds"):
            label, seeds = chunk[0].split(':')
            puzzle_dict["seeds"] = [int(s) for s in seeds.split()]
    return puzzle_dict


def solve_part_1(puzzle_dict: dict[str, list],
                 seeds: list[int]) -> int:
    """This may be the most deeply nested function I've ever made..."""
    locations: list[int] = []
    for seed in seeds:
        locations.append(
            puzzle_dict["humidity-to-location"].get(
                puzzle_dict["temperature-to-humidity"].get(
                    puzzle_dict["light-to-temperature"].get(
                        puzzle_dict["water-to-light"].get(
                            puzzle_dict["fertilizer-to-water"].get(
                                puzzle_dict["soil-to-fertilizer"].get(
                                    puzzle_dict["seed-to-soil"].get(seed)
                                )
                            )
                        )
                    )
                )
            )
        )
    return min(locations)


if __name__ == "__main__":
    with open('d05.input', 'r', encoding='UTF-8') as f:
        puzzle: list[str] = f.read().splitlines()

    puzzle_dict: dict = parse_puzzle_input(puzzle)
    print(f"[Part 1] The lowest location number is {solve_part_1(puzzle_dict=puzzle_dict)}")
