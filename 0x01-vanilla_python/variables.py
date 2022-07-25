# Python Statements, Identation and Comments

# Assignments
a = 10

# Multi-line statement
a = 1 + 2 + 3 + \
    4 + 5 + 6 + \
    8 + 9 + 10
print(a)

b = (1 + 2 + 3 +
     4 + 5 + 6 +
     7 + 8 + 9)
print(b)

# Lists
fruits = [
    "Mangoes", 
    "Oranges", 
    "Tomatoes", 
    "Ovacodo", 
    "Guavas", 
    "Lemons", 
    "Pineapples", 
    "Apples", 
    "Jack Fruit"
]
print(fruits)

club = "Arsenal"
print(club)

python_statement = """Most of the programming languages like C, 
                   C++, and Java use braces { } to define a block of code. 
                   Python, however, uses indentation.
                """
print(python_statement)

c = 10; d = 56; e = 7;
print(c)
print(d)
print(e)


# Python Identation

# For loop in C
"""
for (int i = 0; i < 10; i++) {
    printf(i);
    if (i == 5) {
        break;
    }
}
"""

# In python

"""
for i in range(1, 11):
    print(i)
    if i == 5:
        break
"""

# Functions
def print_name():
    print("Patrick")

print_name()

# This is a comment
# print out Hello
print("Hello")

# Multi-line comments in python below
"""This is also a
perfect example of
multi-line comments"""

'''
This is also a
perfect example of
multi-line comments
'''

# Docstrings in python
def double(num):
    """Function to double the value"""
    return 2 * num

print(double(10))
print(double(5))
print(double.__doc__)


# Python Variables, Constants and Literals
# A variable is a named location used to store data in the memory.
number = 10
club = "Aston Villa"
number_2 = 10
fruits = [
    "Mangoes", 
    "Oranges", 
    "Tomatoes", 
    "Ovacodo", 
    "Guavas", 
    "Lemons", 
    "Pineapples", 
    "Apples", 
    "Jack Fruit"
]
print(id(number)) # Memory location of value 10
print(id(club)) # Memory location of value 'Aston Villa
print(id(number_2)) # Memory location of value 10
print(id(fruits)) # Memory location pointer to first element in list

# Variables in python are case senstive. Fruits is not the same as fruits

# Variable unpacking
a, b, c = 5, 3.2, "Hello"
print(a)
print(b)
print(c)

# Constansts
# A constant is a type of variable whose value cannot be changed.
PI = 3.14
GRAVITY = 9.8

# Literals
# Literal is a raw data given in a variable or constant.

## Numeric Literals
a = 0b1010 #Binary Literals
b = 100 #Decimal Literal 
c = 0o310 #Octal Literal
d = 0x12c #Hexadecimal Literal

#Float Literal
float_1 = 10.5 
float_2 = 1.5e2


print(a, b, c, d)
print(float_1, float_2)

# String literals
strings = "This is Python"
char = "C"
multiline_str = """This is a multiline string with more than one line code."""
unicode = u"\u00dcnic\u00f6de"
raw_str = r"raw \n string"

print(strings)
print(char)
print(multiline_str)
print(unicode)
print(raw_str)

## Boolean literals
## A Boolean literal can have any of the two values: True or False.
x = (1 == True) # = An assignment operator and == An equality operator
y = (1 == False)
a = True + 4
b = False + 10

print("x is", x)
print("y is", y)
print("a:", a)
print("b:", b)

## Special literals
# food = None

## Literal Collections
# There are four different literal collections List literals, Tuple literals, Dict literals, and Set literals.

fruits = ["apple", "mango", "orange"] #list
numbers = (1, 2, 3) #tuple
alphabets = {'a':'apple', 'b':'ball', 'c':'cat'} #dictionary
vowels = {'a', 'e', 'i' , 'o', 'u'} #set

print(fruits)
print(numbers)
print(alphabets)
print(vowels)


## Python Data types
## Python Numbers
# Data types here are int, float, complex
a = 5
print(a, "is of type", type(a))

b = 2.0
print(b, "is of type", type(b))

c = 1+2j
print(c,  "is of type", type(c))
print(c, "is complex number?", isinstance(1+2j,complex))

# Python String data type
s = "This is a string"
print(s)
s = '''A multiline
string'''
print(s)
print(s, "is of type", type(s))