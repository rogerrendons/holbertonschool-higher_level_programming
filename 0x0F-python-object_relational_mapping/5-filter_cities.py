#!/usr/bin/python3
""" Write a script that takes in the name of a state as an argument and lists
    all cities of that state, using the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user="{}".format(sys.argv[1]),
                          passwd="{}".format(sys.argv[2]),
                          db="{}".format(sys.argv[3]),
                          charset="utf8")

    cur = cnx.cursor()
    cur.execute("SELECT cities.name FROM cities LEFT JOIN states\
    ON states.id = cities.state_id WHERE states.name = %s", [sys.argv[4]])

    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    cnx.close()
