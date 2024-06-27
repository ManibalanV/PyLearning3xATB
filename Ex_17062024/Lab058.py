# Functions
# Block of code - which can executed or reused
# Define
# Call

# Built in Functions -  builtins.py - file (Python 3 setup)
# Which are created by the Python contributers
result = max(2,3)


# User defined
# they can return something
# They cant return - Non return
# they have parameters
# They don't parameters / arguments

def say_hello(): # No return type and No parameter / argument:
    print("Hello")

say_hello()

print("------------------------")
def say_hello_arg(name): # No return type with argument/ parameter
    print("Hello ", name)

result = say_hello_arg("Mani")
print(result)
say_hello_arg("Mani")
print("------------------------")

def say_hello_arg_default(name = "Mani"): # No Return type with default parameter
    print("Hello ", name)

say_hello_arg_default()
say_hello_arg_default("Balan")
say_hello_arg_default(name ="Dhanvin")
print("------------------------")

def sum_number_argument_ret(a, b): # Argument + Return type
    return a + b

result = sum_number_argument_ret(4,5)
print(result)

result = sum_number_argument_ret(a = 45, b = 56)
print(result)

