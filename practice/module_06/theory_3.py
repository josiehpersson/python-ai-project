# New columns, sorting and grouping
# This program makes five sales, adds a column, sorts by it, and works out the median price per district.
# The program comes in three steps: a new column, sorting and grouping.
# Each step adds a few lines to the same program, so run each one and look at the output before the next.

# A new column
import pandas as pd

pd.options.display.float_format = "{:,.0f}".format

sales = pd.DataFrame({
    "district": ["Majorna", "Angered", "Majorna", "Angered", "Centrum"],
    "price": [3_350_000, 1_880_000, 2_190_000, 1_490_000, 5_720_000],
    "living_area": [68, 74, 45, 61, 88],
})

sales["price"] = sales["price"].astype(float)
sales["price_per_sqm"] = sales["price"] / sales["living_area"]
# step 2, sorting
by_price = sales.sort_values("price_per_sqm", ascending=False)
# step 3, grouping
medians = sales.groupby("district")["price"].median()

# step 1: print(f"Sales with price per square meter:\n{sales}")

# step 2, sorted: 
print(f"Sorted by price per square meter:\n{by_price}")
# step 3, grouping
print(f"\nMedian price per district:\n{medians}")

# Output 1
#Sales with price per square meter:
#  district     price  living_area  price_per_sqm
#0  Majorna 3,350,000           68         49,265
#1  Angered 1,880,000           74         25,405
#2  Majorna 2,190,000           45         48,667
#3  Angered 1,490,000           61         24,426
#4  Centrum 5,720,000           88         65,000

# Output 2 (sorting)
# the numbers on the left are the rows old numbers : sorting moves the rows and each row keeps it index.
#Sorted by price per square meter:
#  district     price  living_area  price_per_sqm
#4  Centrum 5,720,000           88         65,000
#0  Majorna 3,350,000           68         49,265
#2  Majorna 2,190,000           45         48,667
#1  Angered 1,880,000           74         25,405
#3  Angered 1,490,000           61         24,426

# Output 3 (grouping)
#Sorted by price per square meter:
#  district     price  living_area  price_per_sqm
#4  Centrum 5,720,000           88         65,000
#0  Majorna 3,350,000           68         49,265
#2  Majorna 2,190,000           45         48,667
#1  Angered 1,880,000           74         25,405
#3  Angered 1,490,000           61         24,426

#Median price per district:
#district
#Angered   1,685,000
#Centrum   5,720,000
#Majorna   2,770,000
#Name: price, dtype: float64