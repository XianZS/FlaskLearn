# -*- coding: UTF-8 -*-
"""
    @Project : FlaskLearn 
    @File    : day_2.py.py
    @Author  : XianZS
    @meaning : 路由
"""
"""
    路由：其实就是url
    映射请求和处理函数之间的关系
    eg：
        * 登陆请求 127.0.0.1:5000/login
        login_func()
        * 查询 /find_user
        find_user_func()
"""
from flask import Flask

app = Flask(__name__)


@app.route("/login")
def login():
    return "<h1>Login Page</h1>"


@app.route("/find_user")
def find_user():
    return "<h1>find_user</h1>"


if __name__ == "__main__":
    app.run()
