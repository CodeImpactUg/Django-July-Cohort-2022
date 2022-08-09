"""Chunky Monkey
Write a function that splits an array (first argument) into groups the length of size (second argument) and returns them as a two-dimensional array.
"""


def chunkArrayInGroups(arr, size):
    lst = arr[:]
    two_dim_lst = []

    while lst:
        two_dim_lst.append(lst[:size])
        del lst[:size]
    return two_dim_lst


if __name__ == "__main__":
    print(chunkArrayInGroups(["a", "b", "c", "d"], 2))
