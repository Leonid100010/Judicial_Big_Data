# -*- coding: utf-8 -*-
import json
from flask import Flask, render_template, request
import cuttt
import jieba
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result', methods=['GET', 'POST'])
def handle():
    if request.method == "POST":
        str = request.form.get("Case")
        str=jieba.cut(str,cut_all=False)  # 需要去除空格、换行符等符号
        str=" ".join(str)
        print(str)
        return str


if __name__ == '__main__':
    app.run(debug=True)
