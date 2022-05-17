# Python Numbers

'''
Number data types store numeric values.
They are immutable data types, which means that changing the value of a number data type results in a newly allocated object.

Different types of Number data types are :
1. int - Whole numbers, including negative numbers but not fractions. It can be of any length.
2. float - Numbers with decimal places. Accurate up to 15 decimal places. Extra zeros present at the number's end are ignored automatically.
           They can be created directly by entering a number with a decimal point, or by using operations such as division on integers.
3. complex - Numbers that consists of the real and imaginary parts.

Refer: https://www.geeksforgeeks.org/python-numbers/
'''

# variables of int type
int_num1 = 10
print(int_num1, "is of type", type(int_num1))

int_num2 = 23989437478839310
print(int_num2, "is of type", type(int_num2))

# variables of float type
float_num1 = 123.23
print(float_num1, "is of type", type(float_num1))

float_num2 = 7/4
print(float_num2, "is of type", type(float_num2))

float_num3 = 3.33848232893326583982
print(float_num3, "is of type", type(float_num3))

# variables of complex type
complex_num = 6+9j
print(complex_num, "is of type", type(complex_num))

# the isinstance() function is used to check if an object belongs to a particular class.
print()
print(int_num1, "is an int number?", isinstance(int_num1, int))
print(float_num1, "is a float number?", isinstance(float_num1, float))
print(complex_num, "is a complex number?", isinstance(complex_num, complex))


'''
In Python, changing the value of a number data type results in a newly allocated object.

The id() function returns the memory address referenced by a variable. It returns a based-10 number. 
We can use the hex() function to convert the base-10 number to hexadecimal.
'''
# print the value of variable int_num1
print("\nCurrent value of variable 'int_num1' is", int_num1)
# print the memory address in based-10 number format of int_num1 variable using 
print("Current memory address of 'int_num1' in based-10 number format is", id(int_num1))
# convert the based-10 number memory address to hexadecimal format using hex()
print("Current memory address of 'int_num1' in hexadecimal format is", hex(id(int_num1)))

# re-assign the value of variable int_num1
int_num1 = 50
# print the new value of variable int_num1
print("\nNew value of variable 'int_num1' is", int_num1)
# print the new memory address in based-10 number format of int_num1 variable using 
print("New memory address of 'int_num1' in based-10 number format is", id(int_num1))
# convert the new based-10 number memory address to hexadecimal format using hex()
print("New memory address of 'int_num1' in hexadecimal format is", hex(id(int_num1)))

int_num1 = 10
# print the new value of variable int_num1
print("\nLatest value of variable 'int_num1' is", int_num1)
# print the new memory address in based-10 number format of int_num1 variable using 
print("Latest memory address of 'int_num1' in based-10 number format is", id(int_num1))
# convert the new based-10 number memory address to hexadecimal format using hex()
print("Latest memory address of 'int_num1' in hexadecimal format is", hex(id(int_num1)))

'''
It seems that the value of the object referenced by the int_num1 variable changes, but it doesn't.
Python creates a new integer object with the new value 50 and reassigns the int_num1 variable so that it references the new object.
The reassignment doesn't change the value of the first integer object. It just reassigns the reference.
'''