import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password="----------",# Use the your password
    port='3306',
    database='pydb',
)
mycursor = mydb.cursor()
#mycursor.execute("Create Table IPL(ID int auto_increment primary key,Team varchar(20),Captain varchar(35),Voice_Captain varchar(25),Squad_Members varchar(2))")
print("\n\t IPL(Indian Premier League Team)")
print("\n\t Team    Captain   Voice_Captain   Squad_Members")
#A = "insert into ipl(Team,Captain,Voice_Captain,Squad_Members) values(%s,%s,%s,%s)"
#Team = str(input("Enter the Team Name:"))
#Captain = str(input("Enter the Team Captain:"))
#Voice_Captain = str(input("Enter the Team Voice_Captain:"))
#Squad_Members = input("Enter the total team members:")
#values = (Team,Captain,Voice_Captain,Squad_Members)
##mycursor.execute(A,values)
#mydb.commit()
#print(mycursor.rowcount,"Successfully Team Inserted")
mycursor.execute("Select * from ipl")
#mycursor.execute("Desc ipl")
result = mycursor.fetchall()
for i in result:
    print(i)