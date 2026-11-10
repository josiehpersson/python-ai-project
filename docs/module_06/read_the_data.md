# Read the data

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