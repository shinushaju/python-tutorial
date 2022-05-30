# Python String Methods

'''
Python has a set of built-in methods that you can use on strings.
Every string method does not change the original string instead returns a new string with the changed attributes.

Refer: https://www.geeksforgeeks.org/python-string-methods/
'''

# str_var = "Python is Easy. Python is Fun. Python is fast."
# print(len(str_var))
# # capitalize() - converts first character to Capital Letter
# print(str_var.capitalize())

# # casefold() - converts string to lower case
# print(str_var.casefold())

# center() - pad the string with the specified character. Two parameters - length & fillchar
# new_str = str_var.center(50, '^')
# print(new_str)
# print(len(new_str))

# count() - returns the number of occurrences of a substring in the string.
# parameters - substring (Mandatory), start & stop (Optional)
# print(str_var.count('t'))
# print(str_var.count('Python', 17, 36))

# find() - returns the lowest index of the substring if it is found in a given string. returns -1 if not found.
# parameters - substring, start & stop (Optional)
# print(str_var.find('is'))
# print(str_var.find('Python', 5, 42))

# index() - returns the position of the first occurrence of a substring in a string.
# parameters - substring, start & stop (Optional)
# print(str_var.index('.'))
# print(str_var.index('un', 6, 32))

# # isalpha() - returns “True” if all characters in the string are alphabets, Otherwise, It returns “False”.
# print('python3'.isalpha())

# # isalnum() - checks whether all the characters in a given string are alphanumeric or not.
# print('python3'.isalnum())

# # isdigit() - returns “True” if all characters in the string are digits, Otherwise, It returns “False”.
# print('123'.isdigit())

# # isnumeric() - returns “True” if all characters in the string are numeric characters, Otherwise, It returns “False”.
# print('123'.isnumeric())

# # islower() -  returns True if all alphabets in a string are lowercase alphabets.
# print('data'.islower())

# # isupper() - returns whether or not all characters in a string are uppercased or not.
# print('DATa 123'.isupper())

# # istitle() - returns True if the string is a titlecased string otherwise it returns False.
# print('Python Is Easy'.istitle())

# # lower() - converts all uppercase characters in a string into lowercase characters and returns it.
# print(str_var.lower())

# # upper() -  converts all lowercase characters in a string into uppercase characters and returns it.
# print(str_var.upper())

# # replace() - returns a copy of the string where all occurrences of a substring are replaced with another substring
# # paramters - old, new, count
# str_new = str_var.replace('is', '-', 2)
# print(str_new)

# strip() - returns a copy of the string with both leading and trailing characters removed (based on the string argument passed).
# strip_var = "@@Python 3###"
# print(strip_var)
# str_new = strip_var.strip('#')
# print(str_new)

# # split() - breaks up a string at the specified separator and returns a list of strings.
# # parameters -  seperator & maxsplit
# print(str_var.split('.'))

# # startswith() - returns True if a string starts with the given prefix otherwise returns False.
# # parameters - string, start, end
# # case sensitive
# print(str_var.startswith('Python', 16, -1))