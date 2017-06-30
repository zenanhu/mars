#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import select, and_

from mars.access.base import Base, db_query, open_transaction, row_to_dict
from mars.utils.meta import Singleton
from mars.db.model import word


class Word(Base):
    __metaclass__ = Singleton

    def update_word(self, wid, **kwargs):
        with open_transaction(self) as conn:
            conn.execute(word.update().where(and_(
                word.c.id == wid,
            )).values(**kwargs))

    def get_word(self, w):
        q = select([word]).where(and_(
            word.c.word == w,
            ))
        with db_query(self, q) as r:
            return row_to_dict(r.fetchone())

    def get_word_by_id(self, wid):
        q = select([word]).where(and_(
            word.c.id == wid,
        ))
        with db_query(self, q) as r:
            return row_to_dict(r.fetchone())

    def get_words(self, page=0, size=0):
        q = select([word])
        if page >= 0 and size > 0:
            q = q.limit(size).offset(page * size)
        with db_query(self, q) as r:
            return [row_to_dict(x) for x in r.fetchall()]
