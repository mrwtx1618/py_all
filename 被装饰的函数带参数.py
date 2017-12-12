#encoding:utf-8

#下面看一个被装饰函数带有参数的例子

import time



def timer(func):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        add_result = func(*args,**kwargs)
        end_time = time.time()
        seconds = end_time - start_time
        print('该函数执行了{}秒'.format(seconds))
        return add_result
    return wrapper

@timer
def add_func(a,b):
    print('函数开始！')
    time.sleep(1)
    print('函数结束！')
    return a+b


result = add_func(6,7)
print(result)


























