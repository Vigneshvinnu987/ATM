import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='------------',# Use the your password
    port='3306',
    database='pydb',
)
mycursor = mydb.cursor()
#mycursor.execute("create table worldcup(Team varchar(15),Captain varchar(25),Squad_Members varchar(2))")
#mycursor.execute("Show Tables")
#sql = "Insert into worldcup(Team,Captain,Squad_Members) values(%s,%s,%s)"
#values = ("Bangaladsh","Musthafisur Rahuman","15")
#mycursor.execute(sql,values)
#mydb.commit()
#print(mycursor.rowcount,"Record inserted")
#mycursor.execute("Alter Table worldcup add column id int auto_increment primary key")
mycursor.execute("SELECT * FROM worldcup")
#mycursor.execute("Select * from worldcup where Team= 'Pakisthan' ")
#mycursor.execute("Desc worldcup")
#mycursor.execute("select * from worldcup order by Team desc") # asending default one
#mycursor.execute("update worldcup set captain='Dhoni' where id=1")
#print(mycursor.rowcount,"Record Updated")
result = mycursor.fetchall()
for i in result:
    print(i)
