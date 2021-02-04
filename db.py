import sqlite3


db = sqlite3.connect("faculty.db")


cursor = db.cursor()
   

name = input()
query = "SELECT about FROM mytable WHERE First_name="+name+";"
cursor.execute(query)
for row in cursor:
    print(row)

db.close()
