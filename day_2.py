"""
    Flask 路由是 Web 应用程序中将 URL 映射到 Python 函数的机制。
    /login def login_func(): 账号密码校验之类操作
    /select def select_func(): 进行查询操作
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
from flask import jsonify, Response, render_template

app = Flask(__name__)


# * 定义路由：使用 @app.route('/path') 装饰器定义 URL 和视图函数的映射
@app.route("/login")
def login_func():
    return "Login Page"


@app.route("/select")
def select_func():
    return "Select Page"


# * 路由参数：通过动态部分在 URL 中传递参数
@app.route("/say/<name>")
def say(name: str):
    return f"hello {name}"


# * 路由规则：使用类型转换器指定 URL 参数的类型。
@app.route("/type/<int:number>")
def type1(number):
    return f"int,{number}"


@app.route("/type/<string:strs>")
def type2(strs):
    return f"str,{strs}"


# * 请求方法：指定允许的 HTTP 请求方法。
# [GET POST] PUT DELETE
@app.route("/get", methods=["GET"])
def get_func():
    return "这是一个get请求"


@app.route("/post", methods=["POST"])
def post_func():
    return "这是一个post请求"


# * 路由函数返回：视图函数可以返回不同类型的响应。
@app.route("/json")
def json_func():
    dicts = dict()
    dicts["name"] = "tome"
    dicts["age"] = 19
    return jsonify(dicts)


@app.route("/string")
def str_func():
    return "strs"


@app.route('/html')
def html_func():
    return "<h1>html</h1>"


@app.route("/response")
def response_func():
    response = Response("自定义response对象", status=200)
    response.headers["name"] = "response"
    return response


# * 静态文件和模板：管理静态文件和动态渲染 HTML 模板。
# .html .png .jpg
@app.route("/return_html")
def return_html_func():
    return render_template("./some.html")


# * 路由优先级：确保路由顺序正确，以避免意外的匹配结果
@app.route("/my_route")
def func1():
    return "Func1"


@app.route("/my_route")
def func2():
    return "Func2"


if __name__ == "__main__":
    app.debug = True
    app.run(port=5000, host='0.0.0.0')
