# Python essentials
## The basics
- a variable: price = 2_453_000
- no value/null: None
- a block ({ ... }): A colong, then the lines under it four spaces in.
- else if: elif

## Loops, methods and text with values
- each item in a list (foreach): for apartment in apartments:
- a method: def price_per_sqm(apartment):
- text with values (`text ${variable} text`): f"text {variable} text"  
```python
f"{district}: {price:,} SEK"
```
{price:,} adds a comma between thousands. What comes after the : says how to show the value.
```python
f"Price per square meter: {price / living_area:,.0f} SEK" 
```
{price / living_area:,.0f} works out the price per square meter first. / divides. ,.0f adds the commas, and shows no decimals.
- check if somethin is true: assert price_per_sqm(example) == 50_000

## Keeping many values together, and the code that comes with Python
- array: `[1,2]`
- record (values that must not change): `(57.70, 11.97)`, a tuple
- object (dictionary): `{"district": "Majorna", "price": 2_435_000}`
- filter a list: `[apartment for apartment in apartments if apartment["price"] < 2_000_000]`
- each value only once: `{"Majorna", "Centrum"}`, a set.

## Import the standard library
import csv

## Lists, tuples, dictionaries and sets
Python has four ways to keep many values together.
- list: `[2453000, 1933000]` - Use it when you have many values of the same kind, in an order. You can change the order.
- tuple: `(57.70, 11.97)` - Use it when you have a few values that belong together and must not change, like a position on a map.
- dictionary/dict: `{"district": "Majorna", "price": 2453000}` - Use it when you need to look values up by a key.
- set: `{"Majorna", "Centrum"}` - use it when you need each value once, in no order.

### This example uses all four:
```python
prices = [2_453_000, 1_933_000, 5_053_000]
location = (57.70, 11.97)
apartment = {"district": "Majorna", "living_area": 50, "price": 2_453_000}
districts = {"Majorna", "Centrum", "Majorna"}

print(prices[0])
print(location[1])
print(apartment["price"])
print(apartment.get("balcony"))
print(apartment.get("balcony", "unknown"))
print(sorted(districts))
```
```terminaloutput
2453000
11.97
2453000
None
unknown
['Centrum', 'Majorna']
```

- `prices[0]` is the first value.
- `location[1]` is the second value in the tuple.
- `apartment["price"]` gets the value for the key "price". If the key does not exist, the program stops with with a KeyError.
- `apartment.get("balcony")` gives None instead of stopping, when the key does not exist. `.get("balcony", "unknown") gives you your own value instead.
- `districts` has "Majorna" only once: a set keeps each value once. A set has no order, so the example prints it with sorted().

## Loops and choices
`for` runs the same lines once for each value in a list.
`if` runs lines only when something is true.
This program prints the apartments under 1,000,000 kronor, then a list of every price:
```python
from apartments import apartments

for apartment in apartments:
    if apartment["price"] < 1_000_000:
        print(apartment["listing_id"], apartment["district"], apartment["price"])

prices = [apartment["price"] for apartment in apartments]
print(prices)
```
```terminaloutput
A05 Angered 596000
A07 Frölunda 865000
[2453000, 1933000, 5053000, 2321000, 596000, 1481000, 865000, 2129000]
```
- `from apartments import apartments` gets the list of apartments from apartments.py. The first apartments, after the from, is the file, without.py: Python finds it because it is in the same folder as the program. The second, after import, is the list called apartments in that file.
- the four spaces before a line show that it belongs to the for of the if above it. 
- `[apartment["price"] for apartment in apartments]` is a list comprehension: a new list, built in one line. Read it as "the price, for each apartment in apartments".

The list comprehension does the same as this loop. It makes an empty list, and adds one price for each apartment

## Values and types
Every value in Python has a type. These five are the ones you need most:
- type(...) gives a value's type. Python prints a tye ac <class '...'>, with the type's name in the quotes.
- int is a whole number, and float is a decimal number. Python writes a decimal point, not a comma. the _ in 2_435_000 only makes the number easier to read.
- str is text in quotes.
- bool is true or false.
- None means "no value", for example a year that is not known. It's type is called NoneType.

## Functions
A function is like a recipe card. You write it once, give it a name and use it whenever you need it: you hand it the ingredients, and it hands back the result. In Python, a function gives a name to a piece of code. `def` starts it, the names in parentheses are what you hand it, and return gives back the answer:
```python
def price_per_sqm(apartment):
    return apartment["price"] / apartment["living_area"]

