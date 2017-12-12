#encoding:utf8
#zip函数接受任意多个序列(包括0个和1个)作为参数，返回一个tuple列表

x_list = [1,2,3]
y_list = [4,5,6]
z_list = [7,8,9]

xyz = zip(x_list,y_list,z_list)
print xyz

x = [1,2,3]
y = [4,5,6,7]
xy = zip(x,y)
print xy


a = [1,2,3,4,5,6,7]
print zip(a)

b = []
print zip(b)



