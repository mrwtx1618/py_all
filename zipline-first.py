# -*- coding:UTF-8 -*-
#Every zipline algorithm consists of two funtions you have to define
#initialize(context)
#handle_data(context, data)
import zipline
from zipline.examples import buyapple
from zipline.api import order,record,symbol #We first have to import some functions we would like to use.
def initialize(context):
	pass
def handle_data(context,data):
	order(symbol('APPL'),10) #order()which takes two argument:a security object, and a number specifying how many stocks you would like to order(if negative,order() will sell/short stocks)
	record(APPL = data.current(symbol('APPL'),'price')) #record() function allows you to save the value of a variable at each iteration. 
