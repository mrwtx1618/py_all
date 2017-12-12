#ecoding:utf8
#自从python2.6开始，新增了一种格式化字符串的函数str.format()
#语法：他通过{}和:来代替%
#通过位置：
print '{0},{1}'.format('abc',18)
print '{},{},{},{}'.format(1,2,3,4)
print '{}{}{}{}'.format(1,2,3,4)
print '{}{}{}{}'.format(1,2,3,4)
print '{} {} {} {}'.format(1,2,3,4)
print '{1},{0},{1}'.format('abc',18) #第0个位置是abc,第一个位置是18

#通过关键字参数
print '{name},{age}'.format(age = 18, name = 'Jack')

#通过对象属性：
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def __str__(self):
		return 'This guy is {self.name}, he is {self.age} old'.format(self = self)
print str(Person('Tom', 18))



#精度与类型f
print '{:.2f}'.format(3.1415926)





