# Python Input

'''
In Python, we have input() function to take input from the user.
The syntax for input() is:

input(prompt) 

- prompt is the optional message we want to display on screen.

The input() function first takes the input from the user and convert it into string.
Type of the returned object always will be <type 'str'>. So, we need to explicitly convert it into the data type we need.
'''

# read an integer input from user and assign it to a variable
user_input = input()
# print the user input
print(f"User input is: {user_input}")
# print the type of the user input
print(f"Type of user input is: {type(user_input)}")
# convert the user input to integer using int()
# user_input = int(user_input)
# print(f"Type of  user input after converting to integer: {type(user_input)}")

# read the current year as an input from user with a prompt message and assign it to a variable
current_year = input("\nEnter the current year: ")
# print the user input
print(f"Current year is: {current_year}")
# print the type of the user input
print(f"Type of user input is: {type(current_year)}")

# read a number as an integer input from user
date = int(input("\nEnter today's date: "))
# print the user input
print(f"Today's date is: {date}")
# print the type of the user input
print(f"Type of user input is: {type(date)}")
