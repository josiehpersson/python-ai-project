# keeping an object's data behind methods and properties, so that it can only change by the class's rules, is called encapsulation.
class Commission:
    def __init__(self, rate: float):
        self.rate = rate
    
    # makes rate look like an attribute from outside: commission.rate, no parenthesese.
    @property
    def rate(self):
        return self._rate

    # runs every time someone writes commission.rate = ...
    # both methods are called rate: the first one reads the value, the second one writes it.
    @rate.setter
    def rate(self, value: float):
        # is true when the value is between 0 and 0.1.
        # not turns it around, so the if runs when the valie is outside of 0 and 0.1
        if not 0 <= value <= 0.1:
            raise ValueError(f"rate must be between 0 and 0.1, not {value}")
        # holds the value itself. The _ at the start says "use the property, not me".
        self._rate = value

commission = Commission(0.03)
print(commission.rate)
commission.rate = 0.5

# Output:
# 0.03 <-- from Commission(0.03)
# Traceback (most recent call last):
#  File "/Users/you/python-ai-project/practice/module_04/theory.py", line 18, in <module>
#    commission.rate = 0.5
#    ^^^^^^^^^^^^^^^
#  File "/Users/you/python-ai-project/practice/module_04/theory.py", line 12, in rate
#    raise ValueError(f"rate must be between 0 and 0.1, not {value}")
#ValueError: rate must be between 0 and 0.1, not 0.5