# import statement example
# to import standard module math
import math
import random

# import module by renaming it
import math as m  # import with alias

# import only pi and e from math module
from math import pi, e

import example
from example import div, add, mult

a = 100
b = 200

print(f"The product of {a} and {b} = {example.mult(a, b)}")
print(f"The quotient of {a} and {b} = {div(a, b)}")
print(f"The total of {a} and {b} = {add(a, b)}")
print(f"The product of {a} and {b} = {mult(a, b)}")

print("The value of pi is", math.pi)
print("The value of pi is", m.pi)
print("The value of pi is", pi)
print("The value of e is", math.e)
print("The value of e is", m.e)
print("The value of e is", e)


# Writing a program the generates random number from 1 to 10
# Pseudo random numbers
# random.seed(100)  # used to for reproducibility
print(f"Random number between 1 and 10 = {random.randint(1, 10)}")
