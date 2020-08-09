#!/usr/bin/python3
"""Get all states from hbtn_0d_usa
   database
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
    cur.execute("SELECT * FROM states ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
