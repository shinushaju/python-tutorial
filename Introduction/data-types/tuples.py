# Python Tuples

'''
Tuple is an ordered sequence of items same as a list but written within parentheses.
The only difference is that tuples are immutable. Tuples are more memory efficient and faster compared to Lists.

Refer: https://www.geeksforgeeks.org/python-tuples/
'''
import sys

# create an empty tuple
my_tuple = ()
print(f"\nEmpty Tuple {my_tuple}")
print(f"Type of {my_tuple} is {type(my_tuple)}")

# create tuple without parentheses
my_tuple = 'Car', 'Bike'
print(f"\nTuple created without parentheses => {my_tuple}")
print(f"Type of {my_tuple} is {type(my_tuple)}")

# create tuple with parentheses
my_tuple = ('Python', 'C++', 'Java')
print(f"\nTuple created with parentheses => {my_tuple}")
print(f"Type of {my_tuple} is {type(my_tuple)}")

# create a tuple using List using tuple() function
my_list  = ["React", "Angular", "Vue"]
tuple_from_list = tuple(my_list)
print(f"\nTuple created from the list {my_list} is {tuple_from_list}.")
print(f"Type of {tuple_from_list} is {type(tuple_from_list)}")

# Tuples are more memory efficient and faster compared to Lists.
# get the memory size of list and tuple using getsizeof() from sys module
print(f"\nMemory size of list {my_list} is {sys.getsizeof(my_list)}")
print(f"Memory size of tuple {tuple_from_list} is {sys.getsizeof(tuple_from_list)}")

# tuple containing items of different data types
different_types_tuple = (6, 24.66, "Ginger", "Flute", 5+6j)
print(f"\nTuple containing items of different data types {different_types_tuple}")

# tuple containing duplicate items
duplicate_items_tuple = (5, 5, 6, 6, "Den", "Den", 5)
print(f"\Tuple containing duplicate items {duplicate_items_tuple}")

# length (or number of items) of the tuple using len() function
print(f"\nLength of tuple {different_types_tuple} is {len(different_types_tuple)}.\nLength of tuple {duplicate_items_tuple} is {len(duplicate_items_tuple)}.")

# Index operator [ ] is used to access an item in a tuple.
# access the first element from a tuple
first_item = my_tuple[0]
print(f"\nFirst item in the tuple {my_tuple} is {first_item}")
# access the 2nd item from tuple
tuple_item = my_tuple[1]
print(f"Second item in the tuple {my_tuple} is {tuple_item}")

# In Python, negative indexes represent positions from the end of the tuple.
# access last item from a tuple
last_item = my_tuple[-1]
print(f"Last item in the tuple {my_tuple} is {last_item}")

# access a range of items from the tuple using slice operator [n:m]
new_tuple = duplicate_items_tuple[1:4]
print(f"\nRange of items from the list {duplicate_items_tuple} is {new_tuple}")

# # delete an entire list object using del keyword
# del my_list
# print(my_list)