#!/usr/bin/python3
""" get cities from databases"""
import MySQLdb
from sys import argv


def main():
    """ func not run when import as module """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    start = db.cursor()
    start.execute("""SELECT cities.id, cities.name, states.name
                  FROM cities INNER JOIN states
                  ON cities.state_id = states.id
                  ORDER BY cities.id""")
    rows = start.fetchall()
    for row in rows:
        print(row)
    start.close()
    db.close()


if __name__ == "__main__":
    main()
