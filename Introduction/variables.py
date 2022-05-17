#Python Variables

'''
A python variable is a named location used to store data in the memory.
A variable is created the moment we first assign a value to it.
The value stored in a variable can be changed during program execution.
Python variable types:
1. Local
2. Global

Things to remember while creating variables in python:
    1. A variable name must start with a letter or the underscore character.
    2. A variable name cannot start with a number.
    3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ ).
    4. Variable names are case-sensitive (name, Name and NAME are three different variables).
    5. The reserved words(keywords) cannot be used naming the variables.
    
Refer: https://www.geeksforgeeks.org/python-variables/
'''

# declare and assign a value to variables
# syntax ==> variable name = variable value
number = 3
Number = 7
_number = 10
user_name = 'John Doe'

# display the varible values using print statement
print("\nVariable 'number' value is", number)
print("Variable 'Number' value is", Number)
print("Variable '_number' value is", _number)
print("Variable 'user_name' value is", user_name)

'''
Note: Python is a dynamically typed language, so you don't have to explicitly define the variable type.
It automatically knows that 'John Doe' is a string and declares the user_name variable as a string.
'''
# print the variable type using 'type()' function
print("\nVariable 'number' type is", type(number))
print("Variable 'Number' type is", type(Number))
print("Variable '_number' type is", type(_number))
print("Variable 'user_name' type is", type(user_name))

'''
We can re-declare the python variable once we have declared the variable already.
'''
# re-declare a variable
number = 'Two'
print("\nRe-declared variable 'user_name' value is", number)
print("Variable 'number' type is", type(number))

'''
Python allows assigning a single value to several variables simultaneously with “=” operators. 
'''
# assigning multiple values to multiple variables
var1, var2, var3 = 3, 3.8, "Python3"
# assigning the same value to multiple variables at once
# var1 = var2 = var3 = 'Python3'
# print the variable values
print("\nVariable 'var1' value is",var1)
print("Variable 'var2' value is",var2)
print("Variable 'var3' value is",var3)

'''
You can delete Python variables using the command del “variable name”.
'''
# delete a python variable
del(var1); del(var2); del(var3)
print()
print(var1); print(var2); print(var3)