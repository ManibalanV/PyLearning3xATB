# Function scope

def my_function():
    a = 123 # Local variable
    print("Hello")
    print(a)

my_function()
print(a) # NameError: name 'a' is not defined