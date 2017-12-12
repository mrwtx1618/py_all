# #encoding:utf8
# class A(object):
# 	def __init__(self):
# 		print "Enter A"
# 		print "Leave A"

# class B(A):
# 	def __init__(self):
# 		print "Enter B"
# 		A.__init__(self)
# 		print "Leave B"

# class C(A):
# 	def __init__(self):
# 		print "Enter C"
# 		A.__init__(self)
# 		print "Leave C"

# class D(A):
# 	def __init__(self):
# 		print "Enter D"
# 		A.__init__(self)
# 		print "Leave D"

# class E(B, C, D):
# 	def __init__(self):
# 		print "Enter E"
# 		B.__init__(self)
# 		C.__init__(self)
# 		D.__init__(self)
# 		print "Leave E"

# e = E()
# print e
# #结果是公共父类A被调用多次



class A(object):
    def __init__(self):
        print('Enter A')
        self.__test = 0
class C(object):
    def __init__(self):
        print('Enter C')
        super(C,self).__init__()
        self.__test2 = 3
class D(object):
    def __init__(self):
        super(D,self).__init__()
        print('enter D')
class B(A):
    def __init__(self):
        print('Enter B')
        super(B,self).__init__()
    def set(self):
        self.__test = 2
    def display(self):
        print(dir(self))
class E(C,D):
    def __init__(self):
        print('Enter E')
        super(E,self).__init__()




e = E()
print e











































