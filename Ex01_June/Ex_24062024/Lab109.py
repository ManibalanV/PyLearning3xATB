# Leetcode : sum of digits

def sum_of_digit(n):
    # Base case:
    if n < 10:
        return n
    else:
        return n % 10 + sum_of_digit(n//10)


print(sum_of_digit(1234))