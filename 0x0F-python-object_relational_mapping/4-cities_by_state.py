#!/usr/bin/python3
"""
    match into tables
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

    cur = db.cursor()
    database = cur.execute("SELECT cities.id, cities.name, states.name \
                             FROM cities JOIN states ON cities.state_id = \
                             states.id ORDER BY cities.id;")
    for i in range(0, database):
        ret = cur.fetchone()
        print("{}".format(ret))

    cur.close()
    db.close()
