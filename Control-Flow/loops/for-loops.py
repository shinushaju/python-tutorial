# Python Looping Flow Control - for loop

'''
The for loop in Python is used to iterate over a sequence such as string, list, set, tuple etc., or other iterable objects.
A loop takes the first item of the sequence, executes the loop body, and moves the pointer to the next item until it reaches
the last item of the sequence. The loop body is separated from the rest of the code using indentation.

The range() function is used with a loop to specify the range (how many times) the code block will be executed.
The range() function returns a sequence of numbers starting from 0 (by default) if the initial limit is not specified and it increments by 1 (by default) until a final limit is reached.
Three ways in which a range() function can be used:
1. range(stop)
2. range(start, stop)
3. range(start, stop, step)

For loop with else: The else part is executed if the items in the sequence used in for loop exhausts.
Means, If no break occurs in the for loop the else block will be executed immediately after for block finishes execution.

Loop control statements:
1. break - used to terminate the loop
2. continue - skips the current iteration of a loop and immediately jumps to the next iteration
3. pass -  statement is a null statement, i.e., nothing happens when the statement is executed.

Nested for loops - For loop inside another for loop.
In nested loops, the inner loop finishes all of its iteration for each iteration of the outer loop.
i.e., For each iteration of the outer loop inner loop restart and completes all its iterations, then the next iteration of the outer loop begins.

We can use the built-in function reversed() with for loop to change the order of elements, and this is the simplest way to perform a reverse looping.

Refer:
https://www.geeksforgeeks.org/loops-in-python/
https://www.programiz.com/python-programming/for-loop
https://www.scaler.com/topics/python/for-loop-in-python/
'''

'''
1. Write a program to iterate over a list named roles having elements Architect, Engineer, Developer, Tester, Manager. Display each item in the list.
2. Write a program to find the sum of all numbers stored in a list [3, 5, 7, 12, 26, 31]. Display the sum.
3. Write a program to print all letters in a given string except for vowels.
'''

# # list of roles
# roles = ['Architect', 'Engineer', 'Developer', 'Tester', 'Manager']
# size = len(roles)
# print(f"Length of the list is {size}")
# # for role in roles:
# #     print(role)
# print(list(range(size)))
# for role in range(size):
#     print(f"Role '{roles[role]}' at index position {role}")
    
# # list of numbers
# numbers = [3, 5, 7, 12, 26, 31, 6]
# sum_of_numbers = 0
# for number in numbers:
#     sum_of_numbers = sum_of_numbers + number
# print(f"Sum of numbers in the list is {sum_of_numbers}")

# print(list(range(10)))
# print(list(range(5,10)))
# print(list(range(0,10,2)))

'''
Write a program to find the sum of first 100 even numbers. (Hint: range() with for loop)
'''
# sum_of_numbers = 0
# for i in range(2,101,2):
#     print(i)
#     sum_of_numbers += i
# print(f"Sum of first 100 even numbers is {sum_of_numbers}")

# # print first 10 natural numbers
# numbers = [3, 5, 7, 12, 26, 31, 6]
# num = 26
# for number in numbers:
#     print(number)
#     if num == number:
#         print(f"Digit {num} exists in the list.")
# else:
#     print(f"Digit {num} doesn't exist in the list. No more item present in the list")
    
# print("Exited for loop. Resuming program...")

# str_variable = 'DevOps Engineer'
# for char in str_variable:
#     if char == 'O' or char == 'o':
#         # loop control statement to terminate the looping process
#         break
#     print(char)

# names = ['Samrika', 'Bhavana', 'Divya', 'Shinu']
# cities = ['Delhi', 'Mumbai', 'Bengaluru', 'Chennai']

# # outer loop
# for name in names:
#     # outer loop body
#     # inner loop
#     for city in cities:
#         # inner loop body
#         print(f"{name} likes {city}.")
#         # inner loop body ends
#     else:
#         print("Inner loop iteration completed.")
#     # outer loop body ends
# else:
#     print("Outer loop iteration completed.")

# # reversed
# numbers = [3, 5, 7, 12, 26, 31, 6]
# print(numbers)
# print(list(reversed(numbers)))
# for num in reversed(numbers):
#     print(num)