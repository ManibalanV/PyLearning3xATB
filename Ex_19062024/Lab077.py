def sum_of_three_numbers(a,b,c):
    return a+b+c

o = sum_of_three_numbers(3,3,5)
print(o)

o_f = lambda a,b,c: a+b+c
print(o_f)
print(o_f(2,2,6))