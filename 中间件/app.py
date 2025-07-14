# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : app.py
    @Author  : XianZS
    @meaning : 
"""
from flask import Flask

app = Flask(__name__)


@app.before_request
def before_request():
    print(">>> 前置中间件 <<<")
    print("在每个请求request执行之前触发")


@app.after_request
def after_request(response):
    print(">>> 后置中间件 <<<")
    print("在每个请求request执行之后触发")
    return response


@app.route("/")
def index():
    print("这里是HOME页面")
    return "<h1>HOME</h1>"


if __name__ == "__main__":
    app.debug = True
    app.run()
