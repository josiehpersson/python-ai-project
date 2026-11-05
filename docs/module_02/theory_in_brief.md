# Theory in brief
## Every value has a type
- `int` is a whole number: 2_453_000.
- `float` is a number with decimals: 2.5.
- `str` is text: "Majorna".
- `bool` is true or false.
- `None` means no value at all.

The types decides what you can do with a value: you can add two numbers, but not a number and text. Text from a file or from `input()` is a str, even when it looks like a number, so convert it with `int()` or `float` first. 

## Indentation shows the block
Where C# annd Java uses curly braces, Python uses a colon and indentation. The lines under a `for`, an `if` or a `def`, four spaces in, belong to it. The first line that is not indented ends the block.
So indentation in Python is not only style. Move a line in or out, and the program does something else.

## A list can change, a touple cannot
Both keep values in an order, and both count from 0. A list, `[2_453_000, 1_933_00]`, can grow, shrink and change. A tuple, `(57.70, 11.97)` stays exactly as it was made.

- Use a tuple for a few values that belong together and must stay the same, like a position on a map. 
- Use a list for many values of the same kind.

## Dictionaries look up, sets keep things once
A dictionary pairs each **key** with a value. `apartment["price"]` gets the price. To Python, "price" and "Price" are two different keys, and a key that is not there stops the program with a `KeyError`. `get()` gives `None` instead.

A set keeps each value only once, in no order. Both are written with `{}`. A dictionary holds `key: value` pairs, a set holds only values.

## The standard library comes with Python
Modules like csv, json, pathlib, statistics and collections come with Python itself: the standard library. An `import` line is all they need, with no install step.

Other libraries, like pandas, are not part of it. You install them with `pip` into your virtual environment, and then `import` them the same way.