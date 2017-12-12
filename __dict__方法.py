#encoding:utf8
#一个instance下有__dict__方法
class A():
    x = 1 #通过A.x访问，或者instance访问
    y = x
    def __init__(self,x):#创建实例时会调用
        self.x = x

a = A(10)#self就是a，x is 10
a.__dict__ = {'a':1,'b':2} #instance有__dict__方法
print a.a
print a.b

x = dict({'a':1, 'b':2})
print x['a']





class A():
    pass
x = A()
x.__dict__ = {'a' : 1}
print x.a


class A():
    y = 1
x = A()
print x.__dict__
print A.__dict__







