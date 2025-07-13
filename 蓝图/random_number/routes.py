# -*- coding: UTF-8 -*-
"""
    @Project : Item 
    @File    : routes.py
    @Author  : XianZS
    @meaning : 
"""
from flask import Blueprint
from random import randint

# 创建获取随机数蓝图对象
random_number_bp = Blueprint("random_number_bp", __name__)


# 创建子路由
# 返回正随机数的子路由
@random_number_bp.route("/random_number1", methods=["GET"])
def random_number_1():
    return f"{randint(1, 100)}"


# 返回负随机数的子路由
@random_number_bp.route("/random_number2", methods=["GET"])
def random_number_2():
    return f"{-randint(1, 100)}"
