#!/usr/bin/env python
# coding: utf-8

from flask import send_file

import mars.app.message

from mars.www.base import json_request, render_request
from mars.www.base import app


@app.route('/', methods=['GET'], strict_slashes=False)
@app.route('/<path:path>', methods=['GET'], strict_slashes=False)
def vue(path=''):
    return send_file('client/dist/index.html')


@app.route('/tmp')
@render_request('home.html')
def home():
    messages = mars.app.message.get_messages(page=0, size=0)

    return {
        'messages': messages
    }


@app.route('/messages', methods=['GET'])
@json_request()
def get_messages():
    messages = mars.app.message.get_messages(page=0, size=0)
    return {
        'messages': messages
    }


@app.route('/message', methods=['POST'])
@json_request()
def leave_message(message):
    mid = mars.app.message.create_message(message, message)
    return {
        'rc': 0,
        'message_id': mid,
    }


@app.route('/404', methods=['GET'])
@render_request('404.html')
def not_found():
    return {
    }
