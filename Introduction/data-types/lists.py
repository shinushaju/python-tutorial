# Python Lists

'''
List is an ordered sequence of items written within square brackets [ ]. Python Lists are mutable.
List in Python are ordered and have a definite count. The len() function returns the length of the List.
Each element or value that is inside of a list is called an item. Index operator [ ] is used to access an item in a list.
Slice operation [n:m] can be used to access a specific range of items from the list.
'''

# create an empty list
my_list = []
print(f"Empty List {my_list}")
print(f"Type of {my_list} is {type(my_list)}")

# list of numbers
numbers_list = [2,4,6,8,3,9]
print(f"\nList of numbers {numbers_list}")

# list of strings
unicorns_list = ["CRED", "Unacademy", "CoinSwitch", "Flipkart"]
print(f"List of strings {unicorns_list}")

# list containing items of different data types
different_types_list = [3, 4.66, "CRED", 2+4j, "Flipkart"]
print(f"List containing items of different data types {different_types_list}")

# list containing duplicate items
duplicate_items_list = [3, 4, 3, 3, 4, 5, 1, 1]
print(f"List containing duplicate items {duplicate_items_list}")

# length (or number of items) of the list using len() function
print(f"\nLength of list {my_list} is {len(my_list)}.\nLength of list {unicorns_list} is {len(unicorns_list)}.")

# multi-dimesional list by nesting a list inside another list
multi_dimensional_list = [2, 3, [4,8,12], ["car", "bike", "bus"], [1.54, 3.76, 56.87], 5]
print(f"\nMulti-dimensional list {multi_dimensional_list}")

# Index operator [ ] is used to access an item in a list.
# access the first element from a list
first_item = numbers_list[0]
print(f"\First item in the list {numbers_list} is {first_item}")
# access the 5th item from list
list_item = numbers_list[4]
print(f"Last item in the list {numbers_list} is {list_item}")

# access element 'bike' from the multi-dimensional (nested) list.
print(f"Element from list {multi_dimensional_list} is {multi_dimensional_list[3][1]}.")

# In Python, negative indexes represent positions from the end of the list.
# access last item from a list
last_item = numbers_list[-1]
print(f"Fifth item in the list {numbers_list} is {last_item}")

# access a range of items from the list using slice operator [n:m]
new_list = duplicate_items_list[1:4]
print(f"\nRange of items from the list {duplicate_items_list} is {new_list}")

# delete an entire list object using del keyword
del my_list
print(my_list)