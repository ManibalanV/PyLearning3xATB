list2 = [1, 2, 3, 4, 5]

print(list2*2) # it's added 2 times list

list = [1, 2, 3, 4, 5]
temp_list = []

for i in list:
    temp = i*2
    temp_list.append(temp)

print(temp_list)

print("----------------------------")

list = [1, 2, 3, 4, 5]
temp_list = []

for i in list:
    temp_list.append(i*2)

print(temp_list)

print("----------------------------")
# Note: If you are appending on the same list then it will be infinite loop.. so create empty list to append/save the data..


# Map()
# 1: Takes Each item from the list
# 2: Execute the function on it
# 3: Return same number of elements (list)


my_list = [1,2,3,4,5]
def double_items(num):
    return num*2

double_items = lambda num: num*2

double_list = list(map(double_items,my_list))

print(double_list)

print("---------------------")


print(list(map(lambda num: num*2, [1,2,3,4,5])))

my_new_list = [1,2,3,4,5]
print(list(map(lambda num: num*2, my_new_list)))


