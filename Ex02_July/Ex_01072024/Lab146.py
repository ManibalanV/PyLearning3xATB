# Encapsulation:
# Inheritance
# Polymorphism (method overriding)
# Class
# Object
# Constructor
# self, super, __init__
# public, _, __ private

# Abstraction
# Abstraction - OOPs
# Hiding the details and showing the what is required

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"


dog = Dog("rancho")
print(dog.sound())