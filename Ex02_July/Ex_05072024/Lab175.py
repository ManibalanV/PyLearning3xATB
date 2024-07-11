# OS Module
# OS Module use to interact with Operating system
# get working dir, change dir, file exist, fileName, size file, Envir..

import os
import math
print(os.name) # e.g.. posix for unix/Linux - Mac
# nt - for Windows

print(os.getcwd())
print(math.pi)
print(os.chdir("C:/Users/manib/PycharmProjects/PyLearning3xATB/Ex02_July/Ex_03072024"))
print(os.getcwd())

print(os.chdir("C:/Users/manib/PycharmProjects/PyLearning3xATB/Ex02_July/Ex_05072024"))
print(os.getcwd())
# print(os.mkdir("mani"))
print(os.listdir())

#Read file

size = os.path.getsize("testdata.txt")
print(size)

if size != 0:
    print("File exist")
else:
    print("File don't exist")


# Get file modification time
mtime = os.path.getmtime('testdata.txt')
print(mtime)


