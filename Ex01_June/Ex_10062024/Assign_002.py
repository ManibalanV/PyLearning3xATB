"""
Task 2


✅ 1. Leap Year Checker:
Create a program that determines whether a given year is a leap year.



A leap year is divisible by 4, but not by 100 unless it is also divisible by 400.

Use an if-else statement to make this determination.



Input = 2024

Output = Leap year
"""
year = 2024
#year = int(input("Enter the year to check the leap year: "))

if (year % 400 == 0) and (year % 100 == 0):
    print("Leap year")
elif (year % 4 == 0) and (year % 100 != 0):
    print("Leap year")
else:
    print("Not Leap year")
#-----------------------------------------------------------
"""
✅ 2. Triangle Classifier:
Write a program that classifies a triangle based on its side lengths.
Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal).
Use an if-else statement to classify the triangle.

3 Input

side 1, side 2 and side 3

output - Eq, Iso, Scalene -

Eq. = side 1 == side 2 = side 3
"""
side_1 = float(input("Enter the side_1 value to check the triangle shape: "))
side_2 = float(input("Enter the side_2 value to check the triangle shape: "))
side_3 = float(input("Enter the side_3 value to check the triangle shape: "))

if (side_1 == side_2) and (side_2 == side_3):
    print("Equilateral Triangle")
elif (side_1 == side_2) or (side_1 == side_3):
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')

#-----------------------------------------------------------------------



"""
✅ Task - Fibonacci series and Factorial 


# 3. Factorial

# n = 5

# 5! -->5*4*3*2*1 -> 120

# 3! -> 3*2*1 -> 6

# 4! -> 4*3*2*1 -> 24
"""
num = int(input("Enter the number to calculate Factorial number"))
fact = 1
for i in range(1, num+1):
    fact = fact * i
print(fact)

"""


✅ #4. Fibonaci series
# 0,0+1, 0+1+1,

# n = 7 

# 0, 1, 2, 3, 5, 8, 13
"""

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

print("Fibonacci sequence:")
while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1