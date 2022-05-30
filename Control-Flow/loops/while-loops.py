# Python Looping Flow Control - while loop
'''
The while loop in Python is used to iterate over a block of code as long as the expression (condition) is true.

How while loop works?
1. First, the expression is evaluated, if it returns true, control is passed to the indented statement(s) inside the while loop.
2. All the statements that are indented to the right below the while loop, for the body of the while loop and are executed.
3. Once the statements are executed control again passed to the expression and the expression is evaluated again, 
if it returns true, the body is executed again, this repeats until the expression returns false.
4. Once while loop break, control passed to the next unindented line of the while loop.

The else clause is only executed when your while condition becomes false.
If you break out of the loop, or if an exception is raised, it won't be executed.

while loop control statements are:

1. break - used to terminate the loop
2. continue - skips the current iteration of a loop and immediately jumps to the next iteration
3. pass -  statement is a null statement, i.e., nothing happens when the statement is executed

Refer:
https://www.scaler.com/topics/python/while-loop-in-python/
https://www.programiz.com/python-programming/while-loop
https://www.geeksforgeeks.org/loops-in-python/
'''

# print all natural numbers less than 10 using while
# num = 1
# while num < 10:
#     print(num)
#     num += 1
# else:
#     print("Loop condition returned false")
#     print(f"Value of num is {num}")

# print all items in the list using while loop (Hint: len())
# numbers = [2,5,77,34,21,3]
# i=0
# size = len(numbers)
# while i < size:
#     print(numbers[i])
#     i += 1

# program to display all characters other than vowels in a string using while.
# str_var = input("Enter the string: ")
# vowels = ['a','e','i','o','u']
# print(f"Length of the string {len(str_var)}")
# i=0
# while i < len(str_var):
#     if str_var[i] in vowels:
#         pass
#         # print(f"Character {str_var[i]} is present in {vowels}.")
#     print(str_var[i])
#     i += 1
# else:
#     print("Below is pass statement")
#     pass
#     print("Pass statement executed just before this statement")