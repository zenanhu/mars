#!/usr/bin/env python
# coding: utf-8

from mars.access.word import Word


def update_word(wid, sentences):
    Word().update_word(wid, sentences=sentences)


def get_word(word):
    word = Word().get_word(word)
    return word


def get_word_by_id(wid):
    word = Word().get_word_by_id(wid)
    return word


def get_words(page=0, size=10):
    words = Word().get_words(page=page, size=size)
    return words
