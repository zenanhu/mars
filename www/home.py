# coding: utf-8

from flask import render_template, make_response

from mars.www.core import app


@app.route('/')
def home_test():
    return make_response(render_template('home.html'))
