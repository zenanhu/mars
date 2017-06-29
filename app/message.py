#!/usr/bin/env python
# coding: utf-8

from mars.access.message import Message


def create_message(title, content):
    mid = Message().create_message(title, content)
    return mid


def get_message(mid):
    message = Message().get_message(mid)
    return message


def get_messages(page=0, size=10):
    messages = Message().get_messages(page=page, size=size)
    return messages
