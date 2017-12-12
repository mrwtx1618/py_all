#encoding:utf-8
#作为一种HTTP请求方法，POST用于向指定的资源提交要被处理的数据。
#我们在某网站注册用户、写文章等时候，需要将数据保存在服务器中，这是一般使用POST方法。
#本文使用Python的requests库模拟客户端。postman


from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/register',methods = ['POST'])
def register():
    print(request.headers)
    print(request.form)
    print(request.form['name'])
    print(request.form.get('name'))
    print(request.form.getlist('name'))
    print(request.form.get('nickname',default = 'little apple'))
    return 'welcome'

if __name__ == '__main__':
    app.run(debug=True)



























































