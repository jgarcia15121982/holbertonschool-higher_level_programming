#!/usr/bin/python3
"""Script that takes int the name of a state
   as an argument and lists all cities of
   that state using database hbtn_0d_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    state_nm = sys.argv[4]
    db = MySQLdb.connect(host="localhost",
                         user=mysql_username,
                         passwd=mysql_passwd,
                         db=mysql_db,
                         port=3306)

    cur = db.cursor()
    cur.execute("""SELECT cities.name
                   FROM cities
                   JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %(state_nm)s
                   ORDER BY cities.id ASC;
                """, {'state_nm': state_nm})
    rows = cur.fetchall()
    listx = []
    for row in cur:
        listx.append(row[0])
    print(", ".join(listx))
    cur.close()
    db.close()
