my_list = [1,2,3,4]

def double_item(num):
    return num * 3

double_list = list(map(double_item, my_list))
print(double_list)
