class Dog:
    name = None
    id = None

    # Constructor; Use to initialize the values of the instance variables (Attributes)
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def sleep(self):
        print("Sleeping")


dog1 = Dog("Cha", '12')
dog2 = Dog("Pah", '13')

print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')
