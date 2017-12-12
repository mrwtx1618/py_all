#encoding:utf8
# class A:
# 	def __init__(self):
# 		print "enter A"
# 		print "leave A"
# class B(A):
# 	def __init__(self):
# 		print "enter B"
# 		A.__init__(self) # 用类名来引用的方法，引入带绑定对象self，从而达到调用父类的目的
# 		print "leave B"


# b = B()
# print b

#这样做的缺点是，当一个子类的父类发生变化时，(如类B的父类由A变为C时)，必须遍历整个类定义，，把所有的通过非绑定的方法的类名全部替换过来





'''
class B(C): #A-->C
	def __init__(self):
		print "enter B"
		C.__init__(self) # A-->C
		print "leave B"
'''

#如果代码简单，这样的改动还可以接受。但如果代码量庞大，这样的修改可能是灾难性的。
#因此，从python2.2开始，python添加了一个关键字super，来解决这个问题。


class A(object):  # A must be new-style class
	def __init__(self):
		print "enter A"
		print "leave A"

class B(A):
	def __init__(self):
		print "enter B"
		super(B, self).__init__()
		print "leave B"



b = B()
print b


'''
对于super(B, self).__init__()是这样理解的：super(B, self)首先找到B的父类（就是类A），
然后把类B的对象self转换为类A的对象（通过某种方式，一直没有考究是什么方式，惭愧），
然后“被转换”的类A对象调用自己的__init__函数。

'''



































