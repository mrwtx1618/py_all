#encoding:utf8
import numpy as np
print(np.sum([[0,1,2],[3,4,5],[6,7,8]]))#不加axis参数就把0,1,2,3,4,5,6,7,8全都相加
print(np.sum([[0,1,2],[3,4,5],[6,7,8]],axis=0))#axis = 0是按列相加
print(np.sum([[0,1,2],[3,4,5],[6,7,8]],axis=1))#axis = 1是按行相加












