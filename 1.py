#expose是一个装饰器,参数是一个函数,也返回一个函数

def expose(func):
    func.exposed = True
    return func




@expose
def myview():
    return dict(records = records)



print(myview.exposed)
#结果是True


