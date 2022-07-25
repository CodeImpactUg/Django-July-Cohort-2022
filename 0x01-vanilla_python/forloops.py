# Write program to print natural numbers for 1 to 10

"""This repetitive code
print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)
"""

# DRY --- Don't Repeat Yourself

## Python for Loop
## The for loop in Python is used to iterate over a sequence (list, tuple, string) 
# or other iterable objects. Iterating over a sequence is called traversal.

## Syntax of for Loop
'''
for val in sequence:
    loop body
'''

# Program to find the sum of all numbers stored in a list

# List of numbers
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

# variable to store the sum
total = 0

# iterate over the list
for val in numbers:
    total += val  # sum = sum + val

print(f"The sum is {total}")

# print(f"The sum is {sum(numbers)}")

# The range() function
# We can generate a sequence of numbers using range() function. 
# range(10) will generate numbers from 0 to 9 (10 numbers).
# We can also define the start, stop and step size as 
# range(start, stop,step_size). step_size defaults to 1 if not provided.
print(range(10))
print(list(range(10)))
print(list(range(2, 8)))
print(list(range(2, 20, 3)))

# Write program to display natural numbers from 1 to 100 inclusive
for i in range(1, 101):
    print(i, end=" ")
print()

## Write program to display evens numbers from 0 to 100 inclusive
for num in range(0, 101, 2):
    print(num, end=" ")
print()

# num_list = []
# for num in range(0, 101, 2):
#     num_list.append(num)
# print(num_list)

### Exercise: Write program to print odd numbers from 1 to a given number
# by the user


