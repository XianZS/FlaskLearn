"""
    flask如何操作数据库 sqlite3
    flask-sqlalchemy
"""
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, jsonify

"""
    将sqlite数据库和app对象连接起来
"""
app = Flask(__name__)
# ORM 映射机制
# 数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

"""
    创建一个User类对象
    其实就是数据库表
"""


class User(db.Model):
    # 继承 db.Model 表示会被识别
    # app通过db操作User对象
    user_id = db.Column(db.Integer, primary_key=True)
    # nullable 是否可以为空 False 不可以为空
    user_name = db.Column(db.String(256), nullable=False)
    # email
    user_email = db.Column(db.String(512), nullable=False)

    def __init__(self, user_id, user_name, user_email):
        self.user_id = user_id
        self.user_name = user_name
        self.user_email = user_email

    def __str__(self):
        return "<User {}>".format(self.user_id)

    def __repr__(self):
        print(f"user_id:{self.user_id}, user_name:{self.user_name}, user_email:{self.user_email}")


# 增加
@app.route("/my_add", methods=["GET"])
def my_add_func():
    # 从前端接收一个字符串
    user_things = request.get_json()
    print(user_things)
    # 创建user_obj对象
    user_obj = User(user_things["user_id"], user_things["user_name"], user_things["user_email"])
    if user_obj:
        # 压入内存
        db.session.add(user_obj)
        # 提交
        db.session.commit()
        return "Success"
    return "Fail"


# 删除
@app.route("/my_delete", methods=["DELETE"])
def my_delete_func():
    # 删除
    # 表.query.get("primary key")
    # （1）得到删除对象
    del_obj = User.query.get(10012)
    # （2）判断删除对象是否存在
    if del_obj:
        # （3）将删除内容压入内存之中
        db.session.delete(del_obj)
        # （4）提交删除对象
        db.session.commit()
        return "Success"
    return "Fail"


# 查找
@app.route("/my_select_all", methods=["GET"])
def my_select_all_func():
    # 被操作的数据对象.query.add/delete/all
    all_obj = User.query.all()
    if all_obj:
        # 如何打印all_obj，它其实就是User表
        for child in all_obj:
            print(child, child.user_id, child.user_name, child.user_email)
        # print(all_obj, type(all_obj))
        return "Success"
    else:
        return "Fail"


# 根据其它字段查询
@app.route("/my_select_by_other_str", methods=["GET"])
def my_select_by_other_str_func():
    select_obj = User.query.filter_by(user_name="kom").all()
    if select_obj:
        for child in select_obj:
            print(child, child.user_id, child.user_name, child.user_email)
        return "Success"
    else:
        return "Fail"


# 修改
@app.route("/my_update", methods=["PUT"])
def my_update_func():
    """
        将User_id对应数据的username修改为从前端传送的数值
    """
    user_id = request.args.get("user_id")
    new_user_name = request.args.get("new_user_name")
    # (1)得到修改对象 根据user_id得到修改对象
    update_obj = User.query.get(user_id)
    if update_obj:
        # (2)数据对象存在
        update_obj.user_name = new_user_name
        # (3)提交修改之后的数据
        db.session.commit()
        return "Success"
    else:
        return "Fail"


if __name__ == '__main__':
    with app.app_context():
        # app对象上线文管理中，创建相关数据库
        db.create_all()  # 创建继承了db.Model对象的数据库表
    app.debug = True
    app.run()
