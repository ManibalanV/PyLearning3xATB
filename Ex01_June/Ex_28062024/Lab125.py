# Web Automation
# Page - You are going to automate

class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed")
# This is the end of the class


mani = VWOLoginPage("maniya@gmail.com", "123")
mani.login_confirm()

balan = VWOLoginPage("maniya@gmail.com", "Pass123")
balan.login_confirm()
