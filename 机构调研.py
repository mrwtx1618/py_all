# coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time
from requests.exceptions import ChunkedEncodingError

MONGO_HOST = 'localhost' #本地主机
MONGO_PORT = 27017 #mongodb采用的是27017端口
conn=pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
db=conn.crawls #db is a DataBase,<class 'pymongo.database.Database'>
COLLECTION_SH_ANON = 'sh_anon' #上交所公告
COLLECTION_SZ_ANON = 'sz_anon' #深交所公告
COLLECTION_LHB = 'lhb' #龙虎榜
COLLECTION_XSJJ = 'xsjj' #限售解禁榜
COLLECTION_GGZC = 'ggzc' #高管增持
COLLECTION_JGDY='jgdy' #机构调研
COLLECTION_DZJY='dzjy' #大宗交易

today = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# def _before_sleep():
#     time.sleep(60)

# 上交所公告
# def announcement_SH():
#     try:
#         _before_sleep()
#         SH_URL = 'http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc_2016openpdf.htm'
#         session=requests.session()
#         url=SH_URL
#         req=session.get(url)
#         html=req.content.decode('utf-8')
#         soup=BeautifulSoup(html,'lxml')
#         data=soup.find_all('em')
#         data=[x.a for x in data]
#         data=[{'url':x['href'],'title':x['title'],'code':x.get_text().split('：')[0],'updateTime':today} for x in data]
#         for item in data:
#             result=db[COLLECTION_SH_ANON].update_one({'title':item['title']},{'$set':item},upsert=True)
#         return data
#     except Exception as e:
#         print(e)

# 深交所公告
# def announcement_SZ():
#     try:
#         _before_sleep()
#         SZ_URL='http://disclosure.szse.cn//disclosure/fulltext/plate/szlatest_24h.js?'
#         dns='http://disclosure.szse.cn/'
#         session=requests.session()
#         url=SZ_URL
#         req=session.get(url)
#         req.encoding='gbk'
#         html=req.text.split('=')[1].replace(';','')
#         data=json.loads(html)
#         data = [{'url': dns+x[1], 'title': x[2], 'code':x[0],'updateTime':today} for x in data]
#         for item in data:
#             result=db[COLLECTION_SZ_ANON].update_one({'title':item['title']},{'$set':item},upsert=True)
#         return data
#     except Exception as e:
#         print(e)
# announcement返回格式如下
# {'code': '002252', 'url': 'http://disclosure.szse.cn/finalpage/2016-11-29/1202846741.PDF', 'title': '上海莱士：关于召开2016年第三次临时股东大会的通知'}

# 龙虎榜
# def longhu():
#     #_before_sleep()
#     try:
#         LONGHU_URL='http://data.10jqka.com.cn/market/longhu/'
#         session=requests.session()
#         url=LONGHU_URL
#         req=session.get(url)
#         html=req.content
#         soup=BeautifulSoup(html,'lxml')
#         longhu_data=soup.find('tbody',class_='m_tbd')
#         longhu_data=longhu_data.find_all('tr')
#         data=list()
#         for code_data in longhu_data:
#             trigger=code_data.find_all('td',class_='tip-trigger')
#             code,jian_cheng=[x.get_text().replace('\n','') for x in trigger]
#             jie_du=code_data.find('a',charset='gbk').get_text()
#             if  '知名营业部' in jie_du:
#                 jie_du='游资'
#             elif '机构介入' in jie_du:
#                 jie_du='机构'
#             elif '敢死队' in jie_du:
#                 jie_du='敢死队'
#             else:
#                 continue
#             mai_ru_zhan_bi=code_data.find('td',class_='c-rise').get_text()
#             mai_chu_zhan_bi=code_data.find('td',class_='c-fall').get_text()
#             jing_mai_ru_e = code_data.find_all('td',class_='c_eq')[1].get_text()
#             result=dict()
#             result['code']=code
#             result['stockBrief']=jian_cheng
#             result['explanation']=jie_du
#             result['buyProportion']=mai_ru_zhan_bi
#             result['sellProportion']=mai_chu_zhan_bi
#             result['netBuy']=jing_mai_ru_e
#             result['updateTime']=today
#             result['detail']=longhu_detail(code)
#             data.append(result)
#         for item in data:
#             result=db[COLLECTION_LHB].update_one({'code':item['code'],'updateTime':today},{'$set':item},upsert=True)
#         return data
#     except Exception as e:
#         print(e)

