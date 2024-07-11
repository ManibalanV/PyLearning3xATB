# Polymorphism
# Polymorphism allows objects of different classes to be treated as objects of a common superclass.

# Manibalan - Son, Husband, Father, Brother
# Object - Method -> Mother, sister, ..

# Method overloading


# Method overriding:

class Shape:
    def area(self):
        print("Area of the shape is: ")

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius



shape1 = Rectangle(3,4)
print(shape1.area())

shape2 = Circle(10)
print(shape2.area())

shape3 = Shape()
shape3.area()


