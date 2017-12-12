#encoding:utf8
import random
import matplotlib
import matplotlib.pyplot as plt

def rollDice():
	roll = random.randint(1, 100) #1到100之间的随机整数
	if roll == 100:
		# print roll,'roll is 100,you lose, what are the odds!!!'
		return False
	elif roll <=50:
		# print roll,'roll is 1-50,you lose,play again!'
		return False
	elif 50 < roll < 100:
		# print roll,'roll is 1-50,you win，play more！'
		return True
	return roll


def martingale_strategy(funds, initial_wager, wager_count):
	value = funds
	wager = initial_wager
	
	wX = []
	vY = []

	current_wager = 1 #current_wager是参与赌博的次数

	while current_wager <= wager_count and value > 0:
		if rollDice() == False:
			value = value - wager
			wX.append(current_wager)
			vY.append(value)
			wager = wager * 2
		else:
			value = value + wager
			wX.append(current_wager)
			vY.append(value)
		current_wager = current_wager + 1
		
	# if value < 0:
	# 	break
	print 'Funds',value,current_wager
	plt.plot(wX,vY)
x = 0
while x < 5: #这个5表示生产曲线的条数
	martingale_strategy(100000, 10, 50) #第一个参数表示
	x += 1

plt.axhline(0,color = 'r') #画一条水平的0线作为财产为0的线
plt.xlabel('wager_count')
plt.ylabel('account value')
plt.show()


































