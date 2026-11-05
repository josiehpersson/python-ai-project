# OOP fundamentals

## Class or function?

### Use a class when:
- Data and the code that works on it belong together
- There are rules the data must always follow

### Use a function when:
- A value goes in and a value comes out
- Nothing needs to be remembered between calls

## One class, many objects
A class describes what every object of one kind has and can do. 
Each object made from it has it's own values.

EstateAgent is one class. kim and alex are 2 objects made from it, each with its own name and its own sales. One class Home can describe every apartment in a list.

## init fills in a new object
`EstateAgent("Kim", "Majorna")` makes an object, and `__init__` runs right then, by itself. 
It saves the values in the object with `self.name = name`.

`self` is the object the method works on. That is why a method has one more name in its parentheses than you write in the call.
Without `self.`, a value is gone when the method ends. To be able to call a method or store a value in an instance of the class you need to use `self`.

## Data and the code for it live together
An attribute is a value stored in the object, like kim.name. A method is a function defined in the class, called with parentheses: kim.total().
Keeping both in one class means the code that works on an agent lives next to the agent's data.

## A class can refuse wrong data
A home with 0 square meters cannot exist. `raise ValueError(...)` in `__init__` stops the program before such an object is made, so the mistake shows where it happened.

## Text for users, text for developers
`__str__` gives and object's text for users, in `print` and f-strings `__repr__` gives its text for developers, the way you would write it in code, and a list uses it. Without either, you see only the class and a memory address.

## Inherit only when "is a" is true
With inheritance, a class gets all the attributes and methods of another class, and can override some or add its own. A cat is an animal, so Cat can inherit from Animal, and give speak() its own answer. When each kind of animal answers the same call in its own way, thats polymorphism. `super().__init__(...)` lets Animal set up its part first.

Something that only belongs with a home, like the agent who sells it, is not a home. Then inheritance is wrong.