# Python Operators - Arithmetic Operators

'''
Arithmetic operators are used to perform mathematical operations like addition, subtraction, multiplication, etc.

Refer: https://www.geeksforgeeks.org/python-arithmetic-operators/
'''

# read two integer inputs from user
num_var1 = int(input("Enter first number: "))
num_var2 = int(input("Enter second number: "))
# display the numbers
print(f"The numbers are {num_var1} and {num_var2}.\n")

# find the sum of the numbers using '+' operator
result = num_var1 + num_var2
print(f"Sum of the numbers are {result}.")

# find the difference between the numbers using '-' operator
result = num_var1 - num_var2
print(f"Difference between the numbers are {result}.")

# find the product of the numbers using '*' operator
result = num_var1 * num_var2
print(f"Product of the numbers are {result}.")

# divide first number by second number using '/' operator
result = num_var1 / num_var2
print(f"Division result is {result}.")

# find modulo of numbers using '%' operator
result = num_var1 % num_var2
print(f"Modulo of numbers is {result}.")

# floor division of numbers using '//' operator
result = num_var1 // num_var2
print(f"Floor division result is {result}.")

# find power n**m of numbers using '**' operator
result = num_var1 ** num_var2
print(f"Power of {num_var1}**{num_var2} is {result}.")
