# Python Type Conversion

'''
Converting the value of one data type to another data type is called type conversion.
There are two types of Type Conversion in python:
1. Implicit Type Conversion - Python interpreter automatically converts one data type to another without any user involvement.
2. Explicit Type Conversion - The data type is manually changed by the user as per their requirement.

Some of the Explicit Type Conversions in Python are listed below:
int() - Converts a data type to integer
float() - Converts a data type to floating-point number
str() - Converts a data type to string
list() - Converts a data type to list
tuple() - Converts a data type to a tuple
set() - First, converts a data type to set and returns type
dict() - Converts a tuple of order (key,value) into a dictionary
complex(real,imag) - Converts real numbers to complex(real,imag) number
ord() - Converts a character to integer
hex() - Converts integer to hexadecimal string
oct() - Converts integer to octal string

Refer: https://www.geeksforgeeks.org/type-conversion-python/
'''

var1 = 10; # variable assigned with int value
var2 = 2.3445 # variable assigned with float value
var3 = 3+5j # variable assigned with complex number
var4 = "Python 3" # variable assigned with string value
var5 = [2,4,6,8] # variable assigned with a list
var6 = (1,3,5,7) # variable assigned with a tuple
var7 = {'a', 'e', 'i', 'o'} # variable assigned with a set
var8 = {1: 'a', 2: 'e', 3: 'i', 4: 'o'} # variable assigned with a dictionary

# use type() function to display of each of the varible
print(f"Type of variable var1 is: {type(var1)}")
print(f"Type of variable var2 is: {type(var2)}")
print(f"Type of variable var3 is: {type(var3)}")
print(f"Type of variable var4 is: {type(var4)}")
print(f"Type of variable var5 is: {type(var5)}")
print(f"Type of variable var6 is: {type(var6)}")
print(f"Type of variable var7 is: {type(var7)}")
print(f"Type of variable var8 is: {type(var8)}")

# convert a variable to integer using int()
new_var = "123456789"
int_var = int(new_var)
print(f"\nAfter converting {new_var} to integer: {int_var}")
print(f"Type of new variable 'int_var' is: {type(int_var)}")

# convert a variable to float using float()
new_var = "2"
float_var = float(new_var)
print(f"\nAfter converting {new_var} to float: {float_var}")
print(f"Type of new variable 'float_var' is: {type(float_var)}")

# convert a variable to string using str()
new_var = 12345
string_var = str(new_var)
print(f"\nAfter converting {new_var} to string: {string_var}")
print(f"Type of new variable 'string_var' is: {type(string_var)}")