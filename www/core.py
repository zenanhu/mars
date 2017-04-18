# coding: utf-8

from flask import Flask, request, Blueprint


app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


#import mars.www.home
@app.route('/')
def home():
    return '<h1>Hello</h1>'


if __name__ == "__main__":
    app.run()
