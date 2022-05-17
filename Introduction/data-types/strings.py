# Python Strings

'''
In Python, Strings are ordered sequence of Unicode characters.
All Strings are objects of the str class in Python. 
In Python, a single character is simply a string with a length of 1.
Strings are wrapped inside single, double, or triple quotes.
The len() function to retrieve the length of a string.
Python Strings are immutable. Attempt to modify a String will result in error.

Refer: https://www.geeksforgeeks.org/python-strings/
'''

# string created with single quotes.
str1 = 'This is a string created with single quotes.'
# string created with double quotes.
str2 = "This is a string created with double quotes."
# string created with triple quotes.
str3 = '''This is a string created using triple quotes.'''

# multi-line string created with triple double-quotes.
str4 = """This is a string created using triple double-quotes."""
# multi-line string created with triple quotes.
str5 = """This is a mult-line 
string created using 
triple quotes."""

# print all the string values
print(str1); print(str2); print(str3); print(str4); print(str5)

# all Strings are objects of the str class in Python.
print("\nType of string 'str1'",type(str1))

'''
In Python, there's no specific data type for characters.
A single character is simply a string with a length of 1.
'''
# variable assigned with a single character.
char = 'a'
print("\nType of string 'char' with single character is",type(char))

# In Python, the len() function returns the length of a string.
print("\nLength of string 'char' is",len(char))
print("Length of string 'str1' is",len(str1))

'''
In Python, individual characters of a String can be accessed by using Indexing. Python supports negative indexing as well.
While accessing an index out of the range will cause an IndexError.
Only Integers are allowed to be passed as an index, float or other types that will cause a TypeError.
'''
msg = "Python 3"

# assign the length of the new string to a variable
str_length = len(msg)
print("\nLength of string 'msg' is", str_length)



# access the first character of the string
print("First character of 'msg' is", msg[0])
# access the last character of the string
print("Last character of 'msg' is", msg[-1])
print("Last character of 'msg' using string length", msg[str_length-1])
# access the nth character of the string
print("Fourth character of 'msg' is", msg[3])

# access a character using negative indexing
print("Character at position -3 is", msg[-3])

# print()
# access an index out of range
# print(msg[10])
# pass other data type as an index
# print(msg[2.5])
# print(msg['string'])

'''
In Python, a range of characters in the String can be accessed using the String Slicing method.
It can be done by using slicing operator [n:m].
It returs the part of the string starting with the character at index n and not including the character at index m.
'''
# access a range characters of the string
print("\nCharacters between 2-6 of string 'msg' is", msg[2:6])

'''
Python Strings are immutable, hence In Python, updation or deletion of characters from a String is not allowed.
This will cause error. Only new strings can be reassigned to the same name.
Deletion of the entire string is possible with the use of del keyword. 
'''
# Trying to update a character of the string 'msg'
# msg[1] = 'N'
# print("\nUpdated character at 1st index of string 'msg' is", msg)
# Update the entire string 'msg'
# msg = "Python is Fun!"
# print("\nUpdated string 'msg' is", msg)

# Trying to delete a character of the string 'msg' using del keyword
# del msg[1]
# print("\After deleting character at 1st index of string 'msg'", msg)
# Delete the entire string 'msg' using del keyword
# del msg
# print(msg)

'''
Escape sequences allows you to include special characters in string. In Python, backslash \ is used as an escape character.
To ignore the escape sequences in a String, r or R is used, this implies that the string is a raw string and escape sequences inside it are to be ignored.
'''
esc_str1='Welcome to \'Python 3\' tutorial.'
print(esc_str1)
esc_str2="Welcome to \"Python 3\" tutorial."
print(esc_str2)
# ignore escape sequences in a string using r or R
esc_str3 = r'Welcome to \'Python 3\' tutorial.'
print(esc_str3)

'''
String formatting is also known as String interpolation.
It is the process of inserting a custom string or variable in predefined text.
'''

# Formatting string using format() method
'''
We put placeholders defined by a pair of curly braces {} in a text.
We call the string dot format method. Then, we pass the desired value into the method.
The method replaces the placeholders using the values in the order of appearance replace by value
'''
text_msg1 = "Python 3"
text_msg2 = "beginners"
text_msg3 = "Welcome!"
# format() method with single placeholder
print("This is a {} session.".format(text_msg1))
# format() method with multiple placeholder.
# number of placeholders must be same as number of values passed in format() method.
print("This is a {} session for {}.".format(text_msg1, text_msg2))

'''
Positional arguments - Insert values by using index-based position.
Add index numbers into the placeholders to reorder values. This affects the order in which the method replaces the placeholders.
'''
print("{2} This is a {0} session for {1}.".format(text_msg1, text_msg2, text_msg3))

'''
Keyword arguments - Insert values by using assigned keywords.
We insert keywords in the placeholders. Then, we call these keywords in the format method. We then assign each keyword with a variable.
'''
print("{msg1} This is a {msg2} session for {msg3}.".format(msg2=text_msg1, msg3=text_msg2, msg1=text_msg3))

# We can reuse the inserted values to avoid redundacy if the values are same.
print("{msg} is fun. {msg} is easy".format(msg='Python 3'))

# Formatting string using f-string
'''
New string formatting mechanism known as Literal String Interpolation or more commonly as F-strings.
The idea behind f-strings is to make string interpolation simpler.

f-strings provide a faster, more readable, more concise, and less error prone way of formatting strings in Python.
The f-strings have the f prefix and use {} brackets to evaluate values.
'''
# format string using f-string
print(f'Welcome to {text_msg1} session.')
print(f"{text_msg3} This is a {text_msg1} session for {text_msg2}.")