## Python break and continue

## Python break statement
## The break statement terminates the loop containing it. 
# Control of the program flows to the statement immediately 
# after the body of the loop.

# If the break statement is inside a nested loop (loop inside another loop), 
# the break statement will terminate the innermost loop.

# Syntax of the break
'''
break
'''

# Example
'''
for var in sequence:
    if condition:
        break
    codes inside the forloop
codes outside the forloop
'''

# Initialize string
sport = "footbAll"
## print the characters in sport variable
# but stop when the char is of uppercase
for char in sport:
    if char.isupper():
        break
    print(char, end=" ")
print("\nEnd of for loop")

## Python continue statement
# The continue statement is used to skip the 
# rest of the code inside a loop for the current iteration only. 
# Loop does not terminate but continues on with the next iteration.

# Syntax of continue
'''
continue
'''

'''
Write a proogram that outputs numbers from 0 to 50 inclusive
but excluding even numbers (In short just print out odd numbers)
'''

for num in range(0, 51):
    if num % 2 == 0:
        continue
    print(num, end=" ")
print()

## Exercise: Write a program to print numbers from 0 to n
# Where n is user input and excluding all that multiples
# of 3

## Python pass statement
## In Python programming, the pass statement is a null statement. 
# The difference between a comment and a pass statement in 
# Python is that while the interpreter ignores a comment entirely, pass is not ignored.

# Syntax of pass
'''
pass
'''

# Example: pass Statement
'''pass is just a placeholder for
functionality to be added later.'''
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

##  We can do the same thing in an empty function or class as well.
def function(args):
    pass

class Example:
    pass

# Follow this 
# link https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/
# For practice questions
