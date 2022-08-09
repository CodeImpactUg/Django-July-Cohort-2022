# Opening files in python
f = open("test.txt")  # open file in current directory

# open(filepath, mode)
"""
Mode	Description
r	Opens a file for reading. (default)
w	Opens a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
x	Opens a file for exclusive creation. If the file already exists, the operation fails.
a	Opens a file for appending at the end of the file without truncating it. Creates a new file if it does not exist.
t	Opens in text mode. (default)
b	Opens in binary mode.
+	Opens a file for updating (reading and writing)
"""
# Closing Files in Python
# When we are done with performing operations on the file, we need to properly close the file.

# Closing a file will free up the resources that were tied with the file. It is done using the close() method available in Python.

# Python has a garbage collector to clean up unreferenced objects but we must not rely on it to close the file.
f.close()


# Open the file using the with statement (context manager)
with open("test.txt", "r", encoding="utf-8") as f:
    # perform file operations
    pass


# Writing to files in python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("My first file\n")
    f.write("This file\n")
    f.write("contains three lines\n")

# Reading files in python
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f.readlines():
        print(line.strip())  # rstrip and lstrip() # print(line, end="")


# Iterating the file object
with open("test.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())
