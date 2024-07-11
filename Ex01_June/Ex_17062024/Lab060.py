def f1(a, b, c):
    return a + b + c
    print("Hello") # This code will be never executed

print("end")

result = f1(12,12,12)
print(result)

print(f1(11,12,13)) # Instead of storing the value in the variable we can directly print the result