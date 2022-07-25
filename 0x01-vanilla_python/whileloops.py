## Python while Loop
## The while loop in Python is used to iterate over a
# block of code as long as the test expression (condition) is true.

# Syntax of while Loop in Python
"""
while test_expression:
    Body of while
"""

# Program to add natural
# numbers up to
# sum = 1+2+3+...+n

# To take input from the user,
# n = int(input("Enter n: "))

n = int(input("Enter n: "))
total = 0
i = 1  # counter variable

while i <= n:
    total += i  # total = total + i
    i += 1  # update counter by 1

# print the sum
print(f"The sum is {total}")
