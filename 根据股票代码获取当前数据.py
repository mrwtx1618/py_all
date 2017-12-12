#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import re
import datetime
 
def getStockInfo(url):
    """����url��ȡ��Ϣ"""
    stockList = []
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
 
    stockStr = response.read()
    stockList = stockStr.split(',')
    return stockList
 
def printStock(List):
    """��ӡ�����Ϣ"""
    print '***********price*****************' + List[1]
    print '***********float_price***********' + List[2]
    print '***********float_perct***********' + List[3] + '%'
    print '***********succ_unit*************' + List[4]+' shou'
    print '***********succ_price************' + List[5]
 
def getUrlByCode(code):
    """���ݴ����ȡ��ϸ��url"""
    url = ''
    stockCode = ''
    if code == 'sh':
        url = 'http://hq.sinajs.cn/list=s_sh000001'
    elif code == 'sz':
        url = 'http://hq.sinajs.cn/list=s_sz399001'
    elif code == 'cyb':
        url = 'http://hq.sinajs.cn/list=s_sz399006'
    else:
        pattern = re.compile(r'^60*')
        match = pattern.match(code)
        if match:
            stockCode = 'sh'+ code
        else:
            stockCode = 'sz' + code
        url = 'http://hq.sinajs.cn/list=s_'+stockCode
 
    return url
 
 
#����stock���������Ӧ�ļ۸���Ϣ
#code = raw_input('code: ')
codeDict = {
    'sh'     : 'shang hai zq',
    'sz'     : 'shen zheng zq',
    'cyb'    : 'chang ye ban',
    '601788' : 'guang da zheng quan',
    '000651' : 'ge li dian qi',
}
 
#http://hq.sinajs.cn/list=s_sh000001 (�Ϻ����̲�ѯ)
#http://hq.sinajs.cn/list=s_sz399001 (���ڴ��̲�ѯ)
 
count = 0;
while (count<=100):#ѭ��100�κ����˳�
    # ѭ���ֵ�
    for key in codeDict:
        print key + '--'+codeDict[key]
 
    code = raw_input('please select a code: ')
    now_time = datetime.datetime.now()
 
    #��ӡ��code����Ϣ
    url = getUrlByCode(code)
    stockInfo = getStockInfo(url)
    #print stockInfo
    printStock(stockInfo)
 
    end_time = datetime.datetime.now()
    costTime =  (end_time - now_time).seconds
    print '�ܹ�����ʱ��'+str(costTime)+'��'
    count +=1