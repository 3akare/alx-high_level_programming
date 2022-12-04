#!/usr/bin/python3
''' Takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument '''


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

    try:
        cur.execute(
            '''
            SELECT * FROM states WHERE name=%s ORDER BY id ASC
            ''', (sys.argv[4], ))
        query_rows = cur.fetchall()
        [print(row) for row in query_rows]
        cur.close()
        conn.close()
    except Exception:
        pass
