#!/usr/bin/python3
import sys
from MySQLdb import _mysql

if __name__ == "__main__":
	mydb = _mysql.connect(
		host= "localhost",
		port = 3306,
		user= sys.argv[1],
		password= sys.argv[2],
		database= sys.argv[3],
	)
	sql = """SELECT id, name FROM states ORDER BY id ASC"""
	db.query(sql)
	r=db.store_result()
	print(r.fetch_row(maxrows=0))
