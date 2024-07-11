# File Handling
# How to Read a Text, and Write into in using Python Code.

# Function -
# open("file_name", "mode")

# Mode:
# "r" for reading (default)
# "w" for writing (Creates a new file or truncates and existing one).
# "a" for appending.
# "b" for binary mode. Ex. zoom.exe - binary
# "+" for updating (reading and writing

# Read and Write content
# Read a file
# Reading Entire Content: content = file_object.read()
# line = file_object.readline() for a single line
# lines = file_object.readlines() for all lines in a list.
# Close the file

import os
print(os.getcwd())

file = open("TestData.txt", 'r')
content = file.read()
print(content)
file.close()