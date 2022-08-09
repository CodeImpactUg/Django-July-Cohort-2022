"""Title Case a Sentence

Return the provided string with the first letter of each word capitalized. Make sure the rest of the word is in lower case.

For the purpose of this exercise, you should also capitalize connecting words like the and of.
"""


def titleCase(st):
    title_str = ""
    for word in st.split():
        title_str += f" {word.capitalize()}"
    return title_str.strip()


if __name__ == "__main__":
    print(titleCase("I'm a little tea pot"))
