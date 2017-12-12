#encoding:utf8
class Animal(object):
	def __init__(self, weight, height, color): #有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法相匹配的参数，但是self不需要传，python解释器自己会把实例变量传进去
		self.weight = weight
		self.height = height
		self.color = color
	def run(self):
		print 'Animal is running...'
		print 1
		return 1
	def eat(self):
		print 'animal is eating meat...'

class Dog(Animal): #Animal是Dog的父类，子类获得了父类的全部功能
	def __init__(self,weight,height,teeth,color):
		self.weight = weight
		self.height = height
		self.teeth = teeth 
		self.color = color
	def run(self):
		print 'Dog is running...'
	def chase(self):
		print 'Dog is chasing another dog...' #类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()
	def fight(self):
		print 'Dog is fighting...'
class Cat(Animal):
	pass

dog1 = Dog('20kg', '100cm','犬牙','黑狗')
dog1.eat()

# animal.eat()

# dog = Dog()
# dog.run()
# dog.eat()
# cat = Cat()
# cat.eat()
# print type(cat) #cat是Cat类型的
###当我们定义一个class的时候，我们实际上就定义了一种数据类型。
###我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样
###
###

# print isinstance(cat, Cat)

# print isinstance(cat, Animal) #注意到两个都是True

# print isinstance(animal, Dog) #这个是False












































