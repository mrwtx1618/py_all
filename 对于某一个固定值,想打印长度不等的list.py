#encoding:utf8
list_1 = [1,2,3,4,5]
list_2 = [1,2,3]
list_3 = [1,2,3,4,5,6,7]
list_4 = [1,2,3,4,5,6,7,8]
list_5 = [1]
list_all = []
list_all.append(list_1)
list_all.append(list_2)
list_all.append(list_3)
list_all.append(list_4)
list_all.append(list_5)

#现在想实现的功能是只打印每个list的前5个,如果不足5个,那么有几个打印几个
#发现python里面直接取[:5]就好
for single_list in list_all:
    single_list_5 = (single_list[:5])
    print('the list is',single_list_5)




































