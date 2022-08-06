"""Slice and Splice
You are given two arrays and an index.

Copy each element of the first array into the second array, in order.

Begin inserting elements at index n of the second array.

Return the resulting array. The input arrays should remain the same after the function runs.
"""


def frankenSplice(arr1, arr2, n):
    arr1_slice = arr1[:]
    arr2_slice = arr2[:]
    flat_list = []

    arr2_slice.insert(n, arr1_slice)

    for item in arr2_slice:
        if isinstance(item, list):
            for it in item:
                flat_list.append(it)
        else:
            flat_list.append(item)
    return flat_list


if __name__ == "__main__":
    print(frankenSplice([1, 2, 3], [4, 5, 6], 1))
