#encoding:utf8
import memory_profiler
import random
import time

names = ['John','Corey','Adam','Steve','Rick','Thomas']
majors = ['Math','Engineering','CompSci','Arts','Business']

print('Memory (Before):{}Mb'.format(memory_profiler.memory_usage()))

def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id':1,
                    'name':random.choice(names),
                    'major':random.choice(majors)
        }
        result.append(person)
    return result
# print(people_list(names))



def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id':1,
                    'name':random.choice(names),
                    'major':random.choice(majors)
        }
        yield person

t1 = time.clock()
people = people_generator(1000000)
t2 = time.clock()




print('Memory (after):{}Mb'.format(memory_profiler.memory_usage()))

