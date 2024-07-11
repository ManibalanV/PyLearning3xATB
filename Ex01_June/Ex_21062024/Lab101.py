mani_details = \
    {"name": "Manibalan",
     "90": 34.34,
     "isMale": True,
     "Address": "KA"
     }

print(mani_details)
print(mani_details.get("Address"))
print(mani_details["Address"])
print(mani_details.values())
print(mani_details.keys())

my_dict = {'a': 1, 'b': 2, 'c': 3, 'a': 93} # can't have duplicate keys
print(my_dict)
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))

for i in list(my_dict.keys()):
    print(i)

for k, v in my_dict.items():
    print(k,v)