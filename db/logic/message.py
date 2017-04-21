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
    query = """select * from Message"""
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_message(id):
    conn = get_conn()
    cursor = conn.cursor()
    query = """select * from Message WHERE id=%s""" % str(id)
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row


def insert_message(title, content):
    conn = get_conn()
    cursor = conn.cursor()
    query = """insert into Message (title, content) VALUES (%s, %s)""" % (title, content)
    try:
        cursor.execute(query)
        conn.commit()
    except:
        conn.rollback()

    cursor.close()
    conn.close()

