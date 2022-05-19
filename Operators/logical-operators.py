# Python Operators - Logical Operators

'''
Logical operators perform Logical AND, Logical OR, and Logical NOT operations.
It is used to combine conditional statements.

Refer: https://www.geeksforgeeks.org/python-logical-operators-with-examples-improvement-needed/
'''

# Python program to demonstrate
# logical and operator

num1 = 23
num2 = 0
var = False

# logical AND operator 'and'
if num1 > 0 and num2 > 0:
	print("Both numbers are greater than 0.")
else:
    print("Both numbers are not greater than 0.")

# logical OR operator 'or'
if num1 > 0 or num2 > 0:
	print("Atleast one number is greater than 0.")
else:
	print("Neither of the number is greater than 0.")

'''
The 'not' is a Logical operator in Python that will return True if the expression is False.
'''
# logical NOT operator 'not'
result = not var
print(result)