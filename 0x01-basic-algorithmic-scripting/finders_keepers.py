"""Finders Keepers

Create a function that looks through an array arr and returns the first element in it that passes a 'truth test'. This means that given an element x, the 'truth test' is passed if func(x) is True. If no element passes the test, return None.
"""


def findElement(arr, func):
    print(list(filter(func, arr)))
    for num in arr:
        if func(num):
            return num
    return None


if __name__ == "__main__":
    print(findElement([1, 2, 3, 4], lambda num: num % 2 == 0))
