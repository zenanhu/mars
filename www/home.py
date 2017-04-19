# coding: utf-8

from flask import render_template, make_response

from mars.www.base import json_request, render_request
from mars.www.core import app


@app.route('/')
@render_request('home.html')
def home_test():

    return {

    }


@app.route('/message', methods=['POST'])
@json_request()
def leave_message():
    return {
        'data': 'success',
    }
