#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, unicode_literals
from mars.tasks.celeryapp import app


@app.task
def add(x, y):
    return x + y

