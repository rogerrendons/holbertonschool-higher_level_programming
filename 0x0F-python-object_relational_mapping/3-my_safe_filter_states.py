#!/usr/bin/python3
""" Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE
    TABLE states ; SELECT * FROM states WHERE name = '" as an input? """

import MySQLdb
import sys


if __name__ == "__main__":
    cnx = MySQLdb.connect(host="localhost", port=3306, user="{}"
                          .format(sys.argv[1]), passwd="{}"
                          .format(sys.argv[2]), db="{}"
                          .format(sys.argv[3]),
                          charset="utf8")
    cur = cnx.cursor()
    cur.execute("SELECT * FROM states WHERE BINARY name=%s", [sys.argv[4]])

    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    cnx.close()
