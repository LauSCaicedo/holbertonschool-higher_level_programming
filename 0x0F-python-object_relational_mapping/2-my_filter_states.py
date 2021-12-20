#!/usr/bin/python3
""" Script that takes in an argument
and displays all values in the states
table of hbtn_0e_0_usa where name
matches the argument.
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
    cursor.execute(
        "SELECT * \
        FROM states \
        WHERE name LIKE BINARY '{}' \
        ORDER BY id ASC;".format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    db_database.close()
