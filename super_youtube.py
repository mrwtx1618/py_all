#encoding:utf8
class Person(object):
	def __init__(self, fn, ln, a):
		self.first_name = fn
		self.last_name = ln
		self.age = a

	def __str__(self): #一些特殊方法,所以前后都有双下划线
		return self.last_name + ',' + self.first_name

	def __eq__(self, other):
		return self.first_name == other.first_name and self.last_name == other.last_name
	def sayHello(self):
		print "Hello" + self.first_name + ", how are you?"


class Student(Person):
	def __init__(self ,fn, ln, a, g):
		super(Student, self).__init__(fn, ln, a)
		self.grades = g




























