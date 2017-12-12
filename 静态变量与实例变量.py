#encoding:utf8
class Person(object):
    TAG = "Personaaaaaaaaaaaaaaaaaaaaaaaaa"  # 静态变量,在class内的，但不在class的方法内的，这就是静态变量

    def __init__(self, name):  # self 当前的实例对象（简单的说一下，其实都是引用哈）
        print Person.TAG  # 这里调用了静态变量
        self.personName = name  # personName是实例变量 （简单说就是因为self，哈哈）,在class的方法内的，用self修饰的变量，这就是实例变量

    def printName(self):
        group = "BeiJing_"  # group是局部变量
        print group + self.personName  # self.personName, 调用实例变量


if __name__ == "__main__":
    p = Person('W')
    p.printName()