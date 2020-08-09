#!/usr/bin/python3
"""Script that lists all cities from the
   database hbtn_0e_4_usa
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
                         db=mysql_db,
                         port=3306)

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                   FROM states
                   JOIN cities
                   ON cities.state_id = states.id
                   ORDER BY cities.id ASC;
                """)
    rows = cur.fetchall()
    for row in cur:
        print(row)

    cur.close()
    db.close()
