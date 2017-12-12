# coding=utf-8
import pymongo
import requests
from bs4 import BeautifulSoup
import json
import datetime
import time

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
conn=pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
db=conn.crawl
COLLECTION_SH_ANON = 'sh_anon'
COLLECTION_SZ_ANON = 'sz_anon'
COLLECTION_LHB = 'lhb'
COLLECTION_XSJJ = 'xsjj'
COLLECTION_GGZC = 'ggzj'
COLLECTION_JGDY='jgdy'
COLLECTION_DZJY='dzjy'
today = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

# 上交所公告
def announcement_SH():
    time.sleep(30)
    SH_URL = 'http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc_2016openpdf.htm'
    session=requests.session()
    url=SH_URL
    req=session.get(url)
    html=req.content.decode('utf-8')
    soup=BeautifulSoup(html,'lxml')
    data=soup.find_all('em')
    data=[x.a for x in data]
    data=[{'url':x['href'],'title':x['title'],'code':x.get_text().split('：')[0],'update_time':today} for x in data]
    for item in data:
        result=db[COLLECTION_SH_ANON].update_one({'title':item['title']},{'$set':item},upsert=True)
    return data

# 深交所公告
def announcement_SZ():
    time.sleep(30)
    SZ_URL='http://disclosure.szse.cn//disclosure/fulltext/plate/szlatest_24h.js?'
    dns='http://disclosure.szse.cn/'
    session=requests.session()
    url=SZ_URL
    req=session.get(url)
    req.encoding='gbk'
    html=req.text.split('=')[1].replace(';','')
    data=json.loads(html)
    data = [{'url': dns+x[1], 'title': x[2], 'code':x[0],'update_time':today} for x in data]
    for item in data:
        result=db[COLLECTION_SZ_ANON].update_one({'title':item['title']},{'$set':item},upsert=True)
    return data
# announcement返回格式如下
# {'code': '002252', 'url': 'http://disclosure.szse.cn/finalpage/2016-11-29/1202846741.PDF', 'title': '上海莱士：关于召开2016年第三次临时股东大会的通知'}

# 龙虎榜
def longhu():
    time.sleep(30)
    LONGHU_URL='http://data.10jqka.com.cn/market/longhu/'
    session=requests.session()
    url=LONGHU_URL
    req=session.get(url)
    html=req.content
    soup=BeautifulSoup(html,'lxml')
    longhu_data=soup.find('tbody',class_='m_tbd')
    longhu_data=longhu_data.find_all('tr')
    data=list()
    for code_data in longhu_data:
        trigger=code_data.find_all('td',class_='tip-trigger')
        code,jian_cheng=[x.get_text().replace('\n','') for x in trigger]
        jie_du=code_data.find('a',charset='gbk').get_text()
        if  '敢死队' in jie_du or '知名营业部' in jie_du:
            jie_du='游资'
        elif '机构介入' in jie_du:
            jie_du='机构'
        else:
            continue
        mai_ru_zhan_bi=code_data.find('td',class_='c-rise').get_text()
        mai_chu_zhan_bi=code_data.find('td',class_='c-fall').get_text()
        jing_mai_ru_e=code_data.find('td',class_='c_eq').get_text()
        result=dict()
        result['代码']=code
        result['股票简称']=jian_cheng
        result['独家解读']=jie_du
        result['买入占比']=mai_ru_zhan_bi
        result['卖出占比']=mai_chu_zhan_bi
        result['净买入额']=jing_mai_ru_e
        result['update_time']=today
        data.append(result)
    for item in data:
        result=db[COLLECTION_LHB].update_one({'代码':item['代码'],'update_time':today},{'$set':item},upsert=True)
    return data

