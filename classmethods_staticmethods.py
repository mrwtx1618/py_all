# encoding:utf8
class Employee:
    num_of_emps = 0  # 类变量
    raise_amt = 1.04

    def __init__(self, first, last,
                 pay):  # Regular methods in a class automatically take the instance as the first argument. By convention, in regular methods, we call the instance method:self
        self.first = first  # 实例变量
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        Employee.num_of_emps += 1

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod  # 创建一个类方法
    def set_raise_amt(cls,
                      amount):  # cls is our first argument instead of instance,we cannot use the word "class" here.Because that is a keyword of python.
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')  # Use the emp_str argument here.
        return cls(first, last, pay)  # return a new employee object

    @staticmethod
    def is_workday(
            day):  # Static method don't take the instance or the cls as the first argument.Return whether or not if it is a workday
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# Employee.set_raise_amt(1.05) #Now we are working with the class instead of the instance.
#
# print Employee.raise_amt
# print emp_1.raise_amt
# print emp_2.raise_amt
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
# new_emp_1 = Employee.from_string(emp_str_2)
# We wanna to create the employee from the string.
# first, last, pay = emp_str_1.split('-') #split the string on the '-'
# new_emp_1 = Employee(first,last,pay) #create a new employee

# print new_emp_1.email
# print new_emp_1.pay

import datetime

my_date = datetime.date(2016, 7, 11)
print Employee.is_workday(my_date)
