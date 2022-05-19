# Python Operators - Membership Operators

'''
They are used to check if two values (or variables) are located on the same part of the memory.
Two variables that are equal does not imply that they are identical.

Refer: https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/
'''

var1 = 5
var2 = 'John'
print(f"The values are {var1} and {var2}.\n")

# use 'is' operator to check type of input is int or not
print(type(var1) is int) # returns True if type is int
print(type(var2) is int) # returns True if type is int

# use 'is not' operator to check type of input is int or not
print(type(var1) is not int) # returns False if type is int
print(type(var2) is not int) # returns False if type is int

# use 'is' to check if values of inputs are same or not
print(var1 is var2) # returns True if both values are identical

# use 'is not' to check if values of inputs are same or not
print(var1 is not var2) # returns True if both values are NOT identical