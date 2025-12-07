"""
Breaks a file (or list of strings) separated by a blank line into multiple lists.

Several of the puzzles in AoC have their input as two or more types of objects, separated
by a blank line


type A
type A
type A

type B
type B
"""


def chunk_list(lines: list[str]) -> list[list[str]]:
    """Rearrange lines into new lists"""
    output_list: list[list[str]] = []
    buffer: list[str] = []
    for line in lines:
        if len(line) == 0:
            output_list.append(buffer)
            buffer = []
        else:
            buffer.append(line)
    if len(buffer) > 0:
        output_list.append(buffer)
    return output_list


def chunk_file(filename: str) -> list[list[str]]:
    with open(filename, 'r', encoding='UTF-8') as f:
        return chunk_list(f.read().splitlines())
