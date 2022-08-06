"""Boo who

Check if a value is classified as a boolean primitive. Return True or False.

Boolean primitives are True and False.
"""


def booWho(value):
    if not isinstance(value, bool):
        return False
    return True


if __name__ == "__main__":
    print(booWho(None))
