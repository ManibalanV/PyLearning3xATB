# Unpacking of tuple
a, b, c = (12, 34, 56)
t = (12, 34, 56)
#t.append() # 'tuple' are immutable in nature / 'tuple' object has no attribute 'append'

#new_t = t + (4)  # TypeError: can only concatenate tuple (not "int") to tuple
new_t = t + (4,) # comma need to use after the values entered in the tuple
print(new_t)

my_list = list(t)
print(my_list)
my_list.append(5)
new_t2 = tuple(my_list)

print(new_t2)

# SET

