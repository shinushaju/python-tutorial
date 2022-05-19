# Python Operators - Membership Operators

'''
They are used to test whether a value or variable is found in a sequence  like string, list, tuple, set and dictionary.
The 'in' operator is used to check if a value exists in a sequence or not. The 'is not' operator evaluates the opposite.
Evaluate to true if it finds a variable in the specified sequence and false otherwise.
It is used with conditional and looping statements.

Refer: https://www.geeksforgeeks.org/python-membership-identity-operators-not-not/
'''

# a python list
num_list = [2, 4, 6, 8, 12]

# read an integer input from user
item = int(input("Enter number: "))

# check whether item is present in the list using 'in' operator
print("\nUsing 'in' operator")
if item in num_list:
    print(f"{item} is PRESENT in {num_list}.")
else: 
    print(f"{item} is NOT PRESENT in  {num_list}")
    
# check whether item is present in the list using 'not in' operator
print("\nUsing 'not in' operator")
if item not in num_list:
    print(f"{item} is NOT PRESENT in  {num_list}")
else: 
    print(f"{item} is PRESENT in {num_list}.")