# Python Keywords

'''
Keywords are the reserved words in Python.
They are used to define the syntax and structure of the Python language.

Refer: https://www.geeksforgeeks.org/python-keywords-and-identifiers/
'''
# importing "keyword" for keyword operations from keyword module
import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is: ")
print(keyword.kwlist)
print()
# print total number of keywords
print("The number of keywords is: ")
print(len(keyword.kwlist))

# The 'keyword.iskeyword()' checks whether a string is a keyword or not
print(keyword.iskeyword('While'))