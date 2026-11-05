# gets dataclass from the standard lib
from dataclasses import dataclass

# @dataclass turns it into a dataclass.
#  A line that starts with @ is called a decorator: it changes the class or function right under it.
@dataclass
class EstateAgent:
    name: str
    phone: str
    sales: int = 0

kim = EstateAgent("Kim", "031-390 06 00")
same = EstateAgent("Kim", "031-390 06 00")

print(kim)
# A dataclass compares the values. A normal class only says True if its the very same object.
print(kim == same)

# Output:
# EstateAgent(name='Kim', phone='031-390 06 00', sales=0)
# True