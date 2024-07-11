class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def __withdraw(self, amount):
        self.balance -= amount

    def __show_balance(self):
        print("Your Balance is ", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.__show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, amount):
        if auth:
            self.__withdraw(amount=amount)
        else:
            print("Not Allowed")


jp_chase = BankAccount()
jp_chase.deposit(100)

secret_pass = input("Enter your 4 digit PIN: ")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass = input("Enter your 4 digit PIN to Withdraw: ")
your_amount = int(input("Enter the amount to withdraw: "))
if secret_pass == "1234":
    jp_chase.if_you_are_auth_user(True, amount=your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_user(False, amount=your_amount)


