# Notes on 2022 Puzzles

## Puzzle Types

01. Mainly used built-in functions and list slicing.
02.
03. Some set operations. After solving in a straightforward way, I reimplemented
    it using [itertools.islice](https://docs.python.org/3/library/itertools.html#itertools.islice)
04.
05.
06. Pretty simple iterating over a string and slicing.
07. Tree.
08. Grid
09. Grid, Points

## AI Fail

After puzzle day 1 was released, sombody on Twitter claimed they generated the  solution with an AI tool, thich came up with this:

```python
calories = [int(line) for line in example_puzzle.strip().split('\n')]
```

Another person said it would fail trying to convert the blank lines to _int_. That is in fact what happens.

```python
In [1]: example_puzzle
Out[1]: '1000\n2000\n3000\n\n4000\n\n5000\n6000\n\n7000\n8000\n9000\n\n10000\n'

In [2]: calories = [int(line) for line in example_puzzle.strip().split('\n')]
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
Cell In [2], line 1
----> 1 calories = [int(line) for line in example_puzzle.strip().split('\n')]

Cell In [2], line 1, in <listcomp>(.0)
----> 1 calories = [int(line) for line in example_puzzle.strip().split('\n')]

ValueError: invalid literal for int() with base 10: ''
```

## Lessons Learned

### itertools.islice

[islice](https://docs.python.org/3/library/itertools.html#itertools.islice) allows you to select
some number of items from an iterable.

In the [recipes](https://docs.python.org/3/library/itertools.html#itertools-recipes) section,
we find the "batched" function to "Batch data into lists of length n."

This was exactly what I needed on [day 3](d03.py).

### __str__ and __repr__

I still find these confusing... I kind of get that __str__ is for humans (e.g. readable), where __repr__ tries to make a canonical representation that can reconstruct an object.

Today I learned that calling __str__ on a container object will in turn call __repr__ on the objects contained within.

### Classes that reference themselves

On Day 09, I used a Point class. Actually, I started out with a Point namedtuple, but then thought it would be useful to have some methods that manipulated some point, and another related point.
(In the puzzle, Head and Tail were related, and Tail followed the Head according to some silly rules).

```python

class Point:

    ...
    def delta(self, p: Point):  
        pass
```

This fails with a NameError under Python 3.9 -- the p: Point arg is unknown because the Point class is not yet defined.

NameError: name 'Point' is not defined

Real Python has a good article [Python's Self Type](https://realpython.com/python-type-self/) that gives several options.

For Python 3.9 this worked: `from __future__ import annotations`.

In Python 3.11, you can do it this way

```python
from typing import Self
class Point:

    ...
    def delta(self, p: Self):  
        pass

    def clone(self) -> Self:
        pass
```
