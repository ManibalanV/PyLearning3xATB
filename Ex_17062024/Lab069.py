# Triangle Classifier
side1 = float(input("Enter the side1 value: \n"))
side2 = float(input("Enter the side2 value: \n"))
side3 = float(input("Enter the side3 value: \n"))

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")
