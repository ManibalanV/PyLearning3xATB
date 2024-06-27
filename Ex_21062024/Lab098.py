def decorator1(func):
    def wrapper():
        print("Decorator 1")
        func()
    return wrapper

def decorator2(func):
    def wrapper():
        print("Decorator 2")
        func()
    return wrapper


@decorator1
@decorator2
def say_hello():
    print("Hello!")

say_hello()


# How Decorators Work
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# In this example:
# my_decorator is the decorator function
# wrapper is the inner function that adds behavior before and after calling func.
# The @my_decorator syntax is a shorthand for say_hello = my_decorator(say_hello).

# Benefits of Using Decorators:
# 1. Code reusability
# 2. Separation of concerns
# 3. Enhanced Readability

# Common Use Cases
# Logging
# Access Control
# Memoization
# Timing





