#encoding:utf8
from abc import ABCMeta #用来生成抽象基础类的元类

class MyABC:
    __metaclass__ = ABCMeta #生成了一个名叫MyABC的抽象基础类


MyABC.register(tuple) #然后再将tuple变成他的虚拟子类

assert issubclass(tuple, MyABC)
print isinstance((), MyABC)      #注意到()tuple元组是MyABC的子类
print isinstance([], MyABC)      #[]list列表不是MyABC的子类









