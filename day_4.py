"""
    `html` - 模板渲染
    * 基础使用
    * 简单传参
    * json传参
"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/return_html")
def return_html_func():
    return render_template("html1.html")


@app.route("/gave_name")
def gave_name_func():
    name: str = "jom"
    return render_template("html2.html", name=name)


@app.route("/return_dict")
def return_dict_func():
    dicts = dict()
    dicts["name"] = "kom"
    dicts["age"] = 12
    return render_template("html3.html", dicts=dicts)


if __name__ == "__main__":
    app.debug = True
    app.run()
