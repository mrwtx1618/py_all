# -*- coding:UTF-8 -*-
class Ren:
	name = '人'
	height = '一人高'
	weight = '一人重'

	def run(self):
		print '跑步'
if __name__ == '__main__':
	Tom = Ren() #Tom是Ren的一个实例
	print Tom 
	Tom.name = 'Tom' #对这个属性进行赋值
	Tom.money = '10000' #本来定义时没有这个属性
	print Tom.name,Tom.height,Tom.weight
	print Tom.money
# print Tom.run()