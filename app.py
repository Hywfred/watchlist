from flask import Flask
from flask import escape, url_for, render_template
app = Flask(__name__)

name = 'Grey Li'
movies = [
    {'title': 'My Neighbor Totoro', 'year': '1988'},
    {'title': 'Dead Poets Society', 'year': '1989'},
    {'title': 'A Perfect World', 'year': '1993'},
    {'title': 'Leon', 'year': '1994'},
    {'title': 'Mahjong', 'year': '1996'},
    {'title': 'Swallowtail Butterfly', 'year': '1996'},
    {'title': 'King of Comedy', 'year': '1999'},
    {'title': 'Devils on the Doorstep', 'year': '1999'},
    {'title': 'WALL-E', 'year': '2008'},
    {'title': 'The Pork of Music', 'year': '2012'},
]

@app.route("/")
def index():
    return render_template('index.html', name=name, movies=movies)

@app.route("/<name>")
def hello(name):
    return '{}, Welcome to my watchlist!\n<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'.format(escape(name))

@app.route('/test_url')
def test_url_for():
    # 下面是一些调用示例（请在命令行窗口查看输出的 URL）：
    print(url_for('index'))  # 输出：/
    # 注意下面两个调用是如何生成包含 URL 变量的 URL 的
    print(url_for('hello', name='greyli'))  # 输出：/greyli
    print(url_for('hello', name='peter'))  # 输出：/peter
    print(url_for('test_url_for'))  # 输出：/test_url
    # 下面这个调用传入了多余的关键字参数，它们会被作为查询字符串附加到 URL 后面。
    print(url_for('test_url_for', num=2))  # 输出：/test_url?num=2
    return 'Test URL page'