#!/usr/bin/python3
""" search match"""


from sys import argv
import MySQLdb

if __name__ == '__main__':

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
    database = cur.execute("SELECT * FROM states ORDER BY states.id;")
    for i in range(0, database):
        ret = cur.fetchone()
        if ret[1] == names:
            print("{}".format(ret))

    cur.close()
    db.close()
