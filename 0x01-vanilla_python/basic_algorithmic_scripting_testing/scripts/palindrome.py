"""
Given a string, write a python function to check if it is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as string. For example, “radar” is a palindrome, but “radix” is not a palindrome.

Examples: 
Input : malayalam
Output : Yes

Input : geeks
Output : No

"""


def is_palindrome(st):
    rev = "".join(list(reversed(st)))

    if rev == st:
        return True
    return False


def is_palindrome2(st):
    rev = st[::-1]

    if rev == st:
        return True
    return False


if __name__ == "__main__":
    st = "malayalam"
    ans = is_palindrome(st)

    if ans:
        print(f"is_palindrome({st}) is Yes")
    else:
        print(f"is_palindrome({st}) is No")

    st = "geeks"
    ans = is_palindrome(st)

    if ans:
        print(f"is_palindrome({st}) is Yes")
    else:
        print(f"is_palindrome({st}) is No")
