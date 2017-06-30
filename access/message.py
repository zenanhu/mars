#!/usr/bin/env python
# coding: utf-8

import time
from sqlalchemy.sql import select, and_

from mars.access.base import Base, db_query, row_to_dict, open_transaction
from mars.db.model import message
import mars.utils.meta


class Message(Base):
    __metaclass__ = mars.utils.meta.Singleton

    def create_message(self, title, content):
        with open_transaction(self) as conn:
            now = int(time.time())
            r = conn.execute(
                message.insert(),
                title=title, content=content, time_created=now, time_modified=now
            )
            return r.inserted_primary_key[0]

    def get_message(self, mid):
        q = select([message]).where(and_(
            message.c.id == mid,
            message.c.time_removed == 0
        ))
        with db_query(self, q) as r:
            return row_to_dict(r.fetchone())

    def get_messages(self, page=0, size=0):
        q = select([message]).where(and_(
            message.c.time_removed == 0
        ))
        if page >= 0 and size > 0:
            q = q.limit(size).offset(page*size)
        with db_query(self, q) as r:
            return [row_to_dict(x) for x in r.fetchall()]
