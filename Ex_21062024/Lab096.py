# Docorators
# What is decorator?
# A decorator is essentially a function that takes another function as an argument returns a new function that usually extends the behaviour


def my_decorator(func):

    def wrapper():
        print("Starting......")
        print("**************")
        func()
        print("**************")
        print("........Ending")
    return wrapper()

@my_decorator
def say_hello():
    print("Say Hello")
