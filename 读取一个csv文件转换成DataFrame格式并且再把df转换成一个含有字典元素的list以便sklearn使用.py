#encoding:utf8
import pandas as pd
#读取一个csv文件转换成DataFrame格式再把df转换成一个含有字典元素的list以便sklearn使用
#并且再把df转换成一个含有字典元素的list以便sklearn使用
df = pd.read_csv('601766.csv')

dict_list = df.to_dict(outtype = 'records')
print type(dict_list)
print dict_list[1]



















