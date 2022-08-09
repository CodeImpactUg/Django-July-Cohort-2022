""" Write a Python program that takes a text file as input and returns the number of words and lines of a given text file.
Also show number of occurances of each word in the file
"""


def word_line_count(filename):
    word_counter = 0
    lines = 0
    word_dict = {}

    # Reading file
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines += 1
            line = line.strip().lower()

            words = line.split()
            if len(words) > 0:
                for word in words:
                    word_counter += 1
                    word_dict[word.strip()] = word_dict.get(word.strip(), 0) + 1
    return word_counter, lines, word_dict


# print(f"File name: {__name__}")
if __name__ == "__main__":
    words, lines, word_dict = word_line_count("text.txt")
    print(f"Words: {words} Lines: {lines}")
    print(f"Word Occurrances:\n{word_dict}")
