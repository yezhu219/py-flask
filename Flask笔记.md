# Flask 笔记

## 1. 安装flask
```python
    pip install flask
```
## 2. 创建Flask应用程序

```python
    from flask import  Flask

    app = Flask(__name__)


    # 使用装饰器定义路由
    @app.route('/')
    def index():
        return 'hello word'
    
    if __name__ == '__main__':
        app.run()
```

## 3.路由

### 3.1 限定请求方式
    ` 路由默认只支持get请求，如果要支持其他请求方式需要配置`
### 3.2 路由传参
- 路由报错问题

![](D:\practice\learn-python\img\not found.png)

解决：
1. 路由未定义
2. 5000端口被占用

```python

# 路由定义

@app.route('/order')

@app.route('/order/')
带/路由访问时会自动补全/，
路由定义时不带/，访问时带/则会报错找不到


# 路由传参
@app.route('/order/<order_id>')
def getOrderId(order_id):
    return 'orderId %s' % order_id

#限制传参类型
@app.route('/order/<int:order_id>')
```
3.3 渲染模板
```python
# 渲染模板
@app.route('/tem')
def renderTem():
    return render_template('index.html')

# 模板页面必须放在templates文件夹下面，否则找不到
```
3.4 模板填充数据
```python
# 渲染模板
@app.route('/tem')
def renderTem():
    orderId = 1001
    return render_template('index.html', orderId=orderId)

# 模板中使用
<div>
    <b>订单号</b>
    <i>{{orderId}}</i>
</div>

```

3.5 条件渲染
```python
{% for item in list %}
<div>{{item}}</div>
{% endfor%}

{% if orderId==100 %}
<h2>if order Id == 10001</h2>
{% else %}
<h2>else</h2>
{% endif %}
```
tip: 设置代码片段
-  ``setting->eidtor->live Templates->html``
- 编写代码片段
- 点击define，定义应用范围
```python
{% if $END$ %}

{% else %}

{% endif %}
```
3.6 过滤器

网址：``https://dormousehole.readthedocs.io/en/latest/templating.html?highlight=%E8%BF%87%E6%BB%A4%E5%99%A8#registering-filters`


使用`|` 标识过滤器，支持链式调用

```python
list = "{a:1,b:2}"
{ list | toJson}
```

1.1 自定义过滤器








