# Notes on 2022 Puzzles

## Puzzle Types

01. Mainly used built-in functions and list slicing.
02.
03. Some set operations. After solving in a straightforward way, I reimplemented
    it using [itertools.islice](https://docs.python.org/3/library/itertools.html#itertools.islice)


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