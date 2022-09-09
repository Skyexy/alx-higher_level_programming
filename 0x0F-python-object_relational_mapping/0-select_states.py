#!/usr/bin/python3
import MySQLdb
import sys

db=MySQLdb.connect(host="localhost",user=sys.argv[1],port=3307, passwd=sys.argv[2],db=sys.argv[3])
r=db.store_result()
print(r.fetch_row(maxrows=0))
