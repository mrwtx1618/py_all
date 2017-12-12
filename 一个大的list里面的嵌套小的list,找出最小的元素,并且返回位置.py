#encoding:utf-8
list_1 = [1,2,3,4,5,7,8]
list_2 = [6,7,8,9,10,0.4,5,6,7]
list_3 = [11,12,13,14,15,34]
list_4 = [16,17,0.034,18]
list_5 = [21,22,23,0.01,24,25,1.1,2,3,4,7]
list_6 = [26,27,28,29,30,6,2,1.2]

list_all = []
list_all.append(list_1)
list_all.append(list_2)
list_all.append(list_3)
list_all.append(list_4)
list_all.append(list_5)
list_all.append(list_6)
#现在想在list_all里面找最小的3个值,哪个算法最快？并且要找出最小的3个值的位置
smallest_listed_all = []
for single_list in list_all:
    single_list_sorted = sorted(single_list)
    single_smallest = single_list_sorted[0]
    smallest_listed_all.append(single_smallest)
    smallest_listed_all_sorted = sorted(smallest_listed_all)
    the_min = smallest_listed_all_sorted[0]
#######################################################################
for single_list in list_all:
    for value in single_list:
        # print(value)
        if value == the_min:
            print(the_min)
            print(list_all.index(single_list))
            print(single_list.index(the_min))

#找出了0.01这个值以后,实际上0.01这个值通过两个list算出来的,现在想通过(4,3)这个位置来找到原来的那个list
#根据算法(4,3)说明最小值出现在原来的大的list里面的第5个小的List里面的第4个元素
#对应到寻找相似K线的算法,加入返回了(m,n),则是第m(或者是第m+1)个collection里面的price_list_of_list的第n+1个List生成的