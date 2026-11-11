# Summary
The most important points from Module 06
- The *pandas package* reads a file into a *DataFrame*: a table with named columns. One column is a Series. It does in one line what Module 02 did with `csv` and a loop, and it knows the numbers are numbers.
- *Look first*: `.shape()`, `.head()`, .`.info()` and `.describe()` tell you the size, the types and the missing values before you do anything else, because every later step depends on what is really in the file.
- *Select* with brackets, *filter* with a condition: `apartments["price"]` selects a column. Name the condition, `cheap = apartments["price"] < 2_000_000`, then filter with `apartments[cheap]`. Join two named conditions with `&`, because the word `and` cannot compare whole columns. Written on one line, each condition needs its own parentheses.
- A new column is calculated for *every row a once*, with no loop, so it is short to write and fast to run.
- `.groupby()` summarizes per group. Most questions about data are "per district" or "per year": thats a group.
- Read the file *the way it is written*: `sep=";"` and `decimal=","` for a CSV file from Excel. Read it wrong, and every value lands in one column without an error.