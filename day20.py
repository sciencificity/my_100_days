# 1:0: C0111: Missing module docstring (missing-docstring)
""" Pylint Example"""
# 14:1: C0303: Trailing whitespace (trailing-whitespace)
# pylint: disable = trailing-whitespace
# Using pylint
# Inspects your code and ensures code follows a style guide, does not have bugs etc.
# and gives you feedback
# E.g. checks with PEP8 Style guide if you following that convention
# install pylint: pip install pylint
# Use on CLI by calling:
# > pylint path\file.py

# Here is my badly formatted code
# class car:
#     def __init__(self, color):
#         self.color = color
# 
# my_car = car('blue')        
# 
# def    crash(car1, car2) :
#     car1.color = 'burnt'
# 
# crash(car('red'), my_car)


# 19:0: C0103: Class name "car" doesn't conform to PascalCase naming style (invalid-name)
#     Expecting capital letter as first letter - we have a small letter, so amend that
# 21:0: R0903: Too few public methods (0/2) (too-few-public-methods)
#     Add a pylint ignore here
# pylint: disable = too-few-public-methods
class Car:
    """Example class""" # C0111: Missing function docstring (missing-docstring)
    # 20:21: C0326: Exactly one space required after comma
    def __init__(self, color): # add space after ,
        self.color = color

# 28:0: C0103: Constant name "my_car" doesn't conform to UPPER_CASE naming style (invalid-name)
# Fix: Change from my_car to MY_CAR
MY_CAR = Car('blue')        

# 26:25: C0326: No space allowed before : Fix = remove space before  :
# 30:19: W0613: Unused argument 'car2' (unused-argument) - special command:
#   Ask pylint to ignore that specific error
def crash(car1, car2): #pylint: disable = unused-argument
    """An example fn""" # 31:0: C0111: Missing function docstring (missing-docstring)
    car1.color = 'burnt'

crash(Car('red'), MY_CAR)