# 龙虎榜第二层页面数据
# def longhu_detail(code):
#     detail=dict()
#     LONGHU_DETAIL_URL = 'http://data.10jqka.com.cn/market/lhbcjmx/code/%s/' % code
#     session = requests.session()
#     url =LONGHU_DETAIL_URL
#     req = session.get(url)
#     html = req.content
#     soup = BeautifulSoup(html, 'lxml')
#     # 类型很多，可能两张表或两张以上
#     tables=soup.find_all('div',class_="lhb_rank_list")
#     for index,table in enumerate(tables):
#         title=table.find('div',class_='jj_ggcjmx_title').get_text().replace(' ','').replace('\t','').replace('\r\n','')
#         buy_sell=table.find('tbody')
#         # flag用来判断是买入还是卖出的排序，碰到一个列数为1的行，即买入排序变为卖出排序
#         flag=-1
#         buy=list()
#         sell=list()
#         for row in buy_sell.find_all('tr'):
#             col=row.find_all('td')
#             col=[x for x in col]
#             n_col=len(col)
#             if n_col==1:
#                 flag+=1
#             if n_col==8:
#                 rank_num = col[0].text
#                 hall_name = col[1].a.text
#                 buy_money = col[2].text
#                 buy_proportion = col[3].text
#                 sell_money = col[4].text
#                 sell_proportion = col[5].text
#                 sum_money = col[6].text
#                 vol = col[7].text
#                 hall_data={
#                         'sort':rank_num,
#                         'brokerDepartment':hall_name,
#                         'buyAmount':buy_money,
#                         'buyAmountRate':buy_proportion,
#                         'sellAmount':sell_money,
#                         'sellAmountRate':sell_proportion,
#                         'netAmount':sum_money,
#                         'vol':vol
#                     }
#                 # flag=0为买入排序
#                 if not flag:
#                     buy.append(hall_data)
#                 # flag=1为卖出排序
#                 else:
#                     sell.append(hall_data)
#         detail['type%s'%index]=dict()
#         detail['type%s'%index]['title']=title
#         detail['type%s'%index]['buy']=buy
#         detail['type%s'%index]['sell']=sell
#     return detail

# 高管增持榜
# def gaoguan():
#     try:
#         _before_sleep()
#         GAO_GUAN_URL = 'http://data.10jqka.com.cn/financial/ggjy/'
#         session = requests.session()
#         url = GAO_GUAN_URL
#         req = session.get(url)
#         html = req.content
#         soup = BeautifulSoup(html, 'lxml')
#         gao_guan=soup.find('table',class_='m-table J-ajax-table J-canvas-table')
#         gao_guan=gao_guan.tbody
#         gao_guan=gao_guan.find_all('tr')
#         result_data=list()
#         shijian = list()
#         for code_data in gao_guan:
#             data=code_data.find_all('td')
#             data = [x.get_text() for x in data]
#             xu_hao,code, jian_cheng, bian_dong_ren, bian_dong_ri_qi,bian_dong_gu_shu,cheng_jiao_jun_jia, bian_dong_yuan_yin,bian_dong_bi_li,bian_dong_hou_gu_shu,dong_jian_gao, dong_jian_gao_xin_chou,dong_jian_gao_zhi_wu, dong_jian_gao_guan_xi = data
#             result={
#                 'code':code,
#                 'stockBrief':jian_cheng,
#                 'changePerson':bian_dong_ren,
#                 'changeDate':bian_dong_ri_qi,
#                 'changeNum':bian_dong_gu_shu,
#                 'avgDealPrice':cheng_jiao_jun_jia,
#                 'changeReason':bian_dong_yuan_yin,
#                 'changeRate':bian_dong_bi_li,
#                 'changeLeft':bian_dong_hou_gu_shu,
#                 'mrBig':dong_jian_gao,
#                 'mrBigSalary':dong_jian_gao_xin_chou,
#                 'mrBigDuty':dong_jian_gao_zhi_wu,
#                 'mrBigRelation':dong_jian_gao_guan_xi,
#                 'updateTime':today
#             }
#             shijian.append(bian_dong_ri_qi)
#             if bian_dong_ri_qi==max(shijian):
#                 result_data.append(result)
#             else:
#                 continue
#         for item in result_data:
#             result=db[COLLECTION_GGZC].update_one({'changePerson':item['changePerson'],'changeNum':item['changeNum'],'changeDate':item['changeDate']},{'$set':item},upsert=True)
#         return result_data
#     except Exception as e:
#         print(e)

