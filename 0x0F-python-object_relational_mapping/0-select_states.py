#!/usr/bin/python3
""" list a item """

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    my_db = argv[3]

    db = connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=my_db)

    cursor = db.cursor()
    database = cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in range(database):
        ret = cursor.fetchone()
        print(ret)
    db.close()
