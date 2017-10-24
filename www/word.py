#!/usr/bin/env python
# coding: utf-8

from mars.www.base import json_request, render_request
from mars.www.base import app

import mars.app.word


@app.route('/words', methods=['GET'])
@json_request()
def words():
    words = mars.app.word.get_words(0, 100)
    return {
        "words": words,
    }


@app.route('/dict1', methods=['GET'], strict_slashes=False)
@render_request('dict.html')
def dictionary():
    words = mars.app.word.get_words(0, 100)
    return {
        "words": words,
    }


@app.route('/dict/list', methods=['GET'])
@render_request('word_list.html')
def dict_list(page=0):
    page = int(page)
    words = mars.app.word.get_words(page)
    return {
        'words': words,
        'page': page,
    }


@app.route('/dict/word/<word>', methods=['GET'])
@render_request('word.html')
def search_dict(word):
    word = mars.app.word.get_word(word)
    return {
        'word': word['value'],
    }

