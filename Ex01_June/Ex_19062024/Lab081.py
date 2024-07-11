my_list = [1, 2, "Mani", 3.14]
my_list.sort() # TypeError: '<' not supported between instances of 'str' and 'int'
print(my_list)


squares = [1, 4, 9, 16, 25]

if not squares: # not always work with boolean.. dont use with list or something.. / if not True:
    print("Not empty")
else:
    print("Empty")

if not True:
    print("Not empty")
else:
    print("Empty")



