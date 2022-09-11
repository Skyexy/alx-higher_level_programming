#!/usr/bin/python3
"""List all states from a given db sorted in ascending order by id
Username, password, and database names are given as user args
"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cur = db.cursor()
    cmd = """SELECT id, name FROM states WHERE NAME =%s ORDER BY id ASC"""
    cur.execute(cmd, (sys.argv[4],))
    allStates = cur.fetchall()
    for state in allStates:
        print(state)

    cur.close()
    db.close()