# 高管增持榜
def gaoguan():
    time.sleep(30)
    GAO_GUAN_URL = 'http://data.10jqka.com.cn/financial/ggjy/'
    session = requests.session()
    url = GAO_GUAN_URL
    req = session.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'lxml')
    gao_guan=soup.find('table',class_='m-table J-ajax-table J-canvas-table')
    gao_guan=gao_guan.tbody
    gao_guan=gao_guan.find_all('tr')
    result_data=list()
    shijian = list()
    for code_data in gao_guan[:10]:
        data=code_data.find_all('td')
        data = [x.get_text() for x in data]
        xu_hao,code, jian_cheng, bian_dong_ren, bian_dong_ri_qi,bian_dong_gu_shu,cheng_jiao_jun_jia, bian_dong_yuan_yin,bian_dong_bi_li,bian_dong_hou_gu_shu,dong_jian_gao, dong_jian_gao_xin_chou,dong_jian_gao_zhi_wu, dong_jian_gao_guan_xi = data
        result={
            '股票代码':code,
            '股票简称':jian_cheng,
            '变动人':bian_dong_ren,
            '变动日期':bian_dong_ri_qi,
            '变动股数':bian_dong_gu_shu,
            '成交均价':cheng_jiao_jun_jia,
            '变动原因':bian_dong_yuan_yin,
            '变动比例':bian_dong_bi_li,
            '变动后股数':bian_dong_hou_gu_shu,
            '董监高':dong_jian_gao,
            '董监高薪酬':dong_jian_gao_xin_chou,
            '董监高关系':dong_jian_gao_guan_xi,
            'update_time':today
        }
        shijian.append(bian_dong_ri_qi)
        if bian_dong_ri_qi==max(shijian):
            result_data.append(result)
        else:
            continue
    for item in result_data:
        result=db[COLLECTION_GGZC].update_one({'变动人':item['变动人'],'变动股数':item['变动股数'],'update_time':today},{'$set':item},upsert=True)
    return result_data

# 限售解禁榜
def xianshou():
    time.sleep(30)
    XIAN_SHOU_URL = 'http://data.10jqka.com.cn/market/xsjj/field/enddate/order/asc/ajax/1/page/%s/'
    session = requests.session()
    result_data = list()
    for page in range(1,6):
        url = XIAN_SHOU_URL%page
        req = session.get(url)
        html = req.content.decode('GBK')
        soup = BeautifulSoup(html, 'lxml')
        xian_shou = soup.find('table', class_='m-table J-ajax-table')
        xian_shou = xian_shou.tbody
        if xian_shou==None:
            continue
        xian_shou = xian_shou.find_all('tr')
        for code_data in xian_shou:
            data = code_data.find_all('td')
            data = [x.get_text() for x in data]
            xu_hao,code,jian_cheng,ri_qi,jie_jin_shu,zui_xin_jia,jie_jin_gu_shi_zhi,zhan_zong_gu_ben_bi_li,xian_shou_gu_dong=data
            result = {
                '股票代码': code,
                '股票简称': jian_cheng,
                '限售解禁日期': ri_qi,
                '本次解禁股数':jie_jin_shu,
                '解禁市值':jie_jin_gu_shi_zhi,
                '占总股本比例':zhan_zong_gu_ben_bi_li,
                'update_time':today
            }
            result_data.append(result)
    for item in result_data:
        result=db[COLLECTION_XSJJ].update_one({'股票代码':item['股票代码'],'限售解禁日期':item['限售解禁日期'],'update_time':today},{'$set':item},upsert=True)
    return result_data

# 机构调研
def jigoudiaoyan(date):
    JIGOUDIAOYAN_URL = 'http://data.eastmoney.com/DataCenter_V3/jgdy/gsjsdy.ashx?pagesize=50&page=%s&sortRule=-1&sortType=0'
    HEADERS = {'content-type': 'application/json',
               'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0'}
    flag=False
    for page in range(3):
        url = JIGOUDIAOYAN_URL % page
        try:
            html = requests.get(url, headers=HEADERS)
            job = json.loads(html.text)
            raw_data = job['data']
        except Exception as e:
            break
        data = list()
        for raw_item in raw_data:
            item = dict()
            item['代码'] = raw_item['SCode']
            item['调研日期'] = raw_item['StartDate']
            item['公告日期'] = raw_item['NoticeDate']
            if item['公告日期']<date:
                flag=True
                break
            elif item['公告日期']>date:
                continue
            data.append(item)
        for item in data:
            jigoudiaoyan_main(item['代码'],item['调研日期'])
        if flag:
            break

