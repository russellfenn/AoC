# Notes on 2021 Puzzles

So far, these puzzles are pretty similar to the 2020 puzzles.

## Lessons Learned

### Classes

For [Day 4](d04.py), I was reluctant to make a BingoCard class. I tried to just use List manipulations, but
these turned out to be more complex and error prone than I expected. This puzzle got complex enough that a
class encapsulating the behavior was simpler once I got over my bias.

### list.index()

I forgot that list.index() returns 0 if the target item is first on the list (at position 0, duh), and raises a
ValueError if the target is not found. I created a bug by mixing my programming metaphores, interpreting a 0 value as not found, which took quite a while to figure out.

### Limits of Python Lists

Python lists are incredibly useful, but they have their limits!
When the list of Lanternfish objects in [Day 6](d06.py) grew very large, it consumed so much memory that my machine locked
up and had to be rebooted. Even switching to a list of ints only went so far (around 3 million).

The puzzle example had billions of fish, and the part 2 had trillions. Keeping track of that many items simply does not work
for small machines. Instead, keeping count of a small number of similar items was much simpler and memory efficient.

The Lanternfish problem changed from tracking 1.6 trillion individual fish (impossible) to 9 groups totaling 1.6 trillion (easy).

### Slicing Gotcha

We have all seen what happens when we try to select an element beyond the end of a list
(l[i] where i > len(l))

```python
In [1]: l = list(range(5))

In [2]: l
Out[2]: [0, 1, 2, 3, 4]

In [3]: len(l)
Out[3]: 5

In [4]: l[7]
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-4-dc61b3a869da> in <module>
----> 1 l[7]

IndexError: list index out of range
```

We get the familiar [IndexError](https://docs.python.org/3/library/exceptions.html#IndexError). What I did not realize until now (as documented above!) is that

> Slice indices are silently truncated to fall in the allowed range

N.B. This applies to Tuples and Strings as well!

```python
In [5]: l[:7]
Out[5]: [0, 1, 2, 3, 4]
```

This makes it easy to unwittingly get the wrong value!

```python
In [6]: sum(l[:3])
Out[6]: 3

In [7]: sum(l[:4])
Out[7]: 6

In [8]: sum(l[:5])
Out[8]: 10

In [9]: sum(l[:7])
Out[9]: 10

In [10]: sum(l[:75])
Out[10]: 10
```

In the Crab submarine puzzle [Day 7](d07.py), I incorrectly made the list too short, but that was hidden by "silently truncated" slices, leading me to the wrong answer.

## functools.reduce

[functools.reduce](https://docs.python.org/3/library/functools.html#functools.reduce) applies a given function cumulatively
to the items of the iterable.

A couple times in these puzzles, I have needed a **product**(_iterable_) function similar to the built-in [sum](https://docs.python.org/3/library/functions.html#sum) function. I wrote a function in [2020 Day 1](2020/d01.py), but that can be simplified with

```python
from functools import reduce
from operator import mul
top_three_basins: List[int] = [9, 9, 14]
product: int = reduce(mul, top_three_basins)
```