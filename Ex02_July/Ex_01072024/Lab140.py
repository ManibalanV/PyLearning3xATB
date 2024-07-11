# Hybrid Inheritance

# multiple type of Inheritance
# such as single, multiple and multilevel inheritance

class A:
    def methodA(self):
        return "Method A"

class B(A):
    def methodB(self):
        return "Method B"

class C(A):
    def methodC(self):
        return "Method C"

class D(B, C): # multiple and multi level // MRO- Method Resolution Order
    def methodD(self):
        return "Method D"

# This is perfect example of multiple and multi level inheritance

d = D()
print(d.methodD())
print(d.methodA())
print(d.methodB())
print(d.methodC())

