"""Falsy Bouncer
Remove all falsy values from an array.

Falsy values in Python are False, None, 0, "".

Hint: Try converting each value to a Boolean.
"""


def bouncer(arr):
    new_arr = []
    for val in arr:
        if int(bool(val)) != 0:  # if not val
            new_arr.append(val)
    return new_arr


if __name__ == "__main__":
    print(bouncer([7, "ate", "", False, 9]))
