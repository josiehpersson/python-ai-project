# districts.csv has six rows, so the whole table fits on the page and you can check every result by eye.
# The tasks then use the 443 apartments.
# This progra, reads ot. and prints its size and the whole table.

from pathlib import Path
import pandas as pd

DATA = Path(__file__).parent.parent / "data"
districts = pd.read_csv(DATA / "districts.csv")

print(f"Rows and columns: \n{districts.shape}")
print(f"\nThe whole table:\n{districts}")

# Output:
#Rows and columns:
#(6, 3)

#The whole table:
#   district  distance_to_center_km tram
#0   Centrum                    0.0  yes
#1     Linné                    1.5  yes
#2   Majorna                    3.0  yes
#3   Örgryte                    3.5  yes
#4  Frölunda                    8.0  yes
#5   Angered                   14.0   no

# The numbers on the left are the index: each row's number, counted from 0.
