# Python Set Methods

'''
Refer: https://www.geeksforgeeks.org/python-set-methods/
'''

# numbers = {1,3,4,5,7,8}
# numbers_copy = numbers

# add() - adds a given element to a set. If the element is already present, it doesn't add that element.
# parameter - item
'''
Read 7 items and add it to set numbers.
'''
# for i in range(7):
#     item = int(input(f"Enter set item {i+1}: "))
#     numbers.add(item)
# print(numbers)

# copy() - returns a shallow copy of the set.
# copy_set = numbers.copy()
# print(f"Original set {numbers}")
# print(f"Copy of the set {copy_set}")

# remove() - removes the specified element from the set.
# parameter - item
# print(numbers)
# numbers.remove(5)
# print(numbers)

# discard() - removes a specified element from the set (if present).
# parameter - item
# print(numbers)
# numbers.discard(5)
# print(numbers)

# pop() - returns and removes a random element from the set
# print("Before",numbers)
# removed_item = numbers.pop()
# print(removed_item)
# print("After",numbers)

# clear() - removes all elements from the set.
# numbers.clear()
# print(numbers)