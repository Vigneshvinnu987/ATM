import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="---------------",#Your password
    database="pydb",
    port="3306"
)
mycursor = mydb.cursor()
'''
#mycursor.execute("create table Account(Id int auto_increment primary key,Name varchar(30),Account_Number varchar(15),Password varchar(4),Amount varchar(6))")
#mycursor.execute("desc account")
Name = input("Enter your Name:")
AN = int(input("Enter the your account number:"))
password = int(input("Enter the password:"))
amount = int(input("Enter the amount:"))
a = "Insert into account(Name,Account_Number,Password,Amount) values(%s,%s,%s,%s)"
values = (Name,AN,password,amount)
mycursor.execute(a,values)
mydb.commit()
print(mycursor.rowcount,f"{Name} account successfully added")
'''


class ATM:
    def __init__(self,name,account):
        self.name = name
        self.account = account

    def show(self):
        print(f"{self.name} your account number is {self.account}")

    def withdraw(self):
        self.amount = int(input("Enter the Amount:"))
        self.password = int(input("Enter the Password:"))

        if self.amount == 0:
            print("Till enter the valid Amount")
            if self.amount > 10000:
                print("Please enter the valuevabel amount only withdraw 10,000")
                if self.password == password1:
                    print(f"Please colloect your cash {self.amount}")
        else:
            print("Thanks for using this ATM")

    def Balance(self):
        password = int(input("Enter the password: "))
        if password == password1:
            print(f"{self.name} your balance is {balance}")
        else:
            print("Invalid password please enter the valid password")

Name = input("Enter the Name:")
Name.strip()
mycursor.execute(f"select * from Account where Name='{Name}'")
result = mycursor.fetchall()
for i in result:
    global a
    a = i
account = a[2]
password1 = int(a[3])
balance = a[4]
#print(account)
if True:
    try:
        print(f"{account} Yours account number")
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



