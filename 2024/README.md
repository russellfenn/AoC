# Notes on 2024 Puzzles

## Puzzle Types

01. Mostly manipulating lists. Zip and Counter were handy.
02. More list manipulations, loops.
03. Parse instructions from a (corrupted) string. Regex.
04. Grid.

## Useful Techniques

### Type Aliases

[Type Aliases](https://docs.python.org/3/library/typing.html#type-aliases) allow you to make short, reasonable names for complex types (without making classes).

The general pattern is

```python
type <Alias Name> = <type spec>

type Vector = list[float]
type Grid = list[list[str]]
```

### Dataclasses

A [Dataclass](https://docs.python.org/3/library/dataclasses.html) is a shorthand way to implement a class that incluedes the methods for getters and setters.

```python
In [2]: @dataclass
   ...: class Cell:
   ...:     x: int
   ...:     y: int

In [3]: c = Cell(3, 4)
In [4]: d = Cell(2, 4)
In [5]: e = Cell(3, 4)
In [6]: c == d
Out[6]: False

In [7]: c == e    # We can compare 
Out[7]: True
```
