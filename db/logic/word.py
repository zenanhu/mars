#!/usr/bin/env python
# coding: utf-8

import MySQLdb


def get_conn():
    conn = MySQLdb.connect(user='space', passwd='space',
                           host='localhost',
                           db='mars')
    return conn


def get_words():
    conn = get_conn()
    cursor = conn.cursor()
    query = """select * from Dict limit 10"""
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results


def get_word(word):
    conn = get_conn()
    cursor = conn.cursor()
    query = """select * from Dict WHERE word='%s'""" % word
    cursor.execute(query)
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return row

