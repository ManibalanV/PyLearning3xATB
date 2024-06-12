"""
Task #1
Explain the difference between the = operator and the == operator in Python.
What does the ** operator do in Python, and how is it used?
What does the ^ operator do in Python, and in what context is it commonly used?
"""
# "=" operator is used for assign the value. Ex: a = 12
# "==" operator is used for condition checking. Ex: if a == 12:

# "**" operator is used as exponential. Ex: 2**3 ; can be written as 2*2*2 which is equal to 8

# "^" operator is commonly called as Bitwise XOR. It's commonly used for XOR operation in electronics.
# Below operation it performs:
# Input1    Input2  Output
# False     False   False
# True      False   True
# False     True    True
# True      True    False

#-------------------------------------------------------------------------
"""
Task #2
Develop a Python script that calculates the square and cube of a given number. num = 2 sq - 4, c = 8
Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
Push the code to Github.com
"""
#Program1:

num = 2
#num = int(input("Enter the number: "))
print(f'Square of the given number is {num**2}, and cube of the number is {num**3}')

#Program2:

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))

if first_number == second_number:
    print("First number is equal to second number ")
elif first_number < second_number:
    print("First number is less than second number ")
else:
    print("First number is greater than second number ")






