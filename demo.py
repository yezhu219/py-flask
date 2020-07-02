from flask import Flask, render_template

app = Flask(__name__)


# 使用装饰器定义路由
@app.route('/')
def index():
    return 'hello word'


# 路由传参
@app.route('/order/<int:order_id>')
def getOrderId(order_id):
    return 'orderId %s' % order_id


# 渲染模板
@app.route('/tem')
def renderTem():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
