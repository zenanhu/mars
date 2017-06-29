#!/usr/bin/env python
# coding: utf-8

from contextlib import contextmanager

from sqlalchemy import create_engine

from earth.utils.wrapper import singleton
import mars.utils.meta
import mars.conf


def create_db_engine():
    return create_engine(mars.conf.database_url)


class Resource(object):
    __metaclass__ = mars.utils.meta.Singleton

    def __init__(self):
        self._engine = None

    def get_db_engine(self):
        if not self._engine:
            self._engine = create_db_engine()
        return self._engine


class Base(object):
    def __init__(self, *args, **kwargs):
        self._resources = Resource()

    def get_db_engine(self):
        return self._resources.get_db_engine()


@contextmanager
def db_query(base, q):
    conn = base.get_db_engine().connect()
    result = conn.execute(q)
    yield result
    result.close()


@contextmanager
def open_transaction(base):
    conn = base.get_db_engine().connect()
    trans = conn.begin()
    try:
        yield conn
        trans.commit()
    except:
        trans.rollback()
        raise


def row_to_dict(r):
    if not r:
        return None

    return {k: v for k, v in r.items()}


class MarsAccessBase(object):

    def __init__(self, *args, **kwargs):
        self._resources = kwargs.get('resources', base_resources())

    def dbpool(self):
        return self._resources.get('dbpool')


@singleton
def base_resources():
    dbpool = None
    return {
        'dbpool': dbpool,
    }

