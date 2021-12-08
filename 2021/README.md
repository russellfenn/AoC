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
