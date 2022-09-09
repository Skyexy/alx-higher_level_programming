#!/usr/bin/python3
import sys
import mysql.connector

mydb = mysql.connector.connect(
  host= "localhost",
  port = 3306,
  user= sys.argv[1],
  password= sys.argv[2],
  database= sys.argv[3],
)
mycursor = mydb.cursor()
sql = "SELECT * FROM states ORDER BY id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
