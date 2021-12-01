# Notes on 2020 Puzzles

## Lessons Learned

I worked to use Python Type Hints throughout the various puzzles. I think in general, it makes it easier to reason with the functions and return types (especially as the types get more complex).

Adding a [Type alias](https://docs.python.org/3/library/typing.html#type-aliases) to [day 7](day07.py) gave a reasonable name to a fairly complex type that was used throughout the program. 

The alias also helped to reduce confusion -> in refactoring, I realized the types were not quite what I thought they were. Using [mypy](https://github.com/python/mypy) (essentially a type hint linter) helped to keep things consistent as well.
