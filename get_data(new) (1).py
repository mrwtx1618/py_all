# import redis
import urllib.request
import csv
import pandas as pd
import datetime
import xlwt
import time
import numpy as np



def import_keyvalue():#stockcode->key return dict#这个程序现在是导入key_value
    f=open('key_value.csv','r')
    reader=csv.reader(f)
    keydic={}
    for line in reader:
        keydic[line[0]]=line[1]
    f.close()
    return keydic

def Token():#get token
    url ='http://gw.yundzh.com/token/access?appid=dcdc435cc4aa11e587bf0242ac1101de&secret_key=InsQbm2rXG5z'
    f = urllib.request.urlopen(url)
    f=f.read()
    f=eval(f)
    token=f['Data']['RepDataToken'][0]['token']
    return token

def timetran(t):#timestamp->'yyyymmdd'
    timeStamp = t
    timeArray = time.localtime(timeStamp)
    t = time.strftime("%Y%m%d", timeArray)
    return t

def request_data(url):#request url for data
    for count in range(10):
        try:
            url=url+Token()
            response=urllib.request.urlopen(url)
            html=response.read()
            json_table=eval(html)
            data_json=json_table['Data']['JsonTbl']['data'][0][0]['data'][0][1]['data']
            data=[[timetran(x[0]),x[1]] for x in data_json]
            judge=judge_condition(data)
            if judge:
                return data
            else:
                return False
        except Exception as e:
            if count==9:
                print(e)
                return False
            else:
                continue

def judge_Tingpai(stock):
    url='http://gw.yundzh.com/stkdata?obj=%s&field=ShiFouTingPai&token=%s'%(stock,Token())
    response=urllib.request.urlopen(url)
    html=response.read()
    json_table=eval(html)
    try:
        flag=json_table['Data']['RepDataStkData'][0]['ShiFouTingPai']
    except:
        print(url+Token())
        return False
    if flag:
        return True
    else:
        return False





def judge_condition(data):
    if len(data)<30:
        return False
    first_day=data[0][0]
    last_day=data[-1][0]
    time_delta=datetime.timedelta(55)
    now_day=today
    formal_day=now_day-time_delta
    now_day=str(now_day)[:10].replace('-','')
    formal_day=str(formal_day)[:10].replace('-','')
    if first_day<formal_day:
        print ('stop too long')
        return False
    return True

def calculate_vol3(data_chengjiaoe):
    chengjiaoe_3=sum([x[1] for x in data_chengjiaoe[-3:]])
    n=4
    chengjiaoe_n=sum([x[1] for x in data_chengjiaoe[-n:]])
    chengjiaoe_30=sum([x[1] for x in data_chengjiaoe])
    vol3=chengjiaoe_n/chengjiaoe_30*10
    return chengjiaoe_n,chengjiaoe_30,vol3

def calculate_zijin(stock,begin_time,recent_30_marketing_day,chengjiaoe_30):
    url_dadan='http://gw.yundzh.com/quote/l2stat?obj=%s&field=ShiJian,DaDanJingLiuRuJinE&begin_time=%s-000000-000-0&token='%(stock,begin_time)
    data_dadan=request_data(url_dadan)
    if data_dadan==False:
        print(url_dadan)
        return False,False,False
    data_dadan=[x for x in data_dadan if x[0] in recent_30_marketing_day]
    dadan_30=sum([x[1] for x in data_dadan])
    zijin=chengjiaoe_30/dadan_30
    zijinT=dadan_30/chengjiaoe_30
    return dadan_30,zijin,zijinT

# def calculate_effect(stock,begin_time,now_day,m):
#     key='effect:%i'%int(keydic[stock])
#     dic=r.hgetall(key)
#     effect_data=[[a.decode('utf-8'),b.decode('utf-8')] for a,b in dic.items()]
#     effect_data= sorted(effect_data,key=lambda d:float(d[0]), reverse = True)
#     all_time=[x[0] for x in effect_data]
#     try:
#         now_id=all_time.index(begin_time)
#         n_days_data=effect_data[:now_id+1]
#         formalm_days_data=n_days_data[-m:]
#         n_days_avg=sum([float(x[1]) for x in n_days_data])/len(n_days_data)
#         formal_m_days_avg=sum([float(x[1]) for x in formalm_days_data])/m
#         return n_days_avg,formal_m_days_avg,formal_m_days_avg/n_days_avg
#     except Exception as e:
#         print(e)
#         return 0,0,0

