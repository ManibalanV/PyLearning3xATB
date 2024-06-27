# Multiple Condition

# Problem find the max between 3 Numbers:
# num1, num2, num3

# num1 > num2 and num1 > num3: num1
# num2 > num1 and num2 > num3: num2
# num3

num1 = int(input("Enter the number1: \n"))
num2 = int(input("Enter the number2: \n"))
num3 = int(input("Enter the number3: \n"))

if num1 > num2 and num1 > num3:
    print(num1)
elif num2 > num1 and num2 > num3:
    print(num2)
else:
    print(num3)



