#encoding:utf8
class A():
	height=None
	def set_height(self,x):
		self.height = x
	def __init__(self, x, y):
		self.height = x
		self.weight = y


###有了初始化方法以后，在实例化A的时候,就会按顺序自动传入参数
p=A(172,'70kg')
print p.height
print p.weight
p.set_height(10)
print p.height