# 机构调研主要内容抓取
def jigoudiaoyan_main(code,date):
    JIGOUDIAOYAN_URL2='http://data.eastmoney.com/jgdy/dyxx/%s,%s.html'%(code,date)
    session = requests.session()
    url = JIGOUDIAOYAN_URL2
    req = session.get(url)
    html = req.content
    soup = BeautifulSoup(html,'html5lib')
    item=dict()
    item['代码']=code
    item['调研日期']=date
    tables=soup.find_all('table',class_='tab1')
    data_list=tables[0].find_all('td')
    item['公告日期'],item['上市公司接待人员'],item['接待时间起始'],\
    item['接待时间截止'],item['接待方式'],item['接待地点']=[x.get_text() for x in data_list]
    data_list=tables[1].tbody.find_all('tr')
    item['接待详细对象']=list()
    for data in data_list:
        org_detail=dict()
        detail=data.find_all('td')
        org_detail['序号'],org_detail['接待对象'],org_detail['接待对象类型'],\
        org_detail['机构相关人员']=[x.get_text() for x in detail]
        item['接待详细对象'].append(org_detail)
    db[COLLECTION_JGDY].update_one({'代码': item['代码'],'调研日期':item['调研日期']},
                                   {'$set': item}, upsert=True)
# 大宗交易
def dazongjiaoyi(date):
    year,month,day=date.split('-')
    DAZONGJIAOYI_URL='http://data.eastmoney.com/dzjy/%s.html'%(year+month)
    session = requests.session()
    url = DAZONGJIAOYI_URL
    req = session.get(url)
    html = req.content
    soup = BeautifulSoup(html, 'html5lib')
    table=soup.find_all('tbody')[2]
    data=table.find_all('tr',class_="list_eve")
    result=list()
    for row in data:
        item=dict()
        cols=row.find_all('td')
        if len(cols)==10:
            item['交易日期'],item['股票代码'],item['股票简称'],\
            item['交易详情'],item['当前价格'],item['成交价格'],\
            item['成交数量'],item['成交金额'],item['买方营业部'],\
            item['卖方营业部']=[x.get_text() for x in cols]
            date_template=item['交易日期']
            code_template = item['股票代码']
            name_template = item['股票简称']
            detail_template = item['交易详情']
            price_template = item['当前价格']
        elif len(cols)==9:
            item['交易日期']=date_template
            item['股票代码'], item['股票简称'], \
            item['交易详情'], item['当前价格'], item['成交价格'], \
            item['成交数量'], item['成交金额'], item['买方营业部'],\
            item['卖方营业部'] = [x.get_text() for x in cols]
            code_template=item['股票代码']
            name_template=item['股票简称']
            detail_template=item['交易详情']
            price_template=item['当前价格']
        elif len(cols)==5:
            item['交易日期']=date_template
            item['股票代码'], item['股票简称'],item['交易详情'],\
            item['当前价格']=code_template,name_template,detail_template,price_template
            item['成交价格'],item['成交数量'], item['成交金额'],\
            item['买方营业部'],item['卖方营业部'] = [x.get_text() for x in cols]
        else:
            print('???')
            return
        if item['交易日期']<date:
            continue
        elif item['交易日期']>date:
            break
        else:
            if item['股票代码'][0] in ['6','3','0']:
                result.append(item)
    for item in result:
        item.pop('交易详情')
        db[COLLECTION_DZJY].update_one({'交易日期':item['交易日期'],'股票代码':item['股票代码'],'股票简称':item['股票简称'],\
            '当前价格':item['当前价格'],'成交价格':item['成交价格'],\
            '成交数量':item['成交数量'],'成交金额':item['成交金额'],'买方营业厅':item['买方营业部'],'卖方营业厅':item['卖方营业部']},\
                                       {'$set': item}, upsert=True)







def main():
    gnow = datetime.datetime.now()
    gtoday = str(gnow)[:10]
    current_day = gtoday
    while True:
        now = datetime.datetime.now()
        today = str(now)[:10]
        # run every 5 minutes
        announcement_SH()
        announcement_SZ()
        # run each day in 0:00 AM when day switch
        if current_day != today:
            longhu()
            gaoguan()
            xianshou()
            current_day = today
        time.sleep(600)

if __name__ == '__main__':
    # main()
    dazongjiaoyi('2016-12-22')