# 限售解禁榜
# def xianshou():
#     try:
#         _before_sleep()
#         XIAN_SHOU_URL = 'http://data.10jqka.com.cn/market/xsjj/field/enddate/order/asc/ajax/1/page/%s/'
#         session = requests.session()
#         result_data = list()
#         for page in range(1,6):
#             url = XIAN_SHOU_URL%page
#             req = session.get(url)
#             html = req.content.decode('GBK')
#             soup = BeautifulSoup(html, 'lxml')
#             xian_shou = soup.find('table', class_='m-table J-ajax-table')
#             xian_shou = xian_shou.tbody
#             if xian_shou==None:
#                 continue
#             xian_shou = xian_shou.find_all('tr')
#             for code_data in xian_shou:
#                 data = code_data.find_all('td')
#                 data = [x.get_text() for x in data]
#                 xu_hao,code,jian_cheng,ri_qi,jie_jin_shu,zui_xin_jia,jie_jin_gu_shi_zhi,zhan_zong_gu_ben_bi_li,xian_shou_gu_dong=data
#                 result = {
#                     'code': code,
#                     'stockBrief': jian_cheng,
#                     'releaseDate': ri_qi,
#                     'releaseNum':jie_jin_shu,
#                     'releaseValue':jie_jin_gu_shi_zhi,
#                     'proportion':zhan_zong_gu_ben_bi_li,
#                     'updateTime':today
#                 }
#                 result_data.append(result)
#         for item in result_data:
#             result=db[COLLECTION_XSJJ].update_one({'code':item['code'],'releaseDate':item['releaseDate'],'updateTime':today},{'$set':item},upsert=True)
#         return result_data
#     except Exception as e:
#         print(e)

