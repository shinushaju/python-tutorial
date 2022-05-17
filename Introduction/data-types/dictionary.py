# Python Dictionary

'''
Dictionary is an unordered collection of key-value pairs. They are mutable.
Dictionaries are defined within braces {} with each item being a pair in the form key:value. A colon (:) separates each key from its value.
Key and value can be of any type. Dictionary keys are case sensitive, the same name but different cases of Key will be treated distinctly.
Dictionaries can also be created with dict() function. This function takes a number of keywords arguments as input.
A Dictionary item can be accessed using its key name inside square brackets.
Generally used when we have a huge amount of data. Dictionaries are optimized for retrieving data.

Refer: https://www.geeksforgeeks.org/python-dictionary/
'''

# an empty dictionary using {}
my_dict = {}
print(f"\nEmpty dictionary created using {{}}: {my_dict}")
print(f"Type of {my_dict} is {type(my_dict)}")

# a dictionary with integer keys
my_dict1 = {1: 'Python', 2: 'C++', 3: 'Java'}
print(f"\nDictionary with integer keys:\n{my_dict1}")

# a dictionary with keys of mixed data types
my_dict2 = {'name': 'John Doe', 1: [1, 3, 7]}
print(f"\nDictionary with keys of mixed data types:\n{my_dict2}")

# an empty dictionary using dict()function
my_dict3 = dict()
print(f"\nEmpty dictionary created using dict() function: {my_dict3}")
print(f"Type of {my_dict3} is {type(my_dict)}")

# a non-empty dictionary using dict()function
my_dict4 = dict({1: 'a', 2: 'e', 3: 'i'})
print(f"\nNon-empty dictionary created using dict() function:\n{my_dict4}")

# dictionary with keys having the same name but different cases.
my_dict5 = {'name': 'Virat', 'Name': 'Rohit', 'NAME': 'Rahul'}
print(f"\nDictionary with keys having the same name but different cases:\n{my_dict5}")

# access dictionary item using its key
dict_item1 = my_dict5['name']
dict_item2 = my_dict5['Name']
dict_item3 = my_dict5['NAME']
print(f"\nItems inside the dictionary {my_dict4} are:\n{dict_item1}\n{dict_item2}\n{dict_item3}")

# If using [], then KeyError is raised if an invalid key is passed in.
# print(my_dict5['namE'])

# delete an entire dictionary using del keyword
# del my_dict5
# print(my_dict5)