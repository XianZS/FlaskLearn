# -*- coding: UTF-8 -*-
"""
    @Project : FlaskLearn 
    @File    : day_1.py.py
    @Author  : XianZS
    @meaning : 
"""
# 导入flask
from flask import Flask

# 创建app对象
app = Flask(__name__)


@app.route('/')
def index():
    return "index"


def test():
    app.run()


if __name__ == "__main__":
    test()
