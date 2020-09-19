from flask import Flask
from flask import escape, url_for
app = Flask(__name__)

@app.route("/")
def root():
    return "Welcome to my watchlist!"

@app.route("/<name>")
def hello(name):
    return '{}, Welcome to my watchlist!\n<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'.format(escape(name))

@app.route('/test_url')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('root'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('hello', name='greyli'))  # 输出：/greyli
    print(url_for('hello', name='peter'))  # 输出：/peter
    print(url_for('test_url_for'))  # 输出：/test_url
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test_url?num=2
    return 'Test URL page'