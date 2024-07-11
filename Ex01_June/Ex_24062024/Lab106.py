# map
# pick 1 item and apply the function
# give the same number of elements

numbers = [1,2,3,4,5,6,7,8,9,10]

def double_me(num):
    return num*2

# double_me_lambda = lambda n: n*2

new_list_double = map(lambda n: n*2, numbers)
print(list(new_list_double))

new_list_double = map(double_me, numbers)
print(list(new_list_double))

# Filters
# Pick item if true keep it, false, remove it
# it can give less number of items as compared to actual
# list

def even_giver(num):
    return num%2 == 0

new_filtered_list = list(filter(even_giver, numbers))
print(new_filtered_list)

new_filtered_list = list(filter(lambda x: x%2 == 0, numbers))
print(new_filtered_list)
print(list(filter(lambda x: x%2 == 0, numbers)))