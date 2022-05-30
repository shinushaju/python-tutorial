# Python Dictionary Methods

'''
Refer: https://www.geeksforgeeks.org/python-dictionary-methods/
'''

# mydict = {'name':'Rohit', 'age': 34, 'team': 'Mumbai'}
# num = {1:1, 2:2, 4:4}
# add items in a dictionary
# Syntax: dictionary_name[newKey] = newValue
# mydict['team'] = 'Mumbai' 
# print(len(mydict))

# keys() - returns a view object that displays a list of all the keys in the dictionary
# print(mydict.keys())

# values() - returns a view object that displays a list of all the values in the dictionary.
# print(mydict.values())

# items() - returns a view object that displays a list of dictionary's (key, value) as tuple pairs.
# print(mydict.items())

# get() - returns the value for the specified key if the key is in the dictionary.
# parameters - key, value (optional)
# item = mydict.get('age')
# print(item)

# pop() -  removes and returns an element from a dictionary having the given key.
# parameters - key, value
# removed_item = mydict.pop('age')
# print(removed_item)
# print(mydict)

# popitem() - removes and returns the last element (key, value) pair inserted into the dictionary.
# print(num)
# removed_item = num.popitem()
# print(removed_item)
# print(num)

# copy() - returns a copy (shallow copy) of the dictionary.
# copy_dict = mydict.copy()
# print(copy_dict)

# clear() - removes all items from the dictionary.
# mydict.clear()
# print(mydict)

# update() - updates the dictionary with the elements from another dictionary object or from an iterable of key/value pairs.
# this method takes either a dictionary or an iterable object of key/value pairs (generally tuples).
# new_dict = {'nationality': 'India', 'caps': 300, '100s': 43, '50s': 56}
# mydict.update(new_dict)
# print(mydict)

# setdefault() - returns the value of a key (if the key is in dictionary). If not, it inserts key with a value to the dictionary.
# res = mydict.setdefault('nationality', 45)
# print(res)
# print(mydict)

# fromkeys() - creates a new dictionary from the given sequence of elements with a value provided by the user.
# parameter -  sequence, value(optional)
# my_list = [1,2,3,4,5]
# value = 'data'
# new_dict = dict.fromkeys(my_list, value)
# print(new_dict)