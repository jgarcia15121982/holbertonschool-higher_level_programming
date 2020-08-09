#!/usr/bin/python3
"""Script that takes an argument and displays
   all values in the states table of
   hbtn_0d_usa where name matches the argument
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_nm_srch = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=mysql_db,
                         port=3306)

    cur = db.cursor()
    cur.execute("""SELECT * FROM states
              WHERE name LIKE BINARY '{:s}'
              ORDER BY id ASC
           """.format(state_nm_srch))
    
    rows = cur.fetchall()
    for row in cur:
        print(row)

    cur.close()
    db.close()
