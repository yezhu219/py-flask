from flask import Flask, render_template, url_for

app = Flask(__name__)


# 使用装饰器定义路由
@app.route('/')
def index():
    return 'hello word'
@app.route('/aa')
def aa():
    list = [1, 2, 3, 4, 5]
    return render_template('test.html',list=list)

# 路由传参
@app.route('/order/<int:order_id>')
def getOrderId(order_id):
    return 'orderId %s' % order_id


# 渲染模板
@app.route('/tem/')
def renderTem():
    orderId = 1001
    list = [1,2,3,4,5]
    dic= {'a':1,'b':2,'c':3,'name':'网商贷'}
    return render_template('index.html', orderId=orderId,list=list,dic=dic)

# URL构建


if __name__ == '__main__':
    app.run()
