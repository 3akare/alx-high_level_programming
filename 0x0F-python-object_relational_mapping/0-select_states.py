#!/usr/bin/python3
''' Lists all states from the database hbtn_0e_0_usa '''


if __name__ == '__main__':
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
        user=sys.argv[1],
        password=sys.argv[2],
        db=sys.argv[3],
        port=3306,
        host='localhost'
        )

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
