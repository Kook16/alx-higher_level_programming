#!/usr/bin/python3
'''
script that lists all states from the database hbtn_0e_0_usa
'''
import sys
import MySQLdb


if __name__ == "__main__":
    # connecting to the database
    db = MySQLdb.connect(
        host='localhost', port=3306, username=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur =  db.cursor()

    cur.execute("SELECT * FROM states;")

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
