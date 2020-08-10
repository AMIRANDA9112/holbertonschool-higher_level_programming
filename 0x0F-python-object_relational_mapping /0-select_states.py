#!/usr/bin/python3
""" list a item """


from sys import argv
import MySQLdb

if __name__ == '__main__':

    user = argv[1]
    password = argv[2]
    mydb = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=password,
        db=mydb)

    cursor = db.cursor()
    database = cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for i in range(database):
        print(cursor.fetchone())
    db.close()
