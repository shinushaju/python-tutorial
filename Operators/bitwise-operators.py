# Python Operators - Bitwise Operators

'''
Bitwise operators act on operands as if they were strings of binary digits. They operate bit by bit, hence the name.

Refer: https://www.geeksforgeeks.org/python-bitwise-operators/
'''

num_var1 = 10 # binary value = 0000 1010
num_var2 = 4 # binary value = 0000 0100
# display the numbers
print(f"The numbers are {num_var1} and {num_var2}.\n")

# bitwise AND
result = num_var1 & num_var2
print(f"{num_var1} & {num_var2}: {result}")

# bitwise OR 
result = num_var1 | num_var2
print(f"{num_var1} | {num_var2}: {result}")

# bitwise NOT
result = ~ num_var1
print(f"~ {num_var1}: {result}")

# bitwise XOR
result = num_var1 ^ num_var2
print(f"{num_var1} ^ {num_var2}: {result}")

# bitwise right shift
result = num_var1 >> 2
print(f"{num_var1} >> 2: {result}")

# bitwise left shift
result = num_var1 << 2
print(f"{num_var1} << 2: {result}")