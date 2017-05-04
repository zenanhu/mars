# coding: utf-8

from flask import render_template, make_response, request

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
def search_dict(page):
    words = mars.db.logic.word.get_words(page)
    return {
        "words": words,
    }


@app.route('/dict/<word>', methods=['GET'])
@render_request('word.html')
def search_dict(word):
    word = mars.db.logic.word.get_word(word)
    return {
        'word': word[2],
    }

