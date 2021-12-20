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
        """SELECT cities.name \
        FROM cities \
        INNER JOIN states \
        ON cities.state_id = states.id \
        WHERE states.name=%s \
        ORDER BY cities.id ASC""", (inpt,))
    rows = cursor.fetchall()
    print(', '.join(["{:s}".format(row[0]) for row in rows]))
