#!/usr/bin/python3
"""Script that list all states with a
   name starting with N from the database
   hbtn_0d_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=mysql_db)

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
