# coding: utf-8

from flask import Flask, request, Blueprint, render_template, make_response


app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


#import mars.www.home
@app.route('/')
def home():
    return make_response(render_template('home.html'))


if __name__ == "__main__":
    app.run()
