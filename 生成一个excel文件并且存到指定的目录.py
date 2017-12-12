#encoding:utf8
#本程序想要生成一个xlsx文件并且存到指定的文件夹，而不是存到该py文件所在的目录
import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randn(3,3))
df.to_excel('C:/Users/Administrator/Desktop/PY_ALL/test_excel_path/aaaaaaaaaaaaaa.xlsx') #'C:\Users\Administrator\Desktop\PY_ALL\test_excel_path\aaa.xlsx'























