#!/usr/bin/python3
"""
Script that lists
all states from the
database hbtn_0e_0_usa.
"""
import MySQLdb
import sys
if __name__ == "__main__":

    db_database = MySQLdb.connect(host="localhost",
                                  port=3306,
                                  user=sys.argv[1],
                                  password=sys.argv[2],
                                  database=sys.argv[3])

    cursor = db_database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_database.close()
