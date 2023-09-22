import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="------------",# Use the your password
    port="3306",
    database="pydb"
)
mycursor = mydb.cursor()
print("\n\tDaily Attnance ")
#mycursor.execute("create table attnance(ID int auto_increment primary key,Name varchar(35),Mail_Id varchar(50),Passedout_year varchar(3),Phone_Number varchar(10),Comments varchar(50))")
#mycursor.execute("desc attnance")
#Name = str(input("Enter Your Name:"))
#Mail = input("Enter your mail_id:")
#passedout = input("Enter the your passed out year:")
#phone = input("Enter the Phone number:")
#comments = input("Enter your any comments:")
#a = "insert into attnance(Name,Mail_Id,Passedout_year,Phone_Number,comments) values(%s,%s,%s,%s,%s)"
#values = (Name,Mail,passedout,phone,comments)
#mycursor.execute(a,values)
#mydb.commit()
#print(mycursor.rowcount,f"{Name} attnance successfully sumited")
mycursor.execute("select * from attnance")
result = mycursor.fetchall()
for i in result:
    print(i)
