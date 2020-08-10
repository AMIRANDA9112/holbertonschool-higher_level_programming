# !/usr/bin/python3
""" lists all states with a name starting with 'N'"""

from sys import argv
import MySQLdb

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    my_db = argv[3]

    db = MySQLdb.connect(
        "localhost",
        user,
        password,
        my_db
    )

    cur = db.cursor()
    database = cur.execute("SELECT id, name FROM states ORDER BY states.id;")
    for i in range(0, database):
        rows = cur.fetchall()  # get all the rows.
        for row in rows:
            print(row)
    cur.close()  # Close all cursors.
    db.close()
