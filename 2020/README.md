# Notes on 2020 Puzzles

## Lessons Learned

I worked to use Python Type Hints throughout the various puzzles. I think in general, it makes it easier to reason with the functions and return types (especially as the types get more complex).

### Type Alias

Adding a [Type alias](https://docs.python.org/3/library/typing.html#type-aliases) to [day 7](day07.py) gave a reasonable name to a fairly complex type that was used throughout the program. 

The alias also helped to reduce confusion -> in refactoring, I realized the types were not quite what I thought they were. Using [mypy](https://github.com/python/mypy) (essentially a type hint linter) helped to keep things consistent as well.

### str.splitlines

[splitlines](https://docs.python.org/3/library/stdtypes.html#str.splitlines) will split a string on any of a whole set of line-end markers. The best part is that it does not return the line-ends (unless you want them).

`data.split('\n')` => `data.splitlines()`

### int(str, base)

[int](https://docs.python.org/3/library/functions.html#int) can take a string and a base, which is great for converting
binary or hex values to their int equivalents.

```python
In [7]: int("0000000010", base=2)
Out[7]: 2

In [11]: int("0xABCD", base=16)
Out[11]: 43981
```

See [Day 05 Tests](test_d05.py) for this technique in action.
