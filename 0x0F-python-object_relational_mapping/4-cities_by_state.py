#!/usr/bin/python3
''' Lists all cities from the database hbtn_0e_4_usa'''


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
            SELECT c.id, c.name, s.name
            FROM cities as c
            INNER JOIN states as s
                ON c.state_id = s.id
            ORDER BY c.id ASC
            ''')
        [print(row) for row in cur.fetchall()]
        cur.close()
        conn.close()
    except Exception:
        pass
