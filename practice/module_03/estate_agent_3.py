# a class can hace 2 methods that turn an object into text:
# __str__ is for people, print(kim) and an f-string like f"Call {kim}" use it.
# __repr__ is for developers, when you look for a bug. It shows the object the way you would write it in code. A list shows each object in it with __repr__
# When a class has no __str__, print uses __repr__ instead.
class EstateAgent:
    def __init__(self, name: str, district: str):
        self.name = name
        self.district = district

    def __repr__(self):
        return f"EstateAgent({self.name!r}, {self.district!r})"

    def __str__(self):
        return f"{self.name}, estate agent in {self.district}"


kim = EstateAgent("Kim", "Majorna")
print(kim)
print(f"Call {kim}")
print([kim])

# Output:
#  Kim, estate agent in Majorna
#  Call Kim, estate agent in Majorna
#  [EstateAgent('Kim', 'Majorna')]

# The first 2 lines come from __str__. he list on the last line shows kim with __repr__
# lists always use __repr__
# if the list would use __str__ the output would look like this: [Kim, estate agent in Majorna, Alex, estate agent in Angered] (4 different list posts)