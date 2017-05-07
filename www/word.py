# coding: utf-8

from flask import render_template, make_response, request

from mars.access.dict import AccessDict

from mars.www.base import json_request, render_request
from mars.www.core import app

import mars.db.logic.word


@app.route('/dict')
@render_request('dict.html')
def dictionary():
    words = mars.db.logic.word.get_words()
    return {
        "words": words,
    }


@app.route('/dict/list', methods=['GET'])
@render_request('word_list.html')
def dict_list(page=0):
    words = mars.db.logic.word.get_words(page)
    return {
        'words': words,
        'page': page,
    }


@app.route('/dict/word/<word>', methods=['GET'])
@render_request('word.html')
def search_dict(word):
    word = AccessDict().get_word(word)
    return {
        'word': word[2],
    }

