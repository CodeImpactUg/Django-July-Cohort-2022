# Python Function Arguments

## Arguments
# In the user-defined function topic, we learned about defining a function and calling it. Otherwise, the function call will result in an error. Here is an example.


def greet(name, msg):  # parameters and arguments
    """This function greets to
    the person with the provided message"""
    print(f"Hello, {name} {msg}")

greet("Monica", "Good morning!")
greet("Good morning!", "Monica")
# greet("Monica") this give an error
# greet()  this also results into an error

## Variable Function Arguments
# Up until now, functions had a fixed number of arguments. In Python, there are other ways to define a function that can take variable number of arguments.

# Three different forms of this type are described below.

## Python Default Arguments(Keyword arguments)
# Function arguments can have default values in Python.

# We can provide a default value to an argument by using the assignment operator (=). Here is an example.

def greet(name, msg="Good morning!"):
    """
    This function greets to
    the person with the
    provided message.

    If the message is not provided,
    it defaults to "Good
    morning!"
    """

    print(f"Hello {name} {msg}")


greet("Kate")
greet("Bruce", "How do you do?")

## Python Keyword Arguments
# 2 keyword arguments
greet(name = "Bruce", msg = "How do you do?")

# 2 keyword arguments (out of order)
greet(msg = "How do you do?", name = "Bruce") 

# 1 positional, 1 keyword argument
greet("Bruce", msg = "How do you do?") 

# greet(msg = "How do you do?", "Bruce")  this also will result into a syntax error

# Python Arbitrary Arguments
# In the function definition, we use an asterisk (*) 
# before the parameter name to denote this kind of argument

def greet(*args, **kwargs):  # (*name, **msg)
    """
    This function greets to
    the person with the
    provided message.
    """
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")
    print()

greet("Kate")
greet("Bruce", "How do you do?")
greet(name = "Bruce", msg = "How do you do?")
greet("Bruce", msg = "How do you do?")


def greet(*names):  # *names === *args
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


greet("Monica", "Luke", "Steve", "John", "Patrick", "James", "Caesar", "Aron")

## Read about Global, Local and Nonlocal variables
## Python Global Keyword