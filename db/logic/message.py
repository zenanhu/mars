#!/user/bin/env python
# coding: utf-8

import MySQLdb

def get_conn():
    conn = MySQLdb.connect(user='space', passwd='space',
                           host='localhost',
                           db='mars')
    return conn

def get_messages():
    conn = get_conn()
    cursor = conn.cursor()
    query = ("select * from Message")
    cursor.execute(query)
    print cursor.fetchone()

    cursor.close()
    conn.close()
