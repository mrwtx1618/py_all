# -*- coding:UTF-8 -*-
import xlrd
import os
import pandas as pd
path = os.getcwd()             #得到该py文件当前的目录
filenames_path = os.listdir(path)   
frame = pd.DataFrame()
filenames_list =[]
for filename in filenames_path:
	filenames_list.append(filename)
for x in filenames_list:
	data = xlrd.open_workbook('%s'%x)
	print x
	table = data.sheets()[0]
	cell = table.cell(1,14)
print cell