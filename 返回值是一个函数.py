#encoding:utf8
#函数的返回值是一个函数


def outer_func():
    def inner_func():
        print('This sentence is in the inner_func!')
    return inner_func()
outer_func()




















