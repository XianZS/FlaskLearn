"""
    Flask 路由是 Web 应用程序中将 URL 映射到 Python 函数的机制。
    Flask 路由是 Flask 应用的核心部分，用于处理不同 URL 的请求，并将请求的处理委托给相应的视图函数。
    以下是关于 Flask 路由的详细说明，包括路由的定义、参数、方法和规则等。
        * 定义路由：使用 @app.route('/path') 装饰器定义 URL 和视图函数的映射。
        * 路由参数：通过动态部分在 URL 中传递参数。
        * 路由规则：使用类型转换器指定 URL 参数的类型，字符串、整数、浮点数、路径。
        * 请求方法：指定允许的 HTTP 请求方法。
        * 路由函数返回：视图函数可以返回不同类型的响应。
        * 静态文件和模板：管理静态文件和动态渲染 HTML 模板。
        * 路由优先级：确保路由顺序正确，以避免意外的匹配结果。
"""
from flask import Flask
from flask import render_template, jsonify, Response

app = Flask(__name__)


# * 定义路由：使用 @app.route('/path') 装饰器定义 URL 和视图函数的映射
@app.route("/")
def index():
    return "<h1>Index Page</h1>"


# * 路由参数：通过动态部分在 URL 中传递参数
@app.route("/say/<name>")
def say(name):
    return f"<h1>hello,{name}</h1>"


# * 路由规则：使用类型转换器指定 URL 参数的类型。
@app.route("/user/<int:user_id>")
def user1(user_id: int):
    return f"user1-{user_id}"


@app.route("/user/<string:user_id>")
def user2(user_id: str):
    return f"user2-{user_id}"


# * 请求方法：指定允许的 HTTP 请求方法。
@app.route("/get", methods=["GET"])
def get_method():
    return "get_method"


@app.route("/post", methods=["POST"])
def post_method():
    return "post_method"


# * 路由函数返回：视图函数可以返回不同类型的响应。
@app.route("/myresponse")
def my_response():
    response = Response("自定义相应类型", status=200)
    response.headers["name"] = "response"
    return response


# * 静态文件和模板：管理静态文件和动态渲染 HTML 模板。
@app.route("/html")
def html():
    return render_template("some.html")


# * 路由优先级：确保路由顺序正确，以避免意外的匹配结果
@app.route("/youxianji")
def youxianji1():
    return "优先级-1"


@app.route("/youxianji")
def youxianji2():
    return "优先级-2"


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')
