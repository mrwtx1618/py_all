#encoding:utf8

class Employee():
    def __init__(self,name,age,salary):
        self.name = name
        self.age = age
        self.salary = salary
    def __repr__(self):
        return '({},{},${})'.format(self.name,self.age,self.salary)
e1 = Employee('Carl',37,70000)
e2 = Employee('Sarah',29,80000)
e3 = Employee('John',43,90000)

employees = [e1,e2,e3]

def e_sort(emp):
    return emp.age



s_employees_1 = sorted(employees,key = e_sort)

s_employees_2 = sorted(employees,key = lambda e:e.salary)

print(s_employees_1 )
print(s_employees_2)



