def get_name(stock):
    url='http://gw.yundzh.com/stkdata?obj=%s&field=ZhongWenJianCheng&token=%s'%(stock,Token())
    response=urllib.request.urlopen(url)
    html=response.read()
    json_table=eval(html)
    try:
        name=json_table['Data']['RepDataStkData'][0]['ZhongWenJianCheng']
    except:
        print (stock,'name wrong')
        name='ST'
    if 'ST' in name:
        return False
    return name

def get_data(stock):
    if judge_Tingpai(stock):
        print(stock,'stop today')
        return False
    #get ZhongWenJianCheng
    name=get_name(stock)
    if name==False:
        print(stock,'ST')
        return False
    url_chengjiaoe='http://gw.yundzh.com/quote/kline?obj=%s&start=-30&field=ShiJian,ChengJiaoE&period=1day&token='%(stock)
    data_chengjiaoe=request_data(url_chengjiaoe)
    if data_chengjiaoe==False:
        print(stock,False)
        return False

    recent_30_marketing_day=[x[0] for x in data_chengjiaoe]


    chengjiaoe_3,chengjiaoe_30,vol3=calculate_vol3(data_chengjiaoe)

    #judge begin_time
    time_delta=datetime.timedelta(55)
    now_day=today
    formal_day=now_day-time_delta
    begin_time=str(formal_day)[:10].replace('-','')

    chengjiaoe_20=sum([x[1] for x in data_chengjiaoe[-20:]])
    dadan_30,zijin,zijinT=calculate_zijin(stock,begin_time,recent_30_marketing_day[-20:],chengjiaoe_20)
    if dadan_30==False:
        return False

    #calculate effect
    begin_time=recent_30_marketing_day[0]
    n_days_avg,formal_3_days_avg,effect_3=calculate_effect(stock,begin_time,now_day,3)
    n_days_avg,formal_5_days_avg,effect_5=calculate_effect(stock,begin_time,now_day,5)
    return stock,name,formal_3_days_avg,formal_5_days_avg,n_days_avg,effect_3,effect_5,chengjiaoe_30,dadan_30,zijin,zijinT,vol3,chengjiaoe_3

def rank(data):
    frame=data.copy()
    frame['rankA']=frame['zijinT'].rank(ascending=False)
    frame['rankB']=frame['vol'].rank(ascending=False)
    frame['rankC']=frame['effect_3'].rank(ascending=False)
    return frame

def get_300_500_data(frame):
    hs300_stocks=np.genfromtxt('300.txt','str')
    zz500_stocks=np.genfromtxt('500.txt','str')
    hs300_data=frame.loc[[x for x in hs300_stocks if x in frame.index]]
    zz500_data=frame.loc[[x for x in zz500_stocks if x in frame.index]]
    return hs300_data,zz500_data

def save_excel(all_data,hs300_data,zz500_data):
    writer=pd.ExcelWriter('%sdata.xlsx'%name_by_time)
    all_data.to_excel(writer,sheet_name='all')
    hs300_data.to_excel(writer,sheet_name='hs300')
    zz500_data.to_excel(writer,sheet_name='zz500')
    writer.save()

def add_rate(stock):
    rate=stock['chengjiaoe_3']
    rate=[float(x)/sum(rate) for x in rate]
    rate=correct_rate(rate)
    stock['rate']=rate
    return stock

def correct_rate(rate):
    if len(rate)<20:
        return rate
    surplus=0.0
    num=len(rate)
    largenum=0
    for i,value in enumerate(rate):
        if value>0.05:
            largenum+=1
            surplus+=value-0.05
            rate[i]=0.05
    smallnum=num-largenum
    distr=surplus/smallnum
    for i,value in enumerate(rate):
        if value<0.05:
            rate[i]+=distr
    flag=len([x for x in rate if x>0.05])
    if flag:
      return correct_rate(rate)
    else:
      return rate




