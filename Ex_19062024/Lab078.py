# lambda arguments: expression

def find_odd_even(num):
    if num % 2 == 0:
        print("Even")
    else:
        print("Odd")

find_odd_even(6)



odd_even = lambda num: "Even" if num%2 == 0 else "Odd"
print(odd_even(102))