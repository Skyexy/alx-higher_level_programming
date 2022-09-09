#!/usr/bin/python3
import sys
from MySQLdb import _mysql

mydb = _mysql.connect(
  host= "localhost",
  port = 3306,
  user= sys.argv[1],
  password= sys.argv[2],
  database= sys.argv[3],
)

sql = """SELECT * FROM states ORDER BY id"""
db.query(sql)
r=db.store_result()
print(r.fetch_row(maxrows=0))
