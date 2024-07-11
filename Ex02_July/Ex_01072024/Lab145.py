# Method Overloading:
# Python doesn't support method overloading in the traditional sense.

class MathUtils:
    def add(self, a, b):
        return a+b

    def add(self, a, c):
        return a+c

math = MathUtils()
op1 = math.add(3,4)
op2 = math.add(a=3, c=5)
print(op1)
print(op2)