# 机构调研
def jigoudiaoyan(date):
    try:
        #_before_sleep()
        JIGOUDIAOYAN_URL = 'http://data.eastmoney.com/DataCenter_V3/jgdy/gsjsdy.ashx?pagesize=50&page=%s&sortRule=-1&sortType=0'
        HEADERS = {'content-type': 'application/json',
                   'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
        flag=False
        for page in range(1,4): #3
            url = JIGOUDIAOYAN_URL % page
            try:
                html = requests.get(url, headers=HEADERS)
                job = json.loads(html.text)
                raw_data = job['data']
                # print (raw_data)
            except Exception as e:
                break
            data = list()
            for raw_item in raw_data:
                item = dict()
                item['code'] = raw_item['SCode']
                item['surveyDate'] = raw_item['StartDate']
                item['announceDate'] = raw_item['NoticeDate']
                print (item)
                if item['announceDate']<date:
                    flag=True
                    break
                elif item['announceDate']>date:
                    continue
                data.append(item)
            print ('//////////////////////////////////////////////////////////////////////////////////////////////////////')
            print (data)
            print (item['code'])
            print (item['surveyDate'])
            for item in data:
                _jigoudiaoyan(item['code'],item['surveyDate']) #
            if flag:
                break
    except Exception as e:
        print(e)



# 机构调研主要内容抓取
def _jigoudiaoyan(code,date):
    JIGOUDIAOYAN_URL2='http://data.eastmoney.com/jgdy/dyxx/%s,%s.html'%(code,date)
    session = requests.session()
    url = JIGOUDIAOYAN_URL2
    req = session.get(url)
    html = req.content
    soup = BeautifulSoup(html,'html5lib')
    item=dict()
    item['code']=code
    item['surveyDate']=date
    tables=soup.find_all('table',class_='tab1')
    data_list=tables[0].find_all('td')
    item['anonDate'],item['receptionPerson'],item['receptionStart'],\
    item['receptionClose'],item['receptionType'],item['receptionLocation']=[x.get_text() for x in data_list]
    data_list=tables[1].tbody.find_all('tr')
    content_data = tables[2].p.children
    content_ary = []
    for x in content_data:
        sx = str(x)
        if sx == '<br/>':
            continue
        content_ary.append(sx)
    content = '\r\n\r\n'.join(content_ary)
    item['content'] = content
    item['invitedPersons']=list()
    for data in data_list:
        org_detail=dict()
        detail=data.find_all('td')
        org_detail['no'],org_detail['invitedPerson'],org_detail['invitedPersonType'],\
        org_detail['orgRelatedPerson']=[x.get_text() for x in detail]
        item['invitedPersons'].append(org_detail)
    db[COLLECTION_JGDY].update_one({'code': item['code'],'surveyDate':item['surveyDate']},
                                   {'$set': item}, upsert=True)



jigoudiaoyan('2017-02-08')


# 大宗交易
# def dazongjiaoyi(date):
#     _before_sleep()
#     year,month,day=date.split('-')
#     DAZONGJIAOYI_URL='http://data.eastmoney.com/dzjy/%s.html'%(year+month)
#     session = requests.session()
#     url = DAZONGJIAOYI_URL
#     try:
#         req = session.get(url)
#         html = req.content
#         soup = BeautifulSoup(html, 'html5lib')
#         table=soup.find_all('tbody')[2]
#         data=table.find_all('tr',class_="list_eve")

#         result = list()
#         for row in data:
#             item = dict()
#             cols = row.find_all('td')
#             if len(cols) == 10:
#                 item['tradeDate'], item['code'], item['stockBrief'], \
#                 item['tradeDetail'], item['currentPrice'], item['tradePrice'], \
#                 item['tradeNum'], item['tradeSum'], item['buyBusinessDept'], \
#                 item['sellBusinessDept'] = [x.get_text() for x in cols]
#                 date_template = item['tradeDate']
#                 code_template = item['code']
#                 name_template = item['stockBrief']
#                 detail_template = item['tradeDetail']
#                 price_template = item['currentPrice']
#             elif len(cols) == 9:
#                 item['tradeDate'] = date_template
#                 item['code'], item['stockBrief'], \
#                 item['tradeDetail'], item['currentPrice'], item['tradePrice'], \
#                 item['tradeNum'], item['tradeSum'], item['buyBusinessDept'], \
#                 item['sellBusinessDept'] = [x.get_text() for x in cols]
#                 code_template = item['code']
#                 name_template = item['stockBrief']
#                 detail_template = item['tradeDetail']
#                 price_template = item['currentPrice']
#             elif len(cols) == 5:
#                 item['tradeDate'] = date_template
#                 item['code'], item['stockBrief'], item['tradeDetail'], \
#                 item['currentPrice'] = code_template, name_template, detail_template, price_template
#                 item['tradePrice'], item['tradeNum'], item['tradeSum'], \
#                 item['buyBusinessDept'], item['sellBusinessDept'] = [x.get_text() for x in cols]
#             else:
#                 print("parser error,format can't recognized")
#                 return
#             if item['tradeDate'] < date:
#                 continue
#             elif item['tradeDate'] > date:
#                 break
#             else:
#                 if item['code'][0] in ['6', '3', '0']:
#                     result.append(item)
#         for item in result:
#             item.pop('tradeDetail')
#             db[COLLECTION_DZJY].update_one(
#                 {'tradeDate': item['tradeDate'], 'code': item['code'], 'stockBrief': item['stockBrief'], \
#                  'currentPrice': item['currentPrice'], 'tradePrice': item['tradePrice'], \
#                  'tradeNum': item['tradeNum'], 'tradeSum': item['tradeSum'], 'buyBusinessDept': item['buyBusinessDept'],
#                  'sellBusinessDept': item['sellBusinessDept']},
#                 {'$set': item}, upsert=True)

#     except ChunkedEncodingError as err:
#         print('dazongjiaoyi has ChunkedEncodingError occured! msg:%s' % err)
#     except Exception as e:
#         print(e)




# def main():
#     gnow = datetime.datetime.now()
#     gtoday = str(gnow)[:10]
#     current_day = gtoday
#     while True:
#         now = datetime.datetime.now()
#         today = str(now)[:10]
#         # run every 5 minutes
#         #announcement_SH()
#         #announcement_SZ()
#         # run each day in 0:00 AM when day switch
#         #if current_day != today:
#         #longhu()
#         #gaoguan()
#         #xianshou()
#         jigoudiaoyan(current_day)
#         #dazongjiaoyi(current_day)
#         current_day = today
#         time.sleep(3600)



# def run_now_once():
#     gnow = datetime.datetime.now()
#     gtoday = str(gnow)[:10]
#     current_day = gtoday
#     announcement_SH()
#     announcement_SZ()
#     longhu()
#     gaoguan()
#     xianshou()
#     jigoudiaoyan(current_day)
#     dazongjiaoyi(current_day)


# if __name__ == '__main__':
#     # main()
#    _jigoudiaoyan('300091','2017-01-17')

