# Python Functions

## In Python, a function is a group of related statements that performs a specific task.

# Functions help break our program into smaller and modular chunks. As our program grows larger and larger, functions make it more organized and manageable.

# Furthermore, it avoids repetition and makes the code reusable.

## Syntax of Function

'''
def function_name(parameters):
	"""docstring"""
	statement(s)
    return 
'''

# Example of a function


def greet(name):
    """This function greets to the person passed in as a parameter

    Args:
        name (str): user's short name
    """
    print(f"Hello {name}!")


greet("Patrick")  # function call

# Docstrings

# The first string after the function header is called the docstring and is short for documentation string. It is briefly used to explain what a function does.

# Although optional, documentation is a good programming practice. Unless you can remember what you had for dinner last week, always document your code.

# In the above example, we have a docstring immediately below the function header. We generally use triple quotes so that docstring can extend up to multiple lines. This string is available to us as the __doc__ attribute of the function.

print(greet.__doc__)


## The return statement
# The return statement is used to exit a function and go back to the place from where it was called.

"""
Syntax of return
return [expression_list]
"""

"""Write function returns the absolute value of the entered number"""


def absolute_value(num):
    """This function returns the absolute value of the entered number

    Args:
        num (int): number to get its absolute value
    """

    if num >= 0:
        return num
    else:
        return -num  # -1 * num


print(absolute_value(5))
print(absolute_value(-5))

num = -200
abs_val = absolute_value(num)
print(f"The absolute value of {num} = {abs_val}")


## Scope and Lifetime of variables
# Scope of a variable is the portion of a program where the variable is recognized. Parameters and variables defined inside a function are not visible from outside the function. Hence, they have a local scope.

# The lifetime of a variable is the period throughout which the variable exists in the memory. The lifetime of variables inside a function is as long as the function executes.

# They are destroyed once we return from the function. Hence, a function does not remember the value of a variable from its previous calls.


def my_func():
    x = 10
    print("Value inside function:", x)


x = 20
my_func()
print("Value outside function:", x)

# Types of Functions
# Basically, we can divide functions into the following two types:

# Built-in functions - Functions that are built into Python.
# User-defined functions - Functions defined by the users themselves.
