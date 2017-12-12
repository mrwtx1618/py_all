#encoding:utf-8
import pandas as pd
import os
import xlrd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
path = os.getcwd()             #打印该py文件当前的路径
filenames = os.listdir(path)   #该路径下所有的文件名
filenames_list = []
for filename in filenames:
	if filename.endswith('.xlsx'):
		filenames_list.append(filename)
ultimate_list = []
highest_ratio_list = []
r_list = []
for x in filenames_list:
	data = xlrd.open_workbook('%s'%x)
	table = data.sheets()[0]
	ultimate_ratio = table.cell_value(1,10)
	recommend_ratio = table.cell_value(1,7)
	target_ratio = table.cell_value(1,15)
	if target_ratio != 1:
		if ultimate_ratio < 0:
			recommend_ratio = table.cell_value(1,7)
			r = 0.0453/recommend_ratio
			r_list.append(r)
plt.plot(r_list,'ro')
xmajorLocator = MultipleLocator(20)
ymajorLocator = MultipleLocator(0.5)
yminorLocator = MultipleLocator(0.1)
plt.xlabel("numbers of stocks ")
plt.ylabel('0.0453/recommend')
plt.show()
			
# 	r = 0.0453/recommend_ratio
# 	r_list.append(r)
# print r_list		
# 	frame=pd.read_excel('%s'%x)
# 	frame_list.append(frame)
# 	data = xlrd.open_workbook('%s'%x)
# 	table = data.sheets()[0]
# 	lowest_percentage = table.cell_value(1,9)
# 	lowest_percentage_list.append(lowest_percentage)
# 	lowest_percentage_list.sort(reverse=False)
# 	stop_loss_point_list = [i - 0.0000000000001 for i in lowest_percentage_list]#################################
# 	highest_ratio = table.cell_value(1,15)
# 	highest_ratio_list.append(highest_ratio)
# 	highest_ratio_list.sort(reverse=True)         #没有去掉1 不应该去掉1
# 	#highest_ratio_list = [a for a in highest_ratio_list if a!=1.0] #去掉了所有的1################################
# # print highest_ratio_list
# # print stop_loss_point_list
# for m in range(len(highest_ratio_list)):
# 	for n in range(len(stop_loss_point_list)):
# 		sum_stop_win_list = []
# 		sum_stop_loss_list = []
# 		sum_ultimate_list = []
# 		sum_all_list = []
# 		for j in range(629):
# 			for i,value in frame_list[j].iterrows():
# 				if value[u'每日相对第一天最高涨幅'] > (value[u'目标涨幅'] * highest_ratio_list[m]):
# 					sum_stop_win_list.append(value[u'目标涨幅'] * highest_ratio_list[m])
# 					#print sum_stop_win_list
# 					break
# 				if value[u'每日相对第一天最大跌幅'] < stop_loss_point_list[n]:
# 					sum_stop_loss_list.append(stop_loss_point_list[n])
# 					break
# 			else:
# 				sum_ultimate_list.append(value[u'最终涨跌幅'])
# 		sum_all_list = sum_stop_win_list + sum_stop_loss_list + sum_ultimate_list
# 		sort_list.append([sum(sum_all_list),highest_ratio_list[m],stop_loss_point_list[n]])
# sort_list.sort(key=lambda x:x[0],reverse = True)
# print sort_list
