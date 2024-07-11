# Multiple Inheritance

class Father:
    def father_money(self):
        return "5"
    def home(self):
        return "This is from the Father"

class Mother:
    def mother_money(self):
        return "2"
    def home(self):
        return "This is from the Mother"

class Son(Mother, Father):
    def home(self):
        return "This is from the Son"

# Problematic: Diamond problem - Java
# Python: Multiple Inheritance
# F, M -> S

Manibalan = Son()
Manibalan.father_money()
Manibalan.mother_money()
print(Manibalan.home())

