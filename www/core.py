# coding: utf-8

from flask import Flask, request, Blueprint

app = Flask(__name__)


@app.route('/ping')
def ping():
    return 'pong'


if __name__ == "__main__":
    app.run()
