# -*- coding: utf-8 -*-
"""
    :author: allen lv
    flask post
"""
from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/form', methods=['post'])
def post_1():
    return 'post test'


# form
# application/x-www-form-urlencoded or multipart/form-data
@app.route('/form2', methods=['post'])
def post_2():
    username = request.form['username']
    password = request.form['password']
    return 'post received username:%s, password: %s' % (username, password)


# json
@app.route('/form4', methods=['post'])
def post_4():
    username = request.json['username']
    password = request.json['password']

    return 'post received username:%s, password: %s' % (username, password)


if __name__ == '__main__':
    app.run()
