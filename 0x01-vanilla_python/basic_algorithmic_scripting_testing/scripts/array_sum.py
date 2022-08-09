"""
Given an array of integers, find the sum of its elements.

Examples:

Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6

Input : arr[] = {15, 12, 13, 10}
Output : 50

Input: arr[] = []
Output : 0
"""


def list_sum(arr):
    total_sum = 0

    for num in arr:
        total_sum += num  # total = total + num

    return total_sum


def list_sum2(arr):
    return sum(arr)


if __name__ == "__main__":
    list1 = [1, 2, 3]
    print(f"The sum of list1 elements = {list_sum(list1)}")

    list2 = [15, 12, 13, 10]
    print(f"The sum of list1 elements = {list_sum(list2)}")

    list3 = []
    print(f"The sum of list1 elements = {list_sum(list3)}")

    list4 = [15, 12, 13, 10]
    print(f"The sum of list1 elements = {list_sum2(list4)}")

    list5 = []
    print(f"The sum of list1 elements = {list_sum2(list5)}")
