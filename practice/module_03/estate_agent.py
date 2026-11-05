# class EstateAgent: starts the class. Class names start with a capital letter.
class EstateAgent:
    #__init__ runs when a new object is made: EstateAgent("Kim", "Majorna")
    # It gives the object its starting values. Every agent starts with an empty list of sales,  self.sales = []
    def __init__(self, name: str, district: str) -> None:
        # self is the object itself. self.name = name saves the name in the object, so the other methods can use it.
        self.name = name
        self.district = district
        self.sales: list[int] = []

    # add_sale and total are methods: functions that belong to the class. You call them on an object: kim.total()
    def add_sale(self, price: int) -> None:
        self.sales.append(price)

    def total(self) -> int:
        # sum(self.sales) adds up the numbers in the list. Kim's to sales make 5626000.
        return sum(self.sales)

# kim and alex are 2 objects of the same class, each with its own name and its own sales.
# what an object knows, like kim.name, is an attribute. What it can do, like kim.total(), is a method. An object is also called an instance of its class.
kim = EstateAgent("Kim", "Majorna")
alex = EstateAgent("Alex", "Angered")

# Python hands the object to self by itself. kim.add.sale(2_453_000) runs add.sale with self as kim and price as 2_453_000
# That is why a method has one more name in its brackets than you write when you call it.
kim.add_sale(2_453_000)
kim.add_sale(3_173_000)
alex.add_sale(1_481_000)

print(kim.name, kim.total())
print(alex.name, alex.total())