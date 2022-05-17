# Python Identifiers

'''
An identifier is a name given to entities like class, functions, variables, etc.
It is a user-defined name to represent the basic building blocks of Python.

Refer: https://www.geeksforgeeks.org/python-keywords-and-identifiers/
'''
# the 'isidentifier()' checks the validity of an identifier name while keeping the keywords in mind.

# identifier names can start with an underscore.
print('_dev'.isidentifier()) # valid identifier
print('_'.isidentifier()) # valid identifier

# an identifier cannot start with a digit.
print('1dev'.isidentifier()) # invalid identifier
print('dev1'.isidentifier()) # valid identifier

# keywords cannot be used as identifiers.
print('For'.isidentifier()) # invalid identifier

# we cannot use special symbols like !, @, #, $, % etc. in our identifier.
print('x+iy'.isidentifier()) # invalid identifier

# python identifier can’t contain only digits.
print('123'.isidentifier()) # invalid identifier