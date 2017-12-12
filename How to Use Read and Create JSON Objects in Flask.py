from flask import Flask
from flask import request
from flask import jsonify

#jsonify可以把python的一个字典或者列表转化为json格式



app = Flask(__name__)

@app.route('/',methods = ['GET','POST'])
def index():
    # value = request.json['array'][2]
    result = "result"
    # return value
    my_result =jsonify({"key":result,"the_list":[1,2,3,4,5],"date":'2017-7-27'})
    return my_result

if __name__ == '__main__':
    app.run(debug=True)



























