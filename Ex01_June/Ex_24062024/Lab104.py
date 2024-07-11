# Filter in Python
# filter() builtin function in python
# allows you to filter the elements in the list, tuple, set

numbers = [1,2,3,4,5,6,7,8,9,10]
# Filter on the above -> even ->
# new_list_Even = [2,4,6,8,10]

def is_even(num):
    return num % 2 == 0

def is_greater_five(num):
    return num > 5


new_numbers_even = filter(is_even, numbers)
print(list(new_numbers_even))

new_numbers_five = filter(is_greater_five, numbers)
print(list(new_numbers_five))


