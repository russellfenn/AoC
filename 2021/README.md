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