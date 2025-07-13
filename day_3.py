"""
    Flask 视图函数 - 如何获取相应数据
        GET POST PUT DELETE
        视图函数是 Flask 应用中的核心部分，它负责处理请求并生成响应。
        视图函数与路由紧密结合，通过路由将 URL 映射到具体的视图函数。
        * 返回数据
        * 获取数据
"""
from flask import Flask, request

app = Flask(__name__)


# GET 请求
@app.route("/myget", methods=["GET"])
def get_func():
    request_type = request.method
    # request.args.get(key) ===>>> value
    name = request.args.get("name")
    name = name[::-1]
    return f"{request_type},{name}"


# POST 请求
@app.route("/mypost", methods=["POST"])
def post_func():
    request_type = request.method
    age = request.form.get("age")
    return f"{request_type},{age}"


# PUT 请求
@app.route("/myput", methods=["PUT"])
def put_func():
    request_type = request.method
    things_id = request.args.get("things_id")
    return f"{request_type},things_id:{things_id}"


# DELETE 请求
@app.route("/mydelete", methods=["DELETE"])
def delete_func():
    request_type = request.method
    name = request.args.get("name")
    return f"{request_type},things_id:{name}"


# JSON 传值
@app.route("/myjson")
def my_json_func():
    """
        {
            "name":"kom",
            "age":19
        }
    """
    # request.json.get("name") ===> kom
    # request.json.get("age") ===> 19
    name = request.json.get("name")
    age = request.json.get("age")
    return f"{name}的年龄是{age}"


@app.route("/many", methods=["GET", "POST"])
def many():
    if request.method == "GET":
        return "这是GET请求"
    else:
        return "这是POST请求"


if __name__ == "__main__":
    app.debug = True
    app.run()
