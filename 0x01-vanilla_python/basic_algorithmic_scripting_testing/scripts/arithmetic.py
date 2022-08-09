"""Create a program that adds two numbers.
"""


def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError(f"{a} and {b}  should either be an integer or float")

    return a + b


if __name__ == "__main__":
    num1 = 40
    num2 = 30
    total = add(num1, num2)
    print(f"The sum of {num1} and {num2} = {total}")

    total = add(40, "num2")
    print(f"The sum of {num1} and {num2} = {total}")
