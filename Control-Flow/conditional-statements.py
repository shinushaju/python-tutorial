# Python Conditional Flow Control

'''
Conditional types in Python are:
 1. if
 2. if else
 3. if elif else
 
These are conditional statements and are used for decisions and branching in a program.

If statements are control flow statements that run a particular code only when a certain condition is met.

The if-else statement evaluates the condition and will execute the body of if if the test condition is True, but if the condition is False,
then the body of else is executed. The if block can have only one else block.

Refer: https://www.scaler.com/topics/python/control-flow-statements-in-python/#conditional
'''

'''
1. Read years of experience and expected salary as an integer input from the user and display the inputs.
2. Use if statement to check the years of experience is 0 years. if yes, then print 'Entry Level'. (Hint: use if statement)
3. If the above condition is not met print 'Experienced Professional' as the output. (Hint: use if-else statement)
4. Modify the code in such a way that it shows an error message for input values less than 0.
   display an error message 'Years of experience must be greater than or equal to zero.' for other inputs. (Hint: use if-elif-else statement)
5. Modify the code in such a way that, do the following:
    a) display 'Associate Level Professional' for YOE > 0, but <= 3
    b) display 'Intermediate Level Professional' for YOE > 3, but <= 10
    c) display 'Senior-Level Professional' for YOE > 10, but <=25
    d) display a message 'Years of experience must be less than or equal to 25.' if, YOE > 25.
6. Modify the code to display average salary in the current market along with experience level.
7. Modify the current code to check whether the expected salary exceeds the average market salary. if yes, print "Expected salary exceeds market limit". (Hint: use nested if statements)
8. Update code to display the message "Expected salary is within the market limit", if expected salary is <= average market salary.
''' 

years_of_experience = int(input("Years of Experience: "))
expected_salary = int(input("Expected Salary (LPA): "))
print(f"Years of Experience is {years_of_experience}")
print(f"Expected salary in LPA is {expected_salary}")

if years_of_experience < 0:
    print("Years of experience must be greater than or equal to zero.")
elif years_of_experience == 0:
    print("Entry Level")
    print("Average Market Salary: 4LPA")
    if expected_salary > 4:
        print("Expected salary exceeds market limit")
    else:
        print("Expected salary is within the market limit")
elif years_of_experience > 0 and years_of_experience <= 3:
    print("Associate Level Professional")
    print("Average Market Salary: 6LPA")
    if expected_salary > 6:
        print("Expected salary exceeds market limit")
    else:
        print("Expected salary is within the market limit")
elif years_of_experience > 3 and years_of_experience <= 10:
    print("Intermediate Level Professional")
    print("Average Market Salary: 24LPA")
    if expected_salary > 24:
        print("Expected salary exceeds market limit")
    else:
        print("Expected salary is within the market limit")
elif years_of_experience > 10 and years_of_experience <= 25:
    print("Senior-Level Professional")
    print("Average Market Salary: 48LPA")
    if expected_salary > 48:
        print("Expected salary exceeds market limit")
    else:
        print("Expected salary is within the market limit")
else:
    print("Years of experience must be less than or equal to 25.")


# print("Entry Level") if years_of_experience == 0 else print("Experienced Professional")
    
# if years_of_experience == 0:
#     print("Entry Level")

# if years_of_experience == 0:
#     print("Entry Level")
# else:
#     print("Experienced Professional")

# if years_of_experience < 0:
#     print("Years of experience must be greater than or equal to zero.")
# elif years_of_experience == 0:
#     print("Entry Level")
# else:
#     print("Experienced Professional")

# if years_of_experience < 0:
#     print("Years of experience must be greater than or equal to zero.")
# elif years_of_experience == 0:
#     print("Entry Level")
# elif years_of_experience > 0 and years_of_experience <= 3:
#     print("Associate Level Professional")
# elif years_of_experience > 3 and years_of_experience <= 10:
#     print("Intermediate Level Professional")
# elif years_of_experience > 10 and years_of_experience <= 25:
#     print("Senior-Level Professional")
# else:
#     print("Years of experience must be less than or equal to 25.")

# if years_of_experience < 0:
#     print("Years of experience must be greater than or equal to zero.")
# elif years_of_experience == 0:
#     print("Entry Level")
#     print("Average Market Salary: 4LPA")
# elif years_of_experience > 0 and years_of_experience <= 3:
#     print("Associate Level Professional")
#     print("Average Market Salary: 6LPA")
# elif years_of_experience > 3 and years_of_experience <= 10:
#     print("Intermediate Level Professional")
#     print("Average Market Salary: 24LPA")
# elif years_of_experience > 10 and years_of_experience <= 25:
#     print("Senior-Level Professional")
#     print("Average Market Salary: 48LPA")
# else:
#     print("Years of experience must be less than or equal to 25.")

# if years_of_experience < 0:
#     print("Years of experience must be greater than or equal to zero.")
# elif years_of_experience == 0:
#     print("Entry Level")
#     print("Average Market Salary: 4LPA")
#     if expected_salary > 4:
#         print("Expected salary exceeds market limit")
# elif years_of_experience > 0 and years_of_experience <= 3:
#     print("Associate Level Professional")
#     print("Average Market Salary: 6LPA")
#     if expected_salary > 6:
#         print("Expected salary exceeds market limit")
# elif years_of_experience > 3 and years_of_experience <= 10:
#     print("Intermediate Level Professional")
#     print("Average Market Salary: 24LPA")
#     if expected_salary > 24:
#         print("Expected salary exceeds market limit")
# elif years_of_experience > 10 and years_of_experience <= 25:
#     print("Senior-Level Professional")
#     print("Average Market Salary: 48LPA")
#     if expected_salary > 48:
#         print("Expected salary exceeds market limit")
# else:
#     print("Years of experience must be less than or equal to 25.")