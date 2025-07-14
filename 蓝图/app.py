# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : app.py
    @Author  : XianZS
    @meaning : 
"""
from flask import Flask

from login.routes import login_bp
from random_number.routes import random_number_bp

# 创建app对象
app = Flask(__name__)

# 将蓝图和app对象绑定起来
# 绑定login蓝图
app.register_blueprint(
    blueprint=login_bp,
    url_prefix="/login_routes"
)
# 绑定获取随机数蓝图
app.register_blueprint(
    blueprint=random_number_bp,
    url_prefix="/random_number_routes"
)
if __name__ == '__main__':
    app.debug = True
    app.run()
