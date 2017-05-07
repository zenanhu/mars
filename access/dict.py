#!/usr/bin/env python
# coding: utf-8

from mars.access.base import MarsAccessBase
from mars.db.logic.word import DictLogic


class MarsAccessDict(MarsAccessBase):

    def __init__(self, *args, **kwargs):
        super(MarsAccessDict, self).__init__(*args, **kwargs)

    def get_word(self, dbc, word):
        return DictLogic(dbc).get_word(word)


_access_dict = None


def get_access(*args, **kwargs):
    global _access_dict
    if args or kwargs:
        return MarsAccessDict(*args, **kwargs)
    elif _access_dict is None:
        _access_dict = MarsAccessDict()
    return _access_dict


AccessDict = get_access
