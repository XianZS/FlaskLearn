# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : app.py
    @Author  : XianZS
    @meaning : 
"""
from flask import Flask, abort

app = Flask(__name__)

"""
    自定义错误类型
"""


class MyError(Exception):
    pass


@app.route("/my_error", methods=["GET"])
def my_error_func():
    raise MyError


@app.errorhandler(MyError)
def my_error_handler(e):
    return "这是我的自定义错误类型"


"""
    单个错误状态码捕捉
"""


# 404 500
@app.errorhandler(404)
def errorhandler_func(e):
    print(e)
    return "error"


"""
    捕捉全局错误状态码
"""


@app.errorhandler(Exception)
def errorhandler_func(e):
    return "这是全局错误状态码"


"""
    手动触发错误状态 403 404 500 abort
"""


@app.route("/handler_make_404")
def handler_make_404():
    abort(404)


@app.route("/handler_make_403")
def handler_make_403():
    abort(403)


@app.route("/handler_make_500")
def handler_make_500():
    abort(500)


if __name__ == '__main__':
    app.debug = True
    app.run()
