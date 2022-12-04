#!/usr/bin/python3
''' Takes in the name of a state as an argument and lists all
 cities of that state, using the database hbtn_0e_4_usa'''


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
            SELECT * FROM cities as c
            INNER JOIN states as s
                ON c.state_id = s.id
            ORDER BY c.id ASC
            ''')
        print(", ".join([c[2] for c in cur.fetchall()if c[4] == sys.argv[4]]))
        cur.close()
        conn.close()
    except Exception:
        pass
