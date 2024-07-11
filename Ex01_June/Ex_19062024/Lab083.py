# Tuple - Collection of Items / similar to list

my_list = [1,2,3,4,5]
print(id(my_list))
my_list[0] = 21
print(my_list)
print(id(my_list))


my_tuple = (1,2,3,4,5)
my_tuple[0] = 12 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)
