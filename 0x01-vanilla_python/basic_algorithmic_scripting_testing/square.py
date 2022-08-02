"""Suppose you have Square class that has a property called length and a method area() that returns the area of the square. 
"""


class Square:
    def __init__(self, length) -> None:
        # if type(length) not in [int, float]:
        #     raise TypeError('Length must be an integer or float')
        if not isinstance(length, (int, float)):
            raise TypeError("Length must be an integer or float")
        if length <= 0:
            raise ValueError("Length must not be negative or zero")
        self.length = length

    def area(self):
        return self.length * self.length
