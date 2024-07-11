class MyClass:
    def __init__(self):
        self.name = "Mani"
        self._email = "manibalan@google.com"

    def public_func(self):
        print("Pulic func()")

    def __private_func(self):
        print("You can only access me via a another method, This is private")

    def public_fn_private(self):
        self.__private_func()
        print(self._email)


a = MyClass()
a.public_func()

a.public_fn_private()


