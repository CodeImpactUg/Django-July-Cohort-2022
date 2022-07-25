# Python Input, Output and Import

# Python provides numerous built-in functions that are readily available to us at the Python prompt.

# Some of the functions like input() and print() are widely used for standard input and output operations respectively

## Python Output Using print() function

print('This sentence is output to the screen')

a = 5
print('The value of a is', a)

# The actual syntax of the print() function is:

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
print(1, 2, 3, 4)
print(1, 2, 3, 4, sep='*')
print(1, 2, 3, 4, sep='#', end='&')
print("Hello")
print("End with space", end=" ")
print()


# Output formatting
x = 5
y = 10

# using str.format()
print('The value of x is {} and y is {}'.format(x, y))

name = "Patrick"
age = 26
# print("My name is", name, " and I am ", age, "years old.")
print("My name is {} and I am {} years old.".format(name, age))

# Here, the curly braces {} are used as placeholders. 
# We can specify the order in which they are printed by 
# using numbers (tuple index).

print('I love {0} and {1}'.format('bread','butter'))
print('I love {1} and {0}'.format('bread','butter'))
print("My name is {1} and I am {0} years old.".format(age, name))

# We can even use keyword arguments to format the string.
print('Hello {name}, {greeting}'.format(greeting = 'Goodmorning', name = 'John'))
print("My name is {name} and I am {age} years old.".format(name = name, age = age))

# We can also format strings like the old sprintf() 
# style used in C programming language. 
# We use the % operator to accomplish this.
x = 12.3456789
print('The value of x is %3.3f' %x)

y = 100
print('The value of x is %d' %y)


# Python f-strings
print(f"My name is {name} and I am {age} years old.")


# Python Input
# To allow flexibility, we might want to take the input from the user. 
# In Python, we have the input() function to allow this. The syntax for input() is:
num = input("Enter a number: ")
print(f"The entered is {num}")
print(f"The data type of {num} is {type(num)}")

# Here, we can see that the entered value 10 is a string, not a number. 
# To convert this into a number we can use int() or float() functions.
print(int(num) + 10)
print(float(num) + 10)


# Python Import Statements
# A module is a file containing Python definitions and statements. 
# Python modules have a filename and end with the extension .py.

# Definitions inside a module can be imported to another 
# module or the interactive interpreter in Python. 
# We use the import keyword to do this.

# For example, we can import the math module by typing the following line:
import math
print(math.pi)

# Now all the definitions inside math module are available in our scope. 
# We can also import some specific attributes and functions only, 
# using the from keyword. For example:
from math import pi
print(pi)

# Reuse python_statement from the variables module
# from variables import python_statement
# print(python_statement)
