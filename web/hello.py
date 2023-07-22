# -*- coding: utf-8 -*-
"""
    :author: allen lv
    wsgi
"""


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>hello, web!</h1>']
