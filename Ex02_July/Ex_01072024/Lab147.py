from abc import ABC, abstractmethod

class Father(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def loan(self):
        pass

class Manibalan(Father):
    def loan(self):
        print("Loan given")
        

manibalan = Manibalan("Rancho") # TypeError: Can't instantiate abstract class Dog without an implementation for abstract method 'sound'
print(manibalan.loan())