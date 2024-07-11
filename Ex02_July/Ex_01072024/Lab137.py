# Multilevel Inheritance

class Grandparent:
    def grandparent_method(self):
        return "Grandparent's Method"

class Parent(Grandparent):
    def parent_method(self):
        return "Parent's Method"

class Child(Parent):
    def child_method(self):
        return "Child's Method"


child_object_ref = Child()
print(child_object_ref.grandparent_method())
print(child_object_ref.parent_method())
print(child_object_ref.child_method())

parent_object_ref = Parent()
parent_object_ref.parent_method()
parent_object_ref.grandparent_method()

grand_parent_ref = Grandparent()
grand_parent_ref.grandparent_method()