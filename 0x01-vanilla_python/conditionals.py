# Python if...else Statement
# if…elif…else statement

# Python if Statement Syntax
"""
if test expression:
    statements(s)
"""

x = 3
if x >= 10:
    x += 5
    print(x)

# Python interprets non-zero values as True. None and 0 are interpreted as False.

# If the number is positive, we print an appropriate message
num = 3
if num > 0:
    print(num, "is a positive number.")
print("This is always printed.")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("This is also always printed.")

## Python if...else Statement
# Syntax of if...else
"""
if test expression:
    Body of if
else:
    Body of else
"""

# Program checks if the number is positive or negative
# And displays an appropriate message

num = -10

if num >= 0:
    print("Positive or Zero")
else:
    print("Negative number")


## Python if...elif...else Statement
# Syntax of if...elif...else
# The elif is short for else if. It allows us to check for multiple expressions.
"""
if test expression:
    Body of if
elif test expression:
    Body of elif
elif test expression:
    Body of elif
else: 
    Body of else
"""

'''In this program, 
we check if the number is positive or
negative or zero and 
display an appropriate message'''

num = 0

if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
    
## Python Nested if statements
# We can have a if...elif...else statement inside another 
# if...elif...else statement. This is called nesting in computer programming.

'''In this program, we input a number
check if the number is positive or
negative or zero and display
an appropriate message
This time we use nested if statement'''

num = int(input("Enter number: "))

if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")