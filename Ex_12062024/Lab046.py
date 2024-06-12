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
