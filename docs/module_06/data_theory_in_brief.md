# Data theory in brief

## A DataFrame is a table
The *pandas* package reads a file into a DataFrame, a table with a name on each column. Each row has a number, its *index*. A single column, taken out of the table, is a *series*.

A method works on a whole column at once: 
`apartments["price"].mean()` is the mean of every price.

- DataFrame `apartments` : the whole table with rows, and a name on each column.
- Series `apartments["price"]` : one column on its own, with the index beside it.
- Index `0, 1, 2, ...` : the number of each row.

Take one column out of the table and you have a *Series*. The row numbers come along, so each value still know its row.

## Look before you do anything
Four looks tell you what is really in a new file.
- `.shape()` : how many rows and columns.
- `.head()` : the first rows.
- `.info()` : each columns type, and how many values it has.
- `.describe()` : count, mean, min, max and quartiles of the number columns.

Every later step depends on what you find here, so it comes first.

## A missing value is NaN
An empty cell in the file becomes `NaN` in pandas, which meand a missing value. `.info()` shows it: if a column has fewer vales than the table has rows, some are missing.

A column of whole numbers with a missing value becomes `float64`, decimal numbers, because NaN is a decimal number. Finding the missing values is the first part of processing data.

## Two conditions join with &
To keep the rows where two things are both true, name each condition, then join the names:
`print(districts[close & not_center])`

Written on one line, it is `(first condition) & (second condition)`
- Use `&`, not `and`. The word *and needs a single True or False*, but a condition on a column gives one per row, so Python stops with an error.
- Put parentheses around each condition on one line. Without them, Python joins the wrong parts first.

- *close*
True, True, True, True, False, False
- *not_center*
False, True, True, True, True, True
- *close & not_center*
False, True, True, True, False, False
- *close and not_center*
error: and needs one True or False, a column gives one per row

Each condition is a column of Ture and False, one per district. & compares them row by row and keeps a row only where both are True.

## Groups give one number each
`.groupby("district")` puts the rows in a group per district. A median, a mean or a count then gives one number per group. Most questions about data are "per district" or "per year": that is a group.

### sales
Majorna 3,350,000
Angered 1,880,000
Majorna 2,190,000
Angered 1,490,000
Centrum 5,720,000

`.groupby("district")`
*Angered*
1,880,000
1,490,000

*Centrum*
5,720,000

*Majorna*
3,350,000
2,190,000

`["price"].median()`
Angered 1,685,000
Centrum 5,720,000
Majorna 2,770,000
*one number per group*

Split the rows by disctrict, then summarize each group. Five rows in, three numbers out: one per district.

## Read a file the way its written
A CSV file saved by Excel on a Swedish computer separates the columns with ;, and writes decimals with a comma. Read it wit `sep=";"` and `decimal=","`. 

Read it the usual way, and every row lands in one single column, with no error. `.shape` shows it at once: one column instead of eight.

- `ps.read_csv(path)`
district;rooms;price...
one column, with no error
- `sep=";", decimal=","`
district | rooms | price | ...
eight columns, as the file means

The file is the same. Only how you tell pandas to read it changes, and `.shape` shows the difference at once.