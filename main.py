from flask import Flask, render_template, request

# 创建flask对象
app = Flask(__name__, static_url_path='')


@app.route("/")
def index():
    """
    返回html页面数据
    :return:
    """
    # return "<h1>我是个人主页</h1>"
    return render_template("/firework.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7788)
    # app.run(host='192.168.1.100', port=7788)
