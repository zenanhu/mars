#!/usr/bin/env python
# coding: utf-8

from earth.utils.wrapper import singleton

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
