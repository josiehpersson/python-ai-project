# Data exploration

## The five files downloaded for this module (in practice/data)
- *apartments.csv* is 443 apartments for sale.
- *apartments.json* is the first 40 of them, as JSON: a text format that stores data as named values, often used by web services.
- *apartments_excel.csv* is the same 443, saved the way Excel does on a Swedish computer.
- *apartments_raw.csv* is the aparments before they were cleaned: 492 rows, with the problems left in. Module 07 cleans it.
- *districts.csv* is six districts: the distance to the center, and whether there is a tram.

## The columns in apartments.csv
- `listing_id` the ID of the listing, one apartment for sale.
- `district` the district.
- `living_area` the living area, in square meters.
- `rooms` the number of rooms. Swedish listings count a small room as a half, so 2.5 is two rooms and a small one.
- `year_built` the year the building was built. Empty when its unknown.
- `elevator` yes, no or unknown.
- `monthly_fee` the rent in kronor. Empty when unknown.
- `price` the price in kronor.

## How the tasks find the data
Say you write this:
`df = pd.read_csv("data/apartments.csv")`
A relative path like *data/apartments.csv* is looked up from the folder you are in when you run the script (in the terminal). It is not looked up from the folder where the script lives. That's why the code sometimes work and sometimes doesn't.

- Run it from *practice/* and Python finds *practice/data/apartments.csv*
- Run it from *practice/module_06* and Python looks for *practice/module_06/data/apartments.csv* (FileNotFoundError)
- Run it from the project root and Python looks for *data/apartments.csv*

### The solution, piece by piece

`DATA = Path(__file__).parent.parent / "data"`

Read it from left to right:
- `Path(__file__)` turns it into a Path object you can work with (e.g .../practice/module_06/task1.py but as an object).
- `__file__` is the pah to the script file being run (e.g .../practice/module_06/task1.py).
- `.parent` is one step up, to the folder the file is in (e.g .../practice/module_06).
- `.parent.parent` two steps up (e.g .../practice).
- `"data"` adds the subfolder data (/ joints paths in pathlib, e.g .../practice/data)

### Folder tree
practice/                 ← .parent.parent
├── data/                 ← .parent.parent / "data"   (= DATA)
│   ├── apartments.csv
│   └── districts.csv
└── module_06/            ← .parent
    └── task1.py          ← __file__

### How to use it

`df = pd.read_csv(DATA / "apartments.csv")`

The path is worked out from the script's own location, so you get the same result wherever you run it from. That's what the text means when it says the script finds the data from "its own place". 

Two things to know:
1. \ isn't division here. When there's a Path object on the left, \ means "join paths". It works on Windows, Mac and Linux, so you don't have to worry about \ vs /.
2. `__file__` doesn't exist in Jupyter notebooks. There you get a *NameError*. The pattern only works in regular .py files that you run with `python file.py`

## A table in Python
Think of a spreadsheet: a row of column names at the top, then one row per aoartment. You can sum a whole column, or sort the sheet, without touching each cell by hand.

The pandas package gives Python the same thing. In module 02 the apartments were a list of dictionaries, and every question needed a loop.

The pandas package reads a file into a DataFrame, a table like that sheet where one line of code works on a whole column at once.

A *DataFrame* is a table: named columns, and numbered rows. One column on its own is a *Series*: the values, with the row numbers beside them. 
The row numbers are the *Index*.

## The method you will use most
- `.head()` the first five rows.
- `.info()` each column's type, and how many values it has.
- `.describe()` count, mean, min, max and quartiles of every number column.
- `df["tram"].value_counts()` how many times each value occurs (swap df for your *DataFrame* and *tram* for any column name).
- `.to_csv(path, index=False)` saves the DataFrame as a CSV file, and `index=False` leaves the row numbers out.

The quartiles are the values a quarter, half and three quarters of the way up when the values are sorted. The middle one is the median.

## Choose your dataset
Choose your dataset, and weite your question in one sentence in README.md. Nothing is fraded in this module, but the rest of the course goes faster when you know what you will use.

### Three places to look for a dataset of your own:
- https://www.kaggle.com/datasets : thousands of datasets on almost anything. Needs a free account.
- https://archive.ics.uci.edu/ : classic machine learning datasets.
- https://www.dataportal.se/ : open data from swedish public authorities.

### Not sure? Start with one of these
Both work for the project, and you can download them for free with an account:
- https://allisonhorst.github.io/palmerpenguins/ : 344 rows. You can predict the spieces of a penguin from its bill, flippers and weight. Has a CCO license (free to use).
- https://archive.ics.uci.edu/dataset/186/wine+quality : 1,599 rows. You can predict the quality score of a wine, from its chemistry. CC BY 4.0 license (name the source)

The *wine quality* file separates its columns with `;` so read it with `sep=";"`, as in *read a file the way it is writen*

### What makes a Dataset work
To predict is to guess a column's value, such as a price, from the other columns. A dataset works when:
- It has a *column you can predict*, a number or a category, and some columns that can explain it.
- It has at least a few hundred rows.
- It has columns *you understand*, so that you can tell wheter a value is reasonable.
- It *may be used*: read the license, and write the source in your `README.md`.
- It holds *no personal data*: no names, personal identity numbers or addresses.
