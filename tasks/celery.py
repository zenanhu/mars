#!/usr/bin/env python
# coding: utf-8

from __future__ import absolute_import, unicode_literals
from celery import Celery


celery = Celery('mars_tasks',
             broker='redis://localhost:6379/0',
            #  backend='amqp://',
             include=['mars.tasks.test'])


if __name__ == '__main__':
    celery.start()