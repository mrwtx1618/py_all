# encoding:utf8
class Employee(object):
    num_of_emps = 0  # 类变量
    raise_amt = 1.04

    def __init__(self, first, last,
                 pay):  # Regular methods in a class automatically take the instance as the first argument. By convention, in regular methods, we call the instance method:self
        self.first = first  # 实例变量
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{}{}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # self.first = first  # 实例变量
        # self.last = last
        # self.email = first + '.' + last + '@email.com'
        # self.pay = pay #instead of doing that to make the code larger, We can use the super methods.
        super(Developer, self).__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self,first,last,pay,employees = None):
        super(Developer, self).__init__(first,last,pay)
    if employees is None:
        self.employees = []
    else:
        self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')
print dev_1.pay
dev_1.apply_raise()
print dev_1.pay
#
# print dev_1.email
# print dev_2.email

# print help(Developer)
print dev_1.email
print dev_1.prog_lang
