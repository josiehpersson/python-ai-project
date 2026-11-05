apartments = [
    {"district": "Majorna", "living_area": 68, "price": 3_350_000},
    {"district": "Angered", "living_area": 74, "price": 1_880_000},
    {"district": "Majorna", "living_area": 45, "price": 2_190_000},
    {"district": "Centrum", "living_area": 52, "price": 3_410_000},
    {"district": "Angered", "living_area": 61, "price": 1_490_000},
    {"district": "Centrum", "living_area": 88, "price": 5_720_000},
]

for apartment in apartments:
    print(apartment["district"], apartment["price"])