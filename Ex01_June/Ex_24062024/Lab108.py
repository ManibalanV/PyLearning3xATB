# Recursion
# Recursion is a programming technique where a function calls itself in order to solve a problem

# Key concepts
# 1. Base case
# 2. Recursive case

def factorial(n):
    # Base case:
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(9))