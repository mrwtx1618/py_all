#encoding:utf8
class Employee:
	raise_amount = 1.04
	number_of_emps = 0
	def __init__(self, first, last, pay):
		self.first_name = first
		self.last_name = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'
		Employee.number_of_emps += 1
	def fullname(self):#each method within a class,automatically take the instance as the first argument
		return '{} {}'.format(self.first_name, self.last_name) #print the full name	

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount) #Employee可以改成self

	@classmethod# turn a regular method(实例方法) to a classmethod classmethod是用来指定一个类的方法为类方法，没有此参数指定的类的方法为实例方法
	def set_raise_amt()

emp1 = Employee('Corey', 'Schafer', 50000) #2 instances
emp2 = Employee('Test', 'User', 60000)#orderly
emp3 = Employee('Test', 'User', 60000)
###当实例化的时候，init方法会自动运行，emp1 would be passed in self
# emp1.first = 'Corey'
# emp1.last = 'Schafer'
# emp1.email = 'Corey.Schafer@company.com'
# emp1.pay = 50000

# emp2.first = 'Test'
# emp2.last = 'User'
# emp2.email = 'Test.User@company.com'
# emp2.pay = 60000

print emp1.email
print emp2.pay
print emp1.first_name
print emp1.fullname() #需要括号，因为这里是method而不是attribute
print emp2.fullname()

print emp1.fullname()
print Employee.fullname(emp1)

emp1.raise_amount = 1.05

print emp1.pay
emp1.apply_raise()
print emp1.pay
print emp1.raise_amount #从instance里面添加属性
print emp2.raise_amount
print Employee.raise_amount #从class里面添加属性
#It would first check if the instance contains that attribute,
#and if doesn't, it would check if the class or any class it 
#inherit from contains that attribute.
#So when we access raise_amount from our instances here,
#the instances don't have any attribute themselves, 
#they are accessing the classes raise_amount attribute
print emp1.__dict__ #实例属性
print Employee.__dict__ #类属性
print Employee.number_of_emps






