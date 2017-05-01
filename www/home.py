# coding: utf-8

from flask import render_template, make_response, request

from mars.www.base import json_request, render_request
from mars.www.core import app

import mars.db.logic.message


@app.route('/')
@render_request('home.html')
def home_test():
    messages = mars.db.logic.message.get_messages()

    return {
        'messages': messages
    }


@app.route('/message', methods=['POST'])
@json_request()
def leave_message():
    message = request.form['message']
    mars.db.logic.message.insert_message(message, message)
    return {
        'data': 'success',
    }
