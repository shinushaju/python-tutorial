# Python Operators - Assignment Operators

'''
Assignment operators are used in Python to assign values to variables.

Refer: https://www.geeksforgeeks.org/assignment-operators-in-python/
'''

# read an integer input from user
num_var1 = int(input("Enter number: "))
# display the number
print(f"The number is {num_var1}.\n")

# assignment operator '='
num_var2 = num_var1
print(f"Assigned number is {num_var2}.\n")

# add and assign operator '+='
num_var1 += num_var1
print(f"Updated number is {num_var1}.\n")

# subtract and assign operator '-='
num_var1 -= num_var1
print(f"Updated number is {num_var1}.\n")

# multiply and assign operator '*='
num_var1 *= num_var1
print(f"Updated number is {num_var1}.\n")

# divide and assign operator '/='
num_var1 /= num_var1
print(f"Updated number is {num_var1}.\n")

# modulus and assign operator '%='
num_var1 %= num_var1
print(f"Updated number is {num_var1}.\n")

# floor division and assign operator '//='
num_var1 //= num_var1
print(f"Updated number is {num_var1}.\n")

# exponent and assign operator '**='
num_var1 **= num_var1
print(f"Updated number is {num_var1}.\n")

# bitwise AND and assign operator '&='
num_var1 &= num_var1
print(f"Updated result after bitwise AND is {num_var1}.\n")

# bitwise OR and assign operator '|='
num_var1 |= num_var1
print(f"Updated result after bitwise OR is {num_var1}.\n")

# bitwise XOR and assign operator '^='
num_var1 ^= num_var1
print(f"Updated result after bitwise NOT is {num_var1}.\n")

# bitwise right shift and assign operator '>>='
num_var1 >>= num_var1
print(f"Updated result after bitwise right shift is {num_var1}.\n")

# bitwise right shift and assign operator '<<='
num_var1 <<= num_var1
print(f"Updated result after bitwise left shift {num_var1}.\n")
