class Person:
    # Class variables / instance variables
    name = "Mani"
    age = None
    def walk(self):
        a = 10 # Local variable
        print("I am a Method")
        print("Hi", self.age)

person1 = Person()
person1.walk()