def get_stocks(filename):
    all_data=pd.read_excel(filename,sheetname=0)
    HS300_data=pd.read_excel(filename,sheetname=1)
    ZZ500_data=pd.read_excel(filename,sheetname=2)

#sg200
    sg200=all_data.sort_values('rankA')
    sg200=sg200[:450]
    sg200=sg200.sort_values('rankC')
    sg200=sg200[:200]
    sg200=sg200[['zhongwenjiancheng','chengjiaoe_3']]

#sg50
    sg50=all_data.sort_values('rankA')
    sg50=sg50[:200]
    sg50=sg50.sort_values('rankC')
    sg50=sg50[:50]
    sg50=sg50[['zhongwenjiancheng','chengjiaoe_3']]

#sgm50_all
    sgm50_all=all_data.sort_values('rankB')
    sgm50_all=sgm50_all[:200]
    sgm50_all=sgm50_all.sort_values('rankA')
    sgm50_all=sgm50_all[:50]
    sgm50_all=sgm50_all[['zhongwenjiancheng','chengjiaoe_3']]

#sgm50_hs300
    sgm50_hs300=HS300_data.sort_values('rankB')
    sgm50_hs300=sgm50_hs300[:100]
    sgm50_hs300=sgm50_hs300.sort_values('rankA')
    sgm50_hs300=sgm50_hs300[:30]
    sgm50_hs300=sgm50_hs300[['zhongwenjiancheng','chengjiaoe_3']]

#sgm50_zz500
    sgm50_zz500=ZZ500_data.sort_values('rankB')
    sgm50_zz500=sgm50_zz500[:180]
    sgm50_zz500=sgm50_zz500.sort_values('rankA')
    sgm50_zz500=sgm50_zz500[:50]
    sgm50_zz500=sgm50_zz500[['zhongwenjiancheng','chengjiaoe_3']]

#gold1
    gold1=all_data.sort_values('rankB')
    gold1=gold1[:int(0.382*len(gold1))]
    gold1=gold1.sort_values('rankA')
    gold1=gold1[:int(0.382*len(gold1))]
    gold1=gold1.sort_values('rankC')
    gold1=gold1[:int(0.382*len(gold1))]
    gold1=gold1[['zhongwenjiancheng','chengjiaoe_3']]

#add_rate
    writer=pd.ExcelWriter('%sstock.xlsx'%name_by_time)
    stock_list=[sg200,sg50,sgm50_all,sgm50_hs300,sgm50_zz500,gold1]
    name_list=['sg200','sg50','sgm50_all','sgm50_hs300','sgm50_zz500','gold1']
    dic=dict(zip(name_list,stock_list))
    for stock in name_list:
        stock_result=add_rate(dic[stock])
        stock_result.to_excel(writer,sheet_name=stock)
    writer.save()






if __name__=='__main__':
    # r=redis.Redis(host='localhost',port=16379,db=1)
    keydic=import_keyvalue()
    stocks=[stockcode for stockcode,key in keydic.items()]
    today=datetime.datetime.now()
    data=map(get_data,stocks)
    temp=zip(stocks,data)
    tempdict=dict((name,value) for name,value in temp)
    col_name=['stock','zhongwenjiancheng','formal_3_days_avg','formal_5_days_avg','n_days_avg','effect_3','effect_5','chengjiaoe_30','dadan_20','zijin','zijinT','vol','chengjiaoe_3']
    frame=pd.DataFrame(tempdict).T
    frame=frame.drop(frame[frame[0]==False].index)
    frame.columns=col_name
    del frame['stock']
    all_data=frame.copy()
    hs300_data,zz500_data=get_300_500_data(all_data)
    all_data=rank(all_data)
    hs300_data=rank(hs300_data)
    zz500_data=rank(zz500_data)
    name_by_time=str(today)[:10]
    save_excel(all_data,hs300_data,zz500_data)
    get_stocks('%sdata.xlsx'%name_by_time)
