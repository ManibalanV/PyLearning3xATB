class XYZ:
    def f1(self):
        try:
            a = int(input("Enter the number\n"))
        except Exception as e:
            print("Enter integer only value of a")
        else:
            print(a)
        finally:
            print("Anyhow I will be printed")


x = XYZ()
x.f1()