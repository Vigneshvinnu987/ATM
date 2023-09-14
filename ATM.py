class ATM:
    def __init__(self,name,account_number):
        self.name = name
        self.account_number = account_number

    def show(self):
        print(f"{self.name} your account number is {self.account_number}")

    def withdraw(self):
        self.amount = int(input("Enter the Amount:"))
        self.password = int(input("Enter the Password:"))

        if self.amount == 0:
            print("Till enter the valid Amount")
        elif self.amount > 11000:
                print("Ohooo!!! you only withdraw 10,000 less than amount")
        elif self.password != 9999:
            print("Enter the valid password")
        elif self.password == 9999:
            print(f"Please collect the amount for { self.amount}")
        else:
            print("Thanks for using this ATM")

    def Balance(self):
        password = int(input("Enter the password: "))
        if password == 9999:
            print(f"{self.name} your balance is 200000")

Name = input("Enter the Name:")
Name.strip()
account = 0
if True:
    try:
        account = int(input("Enter the Account Number:"))
    except Exception as e:
        print(" Enter the Valid Account Number")
    else:
        option = "\n\t1.Withdraw\n\t2.Balance\n\t3.Exit"
        print(option)
        choose = int(input("Choose the Option:"))
        if choose == 1:
            w1 = ATM(Name, account)
            w1.show()
            w1.withdraw()
        elif choose == 2:
            w1 = ATM(Name,account)
            w1.show()
            w1.Balance()
        elif choose == 3:
            exit()
    finally:
        exit("Thanks for using")
# Why to use the breakpoint search chatgpt


