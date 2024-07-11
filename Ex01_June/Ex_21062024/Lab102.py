my_dict = {'b': 2, 'w': 1, 'c': 45, 'a': 34}
print(my_dict)

for k, v in my_dict.items():
    print(k,v)

from collections import OrderedDict
od = OrderedDict()
od['a'] = 45
od['c'] = 78
od['b'] = 97
od['d'] = 31
print(od)

# Dict: It will not keep the Order of insertion
# OrderedDict: It will keep the order of insertion