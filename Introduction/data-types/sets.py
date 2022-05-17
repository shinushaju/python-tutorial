# Python Sets

'''
Set is an unordered collection of data type that is iterable and mutable.
Set is defined by values separated by comma inside braces { } or using set() function. Items in a set are not ordered.
Items in the Sets can be of different data types. Set cannot contain duplicate elements.
Elements of sets are immutable. A Set cannot have immutable elements like a list or dictionary, as it is mutable.
'''

# create an empty Set
my_set1 = set()
print(f"\nEmpty Set {my_set1}")
print(f"Type of {my_set1} is {type(my_set1)}")

# create a non-empty set by defining values separated by comma inside braces { }
my_set2 = {6, 3, 7, 4, 1, 9}
print(f"\nSet created by defining values separated by comma inside braces {my_set2}")
print(f"Type of {my_set2} is {type(my_set2)}")

# create a Set with a String object
str_value = "Python"
my_set3 = set(str_value)
print(f"\nSet created with String object {my_set3}")

# create a Set using a List
my_list = [8, 44, 32, 14, 52, 16]
my_set4 = set(my_list)
print(f"\nSet created with a List {my_set4}")

# create a Set using a List of items with different data types
data_types_list = [2, "Car", 1.45, 2+5j]
my_set4 = set(data_types_list)
print(f"\nSet created with a List of different data types {my_set4}")

# create a Set using a List of numbers with duplicate values
num_list = [1, 2, 2, 3, 3, 4, 4, 6]
my_set5 = set(num_list)
print(f"\nSet created with a List of numbers with duplicate values {my_set5}")

'''
Order of elements in a set is undefined and is unchangeable.
So indexing won't work. The slicing operator [] does not work.
'''
# try to access set item with indexing method 
# print(my_set5[0])

'''
Sets are mutable. But, elements of sets are immutable.
Therefore, Set cannot have immutable elements like a list or dictionary.
'''
# try to create a set with an immutable element like list.
# set_with_list = {1, [2, 4, 6], 3, 7}
# print(set_with_list)

# delete an entire set using del() function
# del my_set5
# print(my_set5)