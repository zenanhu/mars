# coding: utf-8

from flask import render_template, make_response, request

from mars.www.base import json_request, render_request
from mars.www.core import app

import mars.db.logic.message


@app.route('/')
@render_request('home.html')
def home():
    messages = mars.db.logic.message.get_messages()

    return {
        'messages': messages
    }


@app.route('/message', methods=['POST'])
@json_request()
def leave_message(message):
    mars.db.logic.message.insert_message(message, message)
    return {
        'data': 'success',
    }


@app.route('/404', methods=['GET'])
@render_request('404.html')
def not_found():
    return {
    }
