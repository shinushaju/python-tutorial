# Python Statements

'''
Instructions that a Python interpreter can execute are called statements.
A Python script usually contains a sequence of statements.
There are mainly four types of statements in Python:
1. Print statements
2. Assignment statements
3. Conditional statements
4. Looping statements

Refer: https://www.geeksforgeeks.org/statement-indentation-and-comment-in-python/
'''

# assignment statement
variable = 3
print(variable)

'''
Statements in Python can be extended to one or more lines using 
parentheses (), braces {}, square brackets [], continuation character slash (\) and, semi-colon (;).
'''

# multiline statement using parentheses ()
multiline_statement_1 = (1 + 2 + 3 + 
    4 + 5 + 6 + 
    7 + 8 + 9)
print("Multiline statement using parentheses output", multiline_statement_1)

# multiline statement using braces {}
multiline_statement_2 = {1 + 2 + 3 + 
    4 + 5 + 6 + 
    7 + 8 + 9}
print("Multiline statement using braces output", multiline_statement_2)

# multiline statement using square brackets []
multiline_statement_3 = [1 + 2 + 3 + 
    4 + 5 + 6 + 
    7 + 8 + 9]
print("Multiline statement using square brackets", multiline_statement_3)

# multiline statement using continuation character slash \
multiline_statement_4 = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    7 + 8 + 9
print("Multiline statement using continuation character slash output", multiline_statement_4)

# multiline statement using semi-colon ;c
a = 'First Statement\n'; b = 'Middle Statement\n'; c = 'Final Statement'
print("Multiline statement using semi-colon:\n",a,b,c)

