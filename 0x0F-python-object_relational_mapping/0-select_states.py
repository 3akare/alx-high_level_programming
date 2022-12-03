#!/usr/bin/python3
if __name__ == '__main__':
    import MySQLdb
    ''' import MySQLdb to connect with a MySQL database with python '''

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user="root",
        passwd="root",
        db="hbtn_0e_0_usa",
        charset="utf8")

    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
