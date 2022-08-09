""" Create program to count the occurance of each letter in given string

text = '''Various built-in functions that work with sequence work with strings as well.

Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.

Similarly, len() returns the length (number of characters) of the string.
'''

Go a head and represent the counter as histogram/bar of stars for each character
"""
from pprint import pprint


def char_counter(text):
    counter_dict = {}
    text = text.lower()
    text = text.replace("\n", "")
    text = text.replace(" ", "")
    text = text.replace("()", "")
    text = text.replace("(", "")
    text = text.replace(")", "")
    text = text.replace(".", "")
    text = text.replace("-", "")
    text = text.replace(",", "")
    for char in text:
        counter_dict[char] = counter_dict.get(char, 0) + 1  # {"a": 3, "b": 4}

    return counter_dict


if __name__ == "__main__":
    text = """Various built-in functions that work with sequence work with strings as well.

            Some of the commonly used ones are enumerate() and len(). The enumerate() function returns an enumerate object. It contains the index and value of all the items in the string as pairs. This can be useful for iteration.

            Similarly, len() returns the length (number of characters) of the string.
        """
    character_counter = char_counter(text)
    pprint(character_counter)

    print()
    for k, v in character_counter.items():
        print(f"{k}: {'*' * v}")
