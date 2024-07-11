class Father:
    def home(self):
        print("1BHK")


class Son(Father):
    def home(self):
        super().home()
        print("3BHK")


Manibalan = Son()
Manibalan.home()