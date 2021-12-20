#!/usr/bin/python3
""" Script that takes in arguments
and displays all values in the states
table of hbtn_0e_0_usa where name matches
the argument. write one that is
safe from MySQL injections!
"""
import MySQLdb
import sys
if __name__ == "__main__":
    inpt = sys.argv[4]

    db_database = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user=sys.argv[1],
                                  password=sys.argv[2],
                                  database=sys.argv[3])

    cursor = db_database.cursor()
    cursor.execute(
        """SELECT * \
        FROM states \
        WHERE name=%s \
        ORDER BY id ASC""", (sys.argv[4],))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_database.close()
