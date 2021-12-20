#!/usr/bin/python3
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
