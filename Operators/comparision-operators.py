# Python Operators - Comparision (Relational) Operators

'''
Comparison operators are used to compare values. It returns either True or False according to the condition.

Refer: https://www.geeksforgeeks.org/relational-operators-in-python/
'''

# read two integer inputs from user
num_var1 = int(input("Enter first number: "))
num_var2 = int(input("Enter second number: "))
# display the numbers
print(f"The numbers are {num_var1} and {num_var2}.\n")

# check whether the 1st number is greater than 2nd number using greater than '>' operator
result = num_var1 > num_var2
print(f"{num_var1} is greater than {num_var2}: {result}")

# check whether the 1st number is smaller than 2nd number using less than '<' operator. 
result = num_var1 < num_var2
print(f"{num_var1} is less than {num_var2}: {result}")

# check whether the 1st number is equal to 2nd number using equal to '==' operator. Returns True if they are equal.
result = num_var1 == num_var2
print(f"{num_var1} is equal to {num_var2}: {result}")

# check whether the 1st number is equal to 2nd number using not equal to '!=' operator. Returns True if they are not equal.
result = num_var1 != num_var2
print(f"{num_var1} is equal to {num_var2}: {result}")

# check whether the 1st number is greater than or equal to 2nd number using greater than or equal to '>=' operator
result = num_var1 >= num_var2
print(f"{num_var1} greater than or equal to {num_var2}: {result}")

# check whether the 1st number is less than or equal to 2nd number using less than or equal to '<=' operator
result = num_var1 <= num_var2
print(f"{num_var1} less than or equal to {num_var2}: {result}")