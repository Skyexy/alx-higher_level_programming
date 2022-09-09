#!/usr/bin/python3
"""List all states where 'name' matches the argument
But this time, one safe from MySQL injection.
Username, password, database name, and state name given as user args
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
    cmd = """SELECT cities.id, cities.name, states.name
         FROM states
         INNER JOIN cities ON states.id = cities.state_id
         ORDER BY cities.id ASC"""
    cur.execute(cmd)
    nStates = cur.fetchall()

    for state in nStates:
        print(state)

    cur.close()
    db.close()
