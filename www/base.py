#!/usr/bin/env python
# coding: utf-8

from functools import wraps
from flask import jsonify, render_template, make_response, redirect
import werkzeug.exceptions as http_exceptions


def render_request(template_name, **param_types):
    def _render_request(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                result = func(**kwargs)
                response = make_response(render_template(template_name, **result))
                result = response
            except http_exceptions.HTTPException, e:
                if e.code == 404:
                    return redirect('/404')
                else:
                    raise e
            return result
        return wrapped
    return _render_request


def json_request(**param_types):
    def _json_request(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                result = func(**kwargs)
                if hasattr(result, '__iter__'):
                    result = jsonify(result)
            except http_exceptions.HTTPException, e:
                raise e
            return result
        return wrapped
    return _json_request

