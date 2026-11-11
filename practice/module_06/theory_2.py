# This program prints the mean distance to the center, and then only the districts closer than 5 km.
# The mean is the average: all the values added, divided by how many there are.

from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent.parent / "data"
districts = pd.read_csv(DATA / "districts.csv")

mean = districts["distance_to_center_km"].mean()
close = districts["distance_to_center_km"] < 5

print(f"Mean distance:\n{mean}")
print(f"\nDistricts closer than 5 km:\n{districts[close]}")

# Output:
#Mean distance:
#5.0

#Districts closer than 5 km:
#  district  distance_to_center_km tram
#0  Centrum                    0.0  yes
#1    Linné                    1.5  yes
#2  Majorna                    3.0  yes
#3  Örgryte                    3.5  yes
