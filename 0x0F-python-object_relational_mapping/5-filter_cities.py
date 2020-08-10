#!/usr/bin/python3
"""
    interchange match date
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":

    user = argv[1]
    password = argv[2]
    my_db = argv[3]
    names = argv[4]

    db = MySQLdb.connect(
        "localhost",
        user,
        password,
        my_db
    )

    my_db = MySQLdb.connect(**db)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
                 FROM cities INNER JOIN states \
                 ON cities.state_id = states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id", (names,))

    rows = cur.fetchall()  # get all the rows.
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
