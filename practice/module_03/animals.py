# Inheritance: when something is a kind of something else.

# a cat is an animal, and so is a dog. The classes cat and dog inherit from animal: they get all its attributes and methods, and can change or add their own.

# Animal is the parent class and Cat and Dog are its child classes.
# You also meet the words base class and subclass for the same 2 things.
# When a child class writes its own version of a methid it inherited, it overrides the method.
class Animal:
    def __init__(self, name: str):
        self.name = name
    def speak(self) -> str:
        return "..."

# says that Cat inherits from animal
# Cat has no __init__, but luna still has a name: Cat inherits Animal's __init__
class Cat(Animal):
    # speak is overridden: Cat and Dog each write their own, and theirs is used instead of Animals.
    def speak(self):
        return "Meow"


class Dog(Animal):
    def __init__(self, name: str, tricks: list[str]):
        #super().__init__(name) lets Animal set up its part. Then Dog adds tricks.
        super().__init__(name)
        self.tricks = tricks

    def speak(self):
        return "Woof"


luna = Cat("Luna")
rex = Dog("Rex", ["sit", "shake"])
animals: list[Animal] = [luna, rex]

# the loop calls speak() on each animal in the list, and gets Meow from the cat and Woof from the dog.
# the loop calls animal.speak() without knowing if it has a cat or a dog, and each animal answers in its own way.
# this is called polymorphism, greek for "many forms".
# it lets you write the loop once, and add a new kind of animal later without changing it.
for animal in animals:
    print(animal.name, "says", animal.speak())

print(rex.tricks)
#isinstance is true: a dog is an animal
print(isinstance(rex, Animal))

# Output:
# Luna says Meow
# Rex says Woof
# ['sit', 'shake']
# True
