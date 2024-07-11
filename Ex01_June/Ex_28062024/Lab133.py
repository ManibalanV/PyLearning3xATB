class Dog:
    name = None # if you dont give this also it will work
    id = None # if you dont give this also it will work
    def __init__(self, name="default", id="12"):
        self.name = name
        self.id = id

    def sleep(self):
        print("Who is sleeping -> " + self.name)

dog1 = Dog("Chow", "12")
dog2 = Dog("Mow", "13")
dog3 = Dog()
dog3.name = "Now"
dog3.id = "14"

print(f'{dog1.name} has ID {dog1.id}')
print(f'{dog2.name} has ID {dog2.id}')
print(f'{dog3.name} has ID {dog3.id}')

dog1.sleep()
dog2.sleep()
dog3.sleep()
