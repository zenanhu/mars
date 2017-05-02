#!/usr/bin/env python
# coding: utf-8

import copy
import logging

from functools import wraps
from flask import jsonify, render_template, make_response, redirect, request, abort
import werkzeug.exceptions as http_exceptions

from mars.www.core import app


def log_request():
    logger = app.logger
    if not logger.isEnabledFor(logging.INFO):
        return
    logger.info("Request: %s [%s]", request.url, request.method)
    if request.form:
        logger.info("Request form: %s", request.form.to_dict())


class WebHandler:
    def __init__(self, request_kwargs, **decorator_kwargs):
        self.decorator_kwargs = copy.deepcopy(decorator_kwargs)
        self.request_params = WebHandler.init_request(request_kwargs, self.decorator_kwargs)

    @staticmethod
    def init_request(request_kwargs, decorator_kwargs):
        log_request()
        require_login = decorator_kwargs.pop('require_login', False)
        if require_login:
            abort(401)

        request_params = {}
        request_params.update(request_kwargs)
        if request.method == 'POST':
            if request.form:
                request_params.update(request.form.to_dict())
            elif request.json:
                request_params.update(request.json)

            if request.files:
                request_params.update({k: request.files.getlist(k) for k in request.files})
        else:
            request_params.update(request.args.to_dict())

        WebHandler.convert_params(request_params, decorator_kwargs)
        return request_params

    @staticmethod
    def convert_params(request_params, decorator_kwargs):
        pass

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def render_request(template_name, **param_types):
    def _render_request(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            try:
                with WebHandler(kwargs, **param_types) as web_handler:
                    result = func(**web_handler.request_params)
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
                with WebHandler(kwargs, **param_types) as web_handler:
                    result = func(**web_handler.request_params)
                    if hasattr(result, '__iter__'):
                        result = jsonify(result)
            except http_exceptions.HTTPException, e:
                raise e
            return result
        return wrapped
    return _json_request

