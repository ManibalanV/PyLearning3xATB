def print_argument(*args): # *args(very similar to list) contains multiple number of arguments
    for i in args:
        print(i, end=" ")


print_argument("Manibalan", "Suriya", "Dhanvin""\n")


# *args -> List

a = ["Manibalan", "Suriya", "Dhanvin"]
for i in a:
    print(i, end=" ")