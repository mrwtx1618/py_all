#encoding:utf8
class Student(object):             #Student是类名,紧接着是(object)，表示该类是从哪个类继承下来的，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类
	def __init__(self,name,score): #由于类可以起到模板的作用，
		self.__score = score       #因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去
		self.__name = name         #通过定义一个特殊的__init__方法
	def print_score(self):         #在创建实例的时候，就把name，score等属性绑上去
		print '%s:%s' % (self.__name, self.__score)
	def get_grade(self):
		if self.__score >= 90:
			return 'A'
		elif self.__score >= 60:
			return 'B'
		else:
			return 'F'
	def get_score(self):
		return self.__score
a = Student('Tom', 58) #实例化
# # print a.score
# print a.print_score()
# print a.get_grade() #外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
print a.get_score()
a.__score = 99 #但是外部代码还是可以取自由地修改一个实例的属性
print a.__score #打印的结果是99,发现加了两条下划线之后，这个对象的__score属性已经无法打印了
print a.get_score()



'''
如果要让内部属性不被外部访问，
可以把属性的名称前加上两个下划线__，
在Python中，实例的变量名如果以__开头,
就变成了一个私有变量（private），只有内部可以访问，
外部不能访问，所以，我们把Student类改一改。
'''














