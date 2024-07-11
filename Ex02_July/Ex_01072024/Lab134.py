# Inheritance
# Acquire the Attributes and Behaviour
# Data members and Methods

# 3 BHK House - F -> Inheritance - Son
# Concept in object-oriented programming (OOP)
# that allow a class (child class) to inherit attributes and methods from another class (parent class)

# Types of Inheritance

# single - 80 % - # API, Web Automation - 80 % -> single
# Multiple
# Multi level
# Hybrid
# Hierarchical

class Grandparent: # Parent Class, Base Class
    key = "!233"
    def grandparent_method(self):
        return "Grandparent's method"

class Father(Grandparent): # Child Class, Sub Class
    def parent_method(self):
        return "Parent's method"


grandfather = Grandparent()
grandfather.grandparent_method()
grandfather.parent_method()

parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)






