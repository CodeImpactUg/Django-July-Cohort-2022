# Python Module example


def add(a, b):
    """This program adds two
    numbers and return the result"""

    result = a + b
    return result


def mult(a, b):
    """This program multiplies two
    numbers and return the result"""

    result = a * b
    return result


def div(a, b):
    """This program divides two
    numbers and return the result"""

    result = a / b
    return result


print("Every thing here is always executed")


if __name__ == "__main__":
    print("Only code in this block will be executed")
    a = 10
    b = 34
    print(f"The sum of {a} and {b} = {add(a, b)}")
    print(f"The name of this module is {__name__}")
