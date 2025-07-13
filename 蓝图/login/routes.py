# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : routes.py
    @Author  : XianZS
    @meaning : 
"""
# 导入蓝图
from flask import Blueprint

# 创建蓝图对象 login_bp
login_bp = Blueprint("login_bp", __name__)


# 子路由的url=蓝图对象的路由url+自定义的子路由url
# 真正的urk=/login_routes/login

# 创建子路由
@login_bp.route("/login", methods=["GET", "POST"])
def login():
    return "登陆成功"
