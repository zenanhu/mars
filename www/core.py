# coding: utf-8

from flask import Flask, request, Blueprint, render_template, make_response

import logging
import datetime


app = Flask(__name__)


def init_logger(app):
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.DEBUG)
    app.logger.addHandler(stream_handler)

init_logger(app)


@app.before_request
def before_request_logging():
    app.logger.error(' '.join([
        str(datetime.datetime.now()),
        request.url,
        "[%s]" % request.method,
        request.data,
    ]))


@app.route('/googleb591a2ae56260ef9.html')
def google_verify():
    return make_response(render_template('googleb591a2ae56260ef9.html'))


@app.route('/ping')
def ping():
    return 'pong'


import mars.www.home
import mars.www.word


if __name__ == "__main__":
    app.run()
