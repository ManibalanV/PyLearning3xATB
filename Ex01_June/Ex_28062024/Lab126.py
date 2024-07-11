# Encapsulation -
# bind the data variables with the methods
# Data Member - Class Variables
# Methods - def function within the class
# wrapping or binding the data variables with the methods - Encapsulation

# Hide the data members(class variables, instance variables) by using only the methods.

class Car:
    name = None
    password = "123"

    def __init__(self):
        print("I am called when an Object is created")

    def change_password(self):
        self.password = "456"


xuv = Car()
xuv.password = "456"

