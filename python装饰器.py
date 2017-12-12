#encoding:utf8
#现在有一个简单的函数”myfunc”，想通过代码得到这个函数的大概执行时间
import time
'''
def timer(func):#这个函数的参数是一个函数
    start_time = time.time()
    func()
    end_time = time.time()
    seconds = (end_time - start_time)
    print('函数执行了{}秒'.format(seconds))
    # print('函数执行了%s秒'%seconds)

def wait_3_seconds():
    print('函数开始！')
    time.sleep(1)
    print('函数结束!')

timer(wait_3_seconds)
'''


#但是如果这样做的话,所有的wait_3_seconds的地方都要改为timer(wait_3_seconds)
#下面做一些改动
import time
print(time.time())

def timer(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        seconds = end_time - start_time
        print('该函数执行了{}秒'.format(seconds))
    return wrapper

@timer
def my_func():
    print('函数开始！')
    time.sleep(1)
    print('函数结束！')
print('现在函数的名字是',my_func.__name__)
# my_func = timer(my_func)
print('现在函数的名字是',my_func.__name__)
my_func()#这里my_func已经被装饰过了,在这个例子中被装饰的函数并不带参数
















































