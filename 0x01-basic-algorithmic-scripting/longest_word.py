"""
Find the Longest Word in a String
Return the length of the longest word in the provided sentence.

Your response should be a number.
"""


def findLongestWordLength(st):
    max_word_length = len(st[0])
    for word in st.split():
        if len(word) > max_word_length:
            max_word_length = len(word)
    return max_word_length


if __name__ == "__main__":
    print(findLongestWordLength("The quick brown fox jumped over the lazy dog"))
