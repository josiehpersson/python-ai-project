class EstateAgent:
    def __init__(self, name: str, district: str):
        self.name = name
        self.district = district
        self.sales : list[int] = []

    #__repr__ returns the text that print shows for the object, when the class has nothing else for it.
    def __repr__(self):
        #{self.name!r} shows the value the way you would write it in code. Text gets its quotes: 'Kim'.
        return f"EstateAgent({self.name!r}, {self.district!r})"

    def add_sale(self, price: int):
        if price <= 0:
            # raise ValueError(...) stops the program with an error, the same kind Python itself gives.
            # here it stops a sale of 0 kronor, so the object never holds a sale that cannot be true.
            raise ValueError(f"a sale must be more than 0, not {price}")
        self.sales.append(price)


kim = EstateAgent("Kim", "Majorna")
print(kim)
kim.add_sale(0)

# Terminal output
# $ python practice/module_03/estate_agent_2.py
# EstateAgent('Kim', 'Majorna')
# Traceback (most recent call last):
#  File "C:\dev\python-ai-project\practice\module_03\estate_agent_2.py", line 18, in <module>
#    kim.add_sale(0)
#    ~~~~~~~~~~~~^^^
#  File "C:\dev\python-ai-project\practice\module_03\estate_agent_2.py", line 12, in add_sale
#    raise ValueError(f"a sale must be more than 0, not {price}")
#ValueError: a sale must be more than 0, not 0