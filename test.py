# -*- coding:UTF-8 -*-
# from IPython.display import HTML
# import numpy as np
# I = np.linspace(0,1,11)
# print I
# print id(123)
# print"Let's go"       #这时候会用到双引号来定义字符串 
# print "Let's \"go\""  #如果双引号里还有双引号，那么需要用到转义符
# mail = 'Tom:\n Hello!\nI am Jack'#换行：\n
# print mail
# a = 'abcde'
# print a[1:4]          #切片操作
# print a[4:]
# print a[:4]
# print a[:-1]
# print a[-1:]
# print a[::1]         #控制步长
# print a[::2]         #两步一取
# print a[::-1]        #倒序，表示从右向左一个一个取
# print a[3:0:-1]
# print a[:]
# print a[::]
# b = '12345'
# print a + b          #拼接字符串
# print b * 5          #使字符串重复出现5次
# print '5' in b       #in函数
# print '9' in b
# print max(b)
# print min(b)
# t = ('Tom',16,'male') #定义了一个tuple类型，tuple类型是不可变的
# print t[0],t[1],t[2]
# t = (2,)              #定义单一元素的元组，要打一个括号
# print type(t)
# t = ('Tom',16,'male')
# name,age,gender = t
# print name
# a,b,c = 1,2,3
# print a,b,c
# list_Tom = ['Tom',30,'male']
# list_Tom.append('65652651')  #append方法
# print list_Tom
# list_Tom.remove('65652651')
# print list_Tom
# t1 = ['name','age','gender']
# t2 = ['Tom',16,'male']
# t = zip(t1,t2) #从两个列表中依次取值，组成一个新的列表
# print t
# print type(t[1]) #这里面每一个是一个tuple类型
# dic1 = {name:'Tom','age':25,'gender':'male'} #定义字典，用冒号
# print type(dic1)
# print dic1[name],dic1['age'],dic1['gender'] #
# print dic1
# for k in dic1:
# 	print k   #打印字典的key
# for k in dic1:
# 	print dic1[k] #打印字典的value
# dic1['Cell Number'] = '13611835757' #往字典里增加一个值
# print dic1
# del(dic1['Cell Number']) #del是一个系统函数，
# print dic1
# dic1.pop('age') #删除字典里age这个字段
# print dic1
# print dic1.get('age','error') #字典下面get方法，如果有age这个key，那么取出来，如果没有，报error
# print not(0) #逻辑否
# for x in 'abcd': #序列包括了字符串，元组，列表
# 	print x,'hello'
# print range(1,10,2) #第三个参数为步长
# print xrange(1,10,2) #xrange返回的是一个迭代对象，看不见那个list，比较节省内存
# d = {1:111,2:222,3:333,4:444,5:555,6:666}
# for k in d:
# 	print k #这样取出的是字典的key
# 	print d[k] #这样可以根据key来得到字典的values
# 	print d.items() #得到一个包含着tuple的list
# a,b,c,d,e = (1,2,3,4,5) #利用这种办法可以拆分一个tuple
# print a

# # for k,v in d.items():#字典有items方法 
# # 	print k
# # 	print v
# formatter = '%r %r %r %r'
# print formatter %(1,2,3,4)
# import pyalgotrade
# import bcolz
# import zipline
# print abs
# print callable(abs) #测试一个函数是否被定义
# lst = []
# print isinstance(lst, list) #判断lst是不是一个list
# print cmp('12345', '12345') #用来比较两个字符串是否一样，一样返回0
# print type(range(10))
# print type(xrange(10)) #xrange类型，效率更高
# s = 'fsjdkfljlsfk;ls'
# print str.capitalize(s) #字符串函数，把首字母大写，是str类当中的一个方法，字符串是一个大的类别
# print s.capitalize() #字符串是一个大的类别，下面有capitalize这个方法
# print s.replace('fs', 'gg')
# ss = '123123123'
# print ss.replace('1', 'x') #把1全部替换成x
# print ss.replace('1', 'x', 2) #替换两次
# print ss.split('3')
# ip = '192.168.168.1'
# print ip.split('.') #返回了一个list，并且以.作为分隔
# print ip.split('.',2)
#用filter函数+lambda函数返回一个list中大于0的值
# lst = [1,2,3,4,-7,0,7.6,-0.8,-8,-0.11,0.123]
# print filter(lambda x: x > 0, lst)
# import string
# # import Brownian_motion
# import myadd
# x = myadd.jia(3,4) #发现如果模块有下划线就会失效,调用
# print x
#结果发现当这个函数调用myadd这个模块时，里面的打印print __name__这个语句并没有执行
#只有在运行myadd这个模块本身时才会执行print__name__这样一句语句
#当其他模块调用myadd这个py文件时，程序并不会执行__name__这一句话
#根据这样一个特点，就可以对程序进行一些改造
# import zipline
# print __name__ #python当中的内置属性
# 如果有很多函数要经常被调用的话，就可以把他们封装到一个模块中
# 然后通过调用模块的方式去导入这些函数，这是模块开发的主旨
import re #如果在python中想使用正则表达式的话，要加载re模块
# s = r'abc' #这就相当于制订了一个规则
# result1 = re.findall(s, 'sssssssssssssab') #这里s是规则
# result2 = re.findall(s, 'ssssssssssssssabc')
# result3 = re.findall(s, 'ssssssssssabcabcabc')
# print result1
# print result2
# print result3
# # 通过普通字符匹配的规则
# st = 'top tip tqp twp tep tcp'
# reg1 = r't[oiw]p' #[]可以匹配一个字符集，表示这里面只要有一个字母满足就可以
# result4 = re.findall(reg1, st)
# print result4
# reg2 = r't[^oiw]p' #尖角号^表示除了oiw以外的字母
# result5 = re.findall(reg2, st)
# print result5
###方括号中出现元字符的话，元字符不起作用
###方括号中[0-9]就表示[0123456789]

#################################正则表达式中^的用法，表示找是否有开头的匹配################################
# s = 'world, hello boy!'
# reg1 = r'hello'
# reg2 = r'^hello' #这个字符的开头并没有hello，所以第二个结果是空
# print re.findall(reg1, s)
# print re.findall(reg2, s)
############################################################################################################

###############################美元$的用法，表示字符的末尾匹配#########################################
s = 'boy, good job boy'
reg1 = r'boy'
reg2 = r'boy$' #s这个字符的末尾有boy这个单词，所以第二个结果能返回一个boy
print re.findall(reg1, s)
print re.findall(reg2, s)

