#!/usr/bin/python3
""" Write a script that lists all cities from the database hbtn_0e_4_usa """

if __name__ == "__main__":
    import MySQLdb
    import sys

    cnx = MySQLdb.connect(host="localhost", port=3306,
                          user=sys.argv[1], passwd=sys.argv[2],
                          db=sys.argv[3])
    cur = cnx.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM \
                  cities JOIN states ON cities.state_id=states.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    cnx.close()
