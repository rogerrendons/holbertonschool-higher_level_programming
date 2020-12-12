#!/usr/bin/python3
"""
"""

if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    with MySQLdb.connect(host="localhost", user=argv[1], passwd=argv[2],
                         db=argv[3], port=3306) as db:
        db.execute("SELECT *\
                   FROM states\
                   WHERE name = %s", (argv[4],))
        table = db.fetchall()
        for data in table:
            print(data)
