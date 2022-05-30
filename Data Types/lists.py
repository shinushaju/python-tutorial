# Python List Methods

'''
Refer: https://www.geeksforgeeks.org/list-methods-python/
'''

# numbers = [5,9,2,1,7,4,6,8]

# chars = ['data', 'account', 'alpha', 'chicken', 'food']

# append() - Add a single element to the end of the list
# parameter - item
'''
Read 5 integer input items from user and add it to the list. (Hint: for loop)
'''
# for i in range(5):
#     item = int(input(f"Enter input {i+1}: "))
#     numbers.append(item)
# i = 0
# while i < 5:
#      item = int(input(f"Enter input {i+1}: "))
#      numbers.append(item)
#      i += 1
     
# insert() - inserts an element to the list at the specified index.
# parameters - index, item
# numbers.insert(4, 8)

# extend() - adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# parameter - iterable object
# add number 3,5,6,7,8 to numbers all together
# list_item = '2345678'
# numbers.extend(list_item)
# print(numbers)

# copy() - returns a shallow copy of the list.
# new_list = numbers.copy()
# using'=' operator
# new_list = numbers
# print(new_list)

# count() - returns the number of times the specified element appears in the list.
# parameter - item
# print(numbers.count(88))

# index() - returns the index of the specified element in the list.
# parameter - item
# print(numbers.index(-2))

# pop() - removes the item at the given index from the list and returns the removed item.
# parameter - index of item
# print("Before",numbers)
# removed_item = numbers.pop()
# print(removed_item)
# print("After",numbers)

# remove() - removes the first matching element from the list.
# parameter - item
# numbers.remove()
# print(numbers)

# reverse() - reverses the elements of the list.
# numbers.reverse()
# print(numbers)

# sort() - sorts the items of a list in ascending or descending order.
# reverse = True sorts the list in the descending order.
# print("Before sorting", chars)
# chars.sort(reverse=True)
# print("After sorting", chars)

# clear() - removes all items from the list.
# print(numbers)
# numbers.clear()
# print("After removing all items",numbers)