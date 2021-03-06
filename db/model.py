#!/usr/bin/env python
# coding: utf-8

from sqlalchemy import Column, Integer, Table, MetaData, String, JSON, \
    PrimaryKeyConstraint, BigInteger, SmallInteger, TEXT, ForeignKeyConstraint, UniqueConstraint, Text, DECIMAL

metadata = MetaData()


message = Table(
    'Message',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String(300), nullable=False),
    Column('content', TEXT, nullable=False),
    Column('time_created', Integer),
    Column('time_modified', Integer),
    Column('time_removed', Integer, default=0),
    mysql_engine='InnoDB'
)

word = Table(
    'Word',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('word', String(300), nullable=True),
    Column('value', TEXT, nullable=True),
    Column('sentences', TEXT, nullable=True),
    mysql_engine='InnoDB'
)

