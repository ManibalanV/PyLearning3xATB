class Person:
    # Attributes:
    name = None
    id = None
    age = None
    phone_number = None

    # Behaviours:
    def talk(self):
        print("I can talk")

    def another(self):
        print("I am method")

    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    def walk(self):
        print("I am walking")


# Create a Object of the Person Class
# ObjectRef = Object - ClassName()
suriya = Person()
suriya.name = "suriya manibalan"
suriya.talk()

manibalan = Person()
manibalan.name = "Manibalan Vaithiyanathan"
manibalan.walk()

print(Person().sleep("ManibalanV"))



