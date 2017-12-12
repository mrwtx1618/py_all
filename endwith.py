# -*- coding:UTF-8 -*-
import csv
import os
import xlrd
s = 38.0376719457
l = 15.7912997439
path = os.getcwd()             #打印该py文件当前的路径
filenames = os.listdir(path)   #该路径下所有的文件名
filenames_list = []
sum1 = 0
positive_sum = 0
negative_sum = 0
for filename in filenames:
	if filename.endswith('.xlsx'):
		filenames_list.append(filename)
highest_to_target_ratio_list_with_names=[]
highest_to_target_ratio_list=[]
lowest_percentage_list = []
for x in filenames_list:
	data = xlrd.open_workbook('%s'%x)
	table = data.sheets()[0]
	deal_percentage = table.cell_value(1,14)      #这个里面是有正有负的
	if deal_percentage > 0:
		deal_percentage_positive = deal_percentage
		positive_sum = positive_sum +deal_percentage
		#print deal_percentage_positive
	else:
		deal_percentage_negative = deal_percentage
		negative_sum = negative_sum + deal_percentage
		#print deal_percentage_negative
	h_to_t_ratio = table.cell_value(1,15)
	highest_to_target_ratio_list.append(h_to_t_ratio)
	highest_to_target_ratio_list_with_names.append([h_to_t_ratio,x])  #加入比例系数以及文件名，加入文件名为了定位比例系数
	sum1 = sum1 + deal_percentage
	lowest_percentage = table.cell_value(1,9)
	lowest_percentage_list.append([lowest_percentage,x])
lowest_percentage_list.sort(key = lambda x:x[0], reverse= False)      #把跌幅排序
lowest_percentage_list_names = [i[1] for i in lowest_percentage_list] #取出股票名
drop_range = [i[0] for i in lowest_percentage_list]
stop_loss_point_list = [i - 0.0001 for i in drop_range]            #设定止损点
print stop_loss_point_list
# print drop_range
# print lowest_percentage_list_names
# print lowest_percentage_list
highest_to_target_ratio_delete_ones_list_with_names = [x for x in highest_to_target_ratio_list_with_names if x[0]!=1.0]     #把所有的1去掉 带股票名
highest_to_target_ratio_delete_ones_list_with_names.sort(key=lambda x:x[0],reverse = True)                                   #排序,按照第一个指标
highest_to_target_ratio_list_delete_ones = [x for x in highest_to_target_ratio_list if x!=1.0]                              #把所有的1去掉 不带股票名
highest_to_target_ratio_list_delete_ones.sort(reverse = True)              #排序
r_list = highest_to_target_ratio_list_delete_ones                              #把这个命名为r_list 已经排序好了
print r_list
# highest_to_target_ratio_delete_ones_list_with_names_without_Rs_list = [i[1] for i in highest_to_target_ratio_delete_ones_list_with_names]    #定义了所有的最高价没有到目标价的股票名，按照比例系数从大到小排列
# f_percentage_list=[]
# t_percentage_list=[]
# for x in highest_to_target_ratio_delete_ones_list_with_names_without_Rs_list:
# 	data = xlrd.open_workbook('%s'%x)
# 	table = data.sheets()[0]
# 	f_percentage = table.cell_value(1,14)
# 	f_percentage_list.append(f_percentage)                                          #定义出了要减去的每一个原来的要按最终价处理的list
# 	t_percentage = table.cell_value(1,7)
# 	t_percentage_list.append(t_percentage)
# f_all_i = 0
# t_all_i = 0
# f_all_i_list=[]
# t_all_i_list=[]
# s_all = 0

# s_all=[(s-sum(f_percentage_list[:i+1])+sum(t_percentage_list[:i+1]))*r_list[i]-l for i in range(30)]
# print [sum(f_percentage_list[:i+1]) for i in range(30)]
# print [sum(t_percentage_list[:i+1]) for i in range(30)]
# print [r_list[i] for i in range(60)]
# #s_all.sort()
# print s_all
# #for i in range(10):
# #	f_all_i = f_all_i + f_percentage_list[i]
# #	f_all_i_list.append(f_all_i)
# # 	t_all_i = t_all_i + t_percentage_list[i]
# # 	t_all_i_list.append(t_all_i)
# # 	#s_all = s - f_all_i_list[i]
# # 	#print s_all
# #print f_all_i_list

# #print highest_to_target_ratio_delete_ones_list_with_names_without_Rs_list
# 	#print f_percentage[i]
# #print t_percentage_list	
# #print t_percentage
# #print f_percentage_list
# #print r[0]
# #print highest_to_target_ratio_delete_ones_list_with_names
# #print highest_to_target_ratio_list_delete_ones
# print sum1
# print positive_sum
# print negative_sum
# #print s
# #for r in highest_to_target_ratio_delete_ones_list:
# #	sum_multiplied_r = positive_sum * r
# #	print sum_multiplied_r
# #print len(highest_to_target_ratio_delete_ones_list) =388  629只股票里有388只未到目标价
# #print "%.2f%%"%((sum/10)*100)