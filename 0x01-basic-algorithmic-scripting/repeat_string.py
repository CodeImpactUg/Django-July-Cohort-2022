"""Repeat a String Repeat a String

Repeat a given string str (first argument) for num times (second argument). Return an empty string if num is not a positive number. 
"""


def repeatStringNumTimes(st, num):
    if len(st) <= 0:
        return ""
    return st * num


if __name__ == "__main__":
    print(repeatStringNumTimes("abc", 3))
