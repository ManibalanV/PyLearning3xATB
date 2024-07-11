# Write a program that calculates and displays the letter
# given numerical score (e.g. A, B, C, D, F)
# input-score - 89
# output - B

A = range(90,101)
B = range(80, 90)
C = range(70, 80)
D = range(60, 70)
F = range(0,60)

score = int(input("Enter your score:\n"))

if score in A:
    print("A grade")
elif score in B:
    print("B grade")
elif score in C:
    print("C grade")
elif score in D:
    print("D grade")
elif score in F:
    print("F grade")
else:
    print("Invalid")
#-------------------------------------------------------


score = int(input("Enter your score:\n"))

if 90 <= score <= 100:
    print("A")
elif 80 <= score <= 89:
    print("B")
elif 70 <= score <= 79:
    print("C")
elif 60 <= score <= 69:
    print("D")
elif 0 <= score <= 59:
    print("F")
else:
    print("Invalid score")
