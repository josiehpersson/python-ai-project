# OOP advanced
- a dataclass: a shorter way to write a class that holds data.
- compositions: a class that uses other classes.
- a property: a class that checks every new value.

## @dataclass writes the routine methods
You list the attributes and their types, `name:str`, and @dataclass writes `__init__`, `__repr__` and `==` from that list. It suits a class whose main job is to keep a few values together.

A dataclass compare values: two objects with the same values are equal. 
`@dataclass(frozen=True)` makes the value unchangeable after the object is made.

## Composition: a class keeps another object
With composition, an object keeps another object as one of its attibutes, and uses it. A listing has a home and an agent: `listing.home` and `listing.agent`.

The listing inherits nothing. It reaches the homes values through the attribute: `listing.home.district`.

## "is a" or "has a"
Ask which one is true:
- Is a: a cat is an animal. Inheritance fits.
- Has a: an office has agents. Composition fits.

The two are not equal choices. Inheritance ties two classes together for good, while an attribute can be swapped for another object later.
That is why composition is the safer start when both seem to fit.

## A property checks every value
A property looks lite an attribute from the outside, `commission.rate`, but a method runs each time it is read or set.
Its setter can refuse a value that makes no sense.

That is encapsulation: the class has the last word on its own data, so no other code can leave an object in a state that maked no sense.
The _ in _rate is a sign to other programmers, not a lock.

## A test checks an answer you know
A test is a small function with an `assert` that checks a result you can work out yourself. 
pytest runs every function whose name starts with `test_`, in files whose name starts with "test_".  

A dot `.` is a test that passed, an `F` is one that failed.
A failing test points to the line with `>`, and shows the value with `E`. 