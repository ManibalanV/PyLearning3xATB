# Strings
# In built Functions -
# Function -> Repeat a task - You can use a function.
# print(), input(), type(), format(), max(), min(), id(), sum(), avg()

# Strings

name = "Mani"
print(name)
print(type(name))
print(id(name)) #Memory address: where it's stored
print(len(name)) #length of a string (length always starts from 1)

name = name.upper()
print(name)
name = name.lower()
print(name)
print(len(name))
a = name.count("A")
b = name.count("a")
print(a)
print(b)

name = "Mani"
# M a n i
# 0 1 2 3
print(name[1])

# Python - Immutable - that can't be changed
name[0] = "K" #TypeError: 'str' object does not support item assignment





