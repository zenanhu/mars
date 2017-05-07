#!/usr/bin/env python
# coding: utf-8


class MarsAccessBase(object):

    def __init__(self, *args, **kwargs):
        self._resources = kwargs.get('resources', base_resources())


def base_resources():
    dbpool = None
    return {
        'dbpool': dbpool,

    }
