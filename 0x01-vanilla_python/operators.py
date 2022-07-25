# Python Operators

## Arithmetic operators
## Arithmetic operators are used to perform mathematical
# operations like addition, subtraction, multiplication, etc.

x = 15
y = 4
print(f"x = {x}, y = {y}")

# Output: x + y = 19
print("x + y =", x + y)

# Output: x - y = 11
print("x - y =", x - y)

# Output: x * y = 60
print("x * y =", x * y)

# Output: x / y = 3.75
print("x / y =", x / y)

# Output: x // y = 3
print("x // y =", x // y)

# Output: x % y = 3
print("x % y =", x % y)

# Output: x ** y = 50625
print("x ** y =", x ** y)
print("\n")

## Comparison operators
## Comparison operators are used to compare values.
# It returns either True or False according to the condition.
x = 10
y = 12

print(f"x = {x}, y = {y}")

# Output: x > y is False
print("x > y is", x > y)

# Output: x < y is True
print("x < y is", x < y)

# Output: x == y is False
print("x == y is", x == y)

# Output: x != y is True
print("x != y is", x != y)

# Output: x >= y is False
print("x >= y is", x >= y)

# Output: x <= y is True
print("x <= y is", x <= y)

print("\n")

# Logical Operators
## Logical operators are the `and`, `or`, `not` operators.
x = True
y = False

print("x and y is", x and y)

print("x or y is", x or y)

print("not x is", not x)

## Assignment operators
# Assignment operators are used in Python to assign values to variables.

# a = 5 is a simple assignment operator that assigns the value 5 on the right to the variable a on the left.

# There are various compound operators in Python like a += 5 that adds to the variable and later assigns the same. It is equivalent to a = a + 5.

a = 10
a = a + 5
print(a)

# a = a + 5 is equivalent a += 5
a += 5

# More examples
# Operator	#Example	Equivalent to
# =	x        = 5	    x = 5
# +=	    x += 5	    x = x + 5
# -=	    x -= 5	    x = x - 5
# *=	    x *= 5	    x = x * 5
# /=	    x /= 5	    x = x / 5
# %=        x %= 5      x = x % 5

## Identity operators
## is and is not are the identity operators in Python.
# They are used to check if two values (or variables) are
# located on the same part of the memory. Two variables
# that are equal does not imply that they are identical.

## Membership operators
## in and not in are the membership operators in Python.
# They are used to test whether a value or variable is
# found in a sequence (string, list, tuple, set and dictionary)

club = "Arsenal"
print("A" in club)
print("g" in club)
print("g" not in club)
