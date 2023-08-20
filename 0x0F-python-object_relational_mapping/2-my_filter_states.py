#!/usr/bin/python3
""" module to filter DB acording to atgv provided """
import MySQLdb
from sys import argv


def main():
    """ finc not run when imported as module """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    start = db.cursor()
    start.execute("SELECT * FROM states WHERE states.name LIKE BINARY '{}'\
                  ORDER BY states.id".format(argv[4]))
    rows = start.fetchall()
    for row in rows:
        print(row)
    start.close()
    db.close()


if __name__ == "__main__":
    main()
