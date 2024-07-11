# Hierarchical Inheritance

# Father - Multiple children

class Father:
    def BHK1(self):
        print("1BHK")

class Manibalan(Father):
    def BHK3(self):
        print("3BHK")

class Anna(Father):
    def BHK2(self):
        print("2BHK")

class Quicky(Father):
    def no_house(self):
        print("No House")



manibalan = Manibalan()
manibalan.BHK1()
manibalan.BHK3()

anna = Anna()
anna.BHK1()
anna.BHK2()





