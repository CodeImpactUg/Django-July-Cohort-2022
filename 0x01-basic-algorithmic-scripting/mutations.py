"""Mutations

Return True if the string in the first element of the array contains all of the letters of the string in the second element of the array.

For example, ["hello", "Hello"], should return True because all of the letters in the second string are present in the first, ignoring case.

The arguments ["hello", "hey"] should return False because the string hello does not contain a y.

Lastly, ["Alien", "line"], should return True because all of the letters in line are present in Alien.
"""


def mutation(arr):
    for ch in arr[1].lower():
        if ch not in arr[0].lower():
            return False
    return True


if __name__ == "__main__":
    print(mutation(["hello", "hey"]))