example = {"price": 2_500_000, "living_area": 50}
assert price_per_sqm(example) == 50_000
print(price_per_sqm(example))
```
The output:
5000.0

- `def price_per_sqm(apartment):` starts the function. price_per_sqm is its name. Inside the function, the value you hand it is called apartment.
- `return` gives back the answer, and ends the function.
- `price_per_sqm(example)` runs the function with example as apartment.
- 5000.0 has a decimal, because / always gives a float, even when he numbers divide evenly.
- `assert` checks that something is true, and stops the program if it's not. Check a function with an example you can work out youself: 2,500,000 kronor for 50 square meters is 50,000 per square meter.

Had the check been wrong, for example == 40_000, the program would stop at the assert before the print:
```terminalOutput
Traceback (most recent call last):
  File "/Users/you/python-ai-project/practice/module_02/try.py", line 6, in <module>
    assert price_per_sqm(example) == 40_000
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError
```

Read it from the botom up:
- AssertionError, the last line, is what went wrong: a check with assert was not true.
- The line with ^ marks the part of the line that failed.
- The line above it is the line of your code that stopped the program.
- File "...", line 6 says which file and which line it is.
- Traceback (most recent call last) only says that a traceback begins.

## The standard library
The standard library is the modules that come with Python. A module here is a file of Python code that you import, not a module of this course. You import them, and install nothing.

### statistics
What it does: Mean, median and more: median([1,5,3])
### csv
What it does: Reads and writes CSV files, a table as text, one row per line, with a comma between values.
#### json
What it does: Reads and writes JSON, text that looks like a list an dictionary, which many programs use to send data.
### pathlib
What it does: Paths to files and folders `Path("practice") / "data" / "apartments_small.csv"`
### collections
What it does: Extra collections, like Counter, which counts how often each value occurs.

There are 2 ways to import from a module:
- `import csv` gets the whole module. You then write the module's name before what you use from it: csv.DictReader.
- `from statistics import median` gets one name from the module. You then write the name alone: median(prices).

Libraries like pandas, which works with tables and which the course uses from module 6 are not in the standard library. You install them with `pip`. Pythons tool for installing packages.

## Read a file
A file is opened with `open()`, inside `with`. This program reads the CSV file that the exercises use, and prints its first row:
```python
import csv
from pathlib import Path

path = Path("practice") / "data" / "apartments_small.csv"
with open(path, encoding="utf-8", newline="") as file:
    rows = list(csv.DictReader(file))

print(rows[0]["district"], rows[0]["price"])
```
The output:
```terminalOutput
Majorna 2453000
```

- `Path("practice") / "data" / "apartment_small.csv"` is the path to the file: the folder practice, the folder data in it, and the file. Between paths, / does not divide: it joins folders and file name, on every system. The path starts from the folder you run your program in.
- `with open(...) as file:` opens the file, and closes it again after the indented lines.
- `encoding="utf-8"` reads å, ä and ö right.
- `newline=""` lets `csv` handle the ends of the lines itself, as Python's documentation asks.
- `csv.DictReader(file)` gives each row as a dictionary, with the column names as keys.
- `list(...)` around it gives you all the rows in a list.

`csv` gives every value as text. A CSV file is only text, so "2453000" is a str, not an int.
Convert it with `int()` or `float()` before you calculate with it or compare with a number.

## Read an error
These are the errors you'll meet most and what they usually mean:
### NameError
A name that does not exist, often a typo. Python often suggests the right name.
### KeyError
A key that does not exist in a dictionary.
### IndexError
A position that does not exist in a list
### TypeError
The wrong type, like text where a number should be.
### ValueError
The right type but a value that cannot work, like `int("2,5")`
### FileNotFoundError
The file does not exist, or the program looks in the wrong folder.