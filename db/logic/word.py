#!/usr/bin/env python
# coding: utf-8

import MySQLdb

import mars.db.tables


def get_conn():
    conn = MySQLdb.connect(user='space', passwd='space',
                           host='localhost',
                           db='mars', charset='utf8')
    return conn


def get_words(page=0, limit=10):
    conn = get_conn()
    cursor = conn.cursor()
    query = """select * from Dict limit %s, %s""" % (page, limit)
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_word(word):
    return None


class DictLogic(object):
    def __init__(self, conn):
        self._conn = conn
        self._dict = mars.db.tables.Dict()

    def get_word(self, word):
        conn = get_conn()
        cursor = conn.cursor()
        query = """select * from Dict WHERE word='%s'""" % word
        cursor.execute(query)
        row = cursor.fetchone()
        cursor.close()
        conn.close()
        return row
