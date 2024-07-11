numbers = [1, 2, 3]


# Collection of items

def do_something(mani_list):
    mani_list.append(4)
    mani_list[0] = 100
    return mani_list

numbers.append(10)
l = do_something(numbers)
print(l)