# Program - Calculate the area of circle
# input - radius // Data type: int or float - float
# output - area // Data type: float

# core logic: area of circle = pi * r * r

import math
radius = float(input("Enter the radius to calculate area: "))

area_of_circle = math.pi * pow(radius, 2)

print(area_of_circle)



