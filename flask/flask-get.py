# -*- coding: utf-8 -*-
"""
    :author: allen lv
    flask get
"""
from flask import Flask
from flask import request

app = Flask(__name__)


# 1. 匹配 /hello
@app.route("/")
def hello_0():
    return 'hello index'

# 1. 匹配 /hello
@app.route("/hello")
def hello_1():
    return 'hello flask'


# 2. 匹配 /hello/<params>
@app.route("/hello/<username>")
def hello_2(username):
    print('username:%s' % username)
    return 'hello ' + username


# 3. 匹配 /hello/args/<params>?id=xx&&age=xx
@app.route("/hello/args/<username>")
def hello_3(username):
    print('username:%s' % username)
    id = request.args.get("id")
    age = request.args.get("age")
    return 'hello, id from request %s, age from request %s' % (id, age)


if __name__ == '__main__':
    app.run()
