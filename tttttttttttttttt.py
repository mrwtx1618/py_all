#encoding:utf-8

import requests
from bs4 import BeautifulSoup
import requests
import datetime
import pymysql
import json
import time
import datetime
import sys



# the_str = 'JC-20151210\n\n开标日期：2015年12月10日\n\n中标供应商名称：东方财富信息股份有限公司\n\n中标金额：5.6万元\n\n'
# print(the_str)
# the_str_2 = the_str.replace('\n','')
# print(the_str_2)




# print(timestamp)
#
#
#
#
#
def get_page_source(need_url,need_cookies):
    proxy = {'http': 'http://110.73.15.65:8123'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0','Referer':'https://www.tianyancha.com/search?key=%E4%B8%8A%E6%B5%B7%E7%86%99%E9%A3%8E%E7%94%B5%E5%AD%90%E5%95%86%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox','Cookie':need_cookies}
    html = requests.get(need_url, headers=headers,proxies = proxy)
    soup = BeautifulSoup(html.content, 'lxml')
    return soup

#
soup_main_page = get_page_source('https://www.tianyancha.com/company/176277626','aliyungf_tc=AQAAAON7dk61GAYAbfLidH9WUXRG/FVA;csrfToken=gwjM6R4GDpbk_LLWVahk0J5m;TYCID=9ecbde40977811e7b5e02bd9acd5314e;uccid=530df41ef52d5d353180b1c09cb2efb5;ssuid=1658604870;tyc-user-info={"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODcwMTc4MDI1MSIsImlhdCI6MTUwNTE5MjkxMywiZXhwIjoxNTIwNzQ0OTEzfQ.MtkEmRmavz0fFp1UXS4V1XtcF-FLRWo3F1bubfoJkbzwx_ndmyVg4FfB4Ky9vw800s0tT_8s1cxaYaqNkDRLDA","integrity":"0%","state":"0","vnum":"0","onum":"0","mobile":"18701780251"};auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODcwMTc4MDI1MSIsImlhdCI6MTUwNTE5MjkxMywiZXhwIjoxNTIwNzQ0OTEzfQ.MtkEmRmavz0fFp1UXS4V1XtcF-FLRWo3F1bubfoJkbzwx_ndmyVg4FfB4Ky9vw800s0tT_8s1cxaYaqNkDRLDA;_csrf=j0BF7WMN0JgETy/uoLpHtA==;OA=YCBOCiyel30b/GvnGZdsuhTSyrHHzN3Y421rjNYpNag=;_csrf_bk=9e474d7ad73a2628f22bbde098f2a6fd;Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1505193001;Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1505193008')
# print(soup_main_page.prettify())

# if soup_main_page.find('div',class_ = 'mtft mbft f24') is not None:#说明存在'mtft mbft f24'这一项
#     print('Cookie时间过长,已经失效！')
# elif soup_main_page.find('div')

#过期的Cookie:
#TYCID=9b93e2e078ba11e7b908f565a2117175; uccid=ea09126cde05fc87d81f8231a5e8dc9c; aliyungf_tc=AQAAAFX81w1TIg0AbfLidHUGYBRoXCTr; csrfToken=FvhvDqhYzGLFwvHW27LJxGQN; bannerFlag=true; RTYCID=82886310c704490ab248adf7f2979be1; token=8623512cbd484c05b200449f5d07e065; _utm=68fd5a19253a4920bf2fcc7a8f8e270e; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwMzk5MDkxNiwiZXhwIjoxNTE5NTQyOTE2fQ.ikbmDEWf3Dq13YUVFsMe2cdEbPRdnlgPdDZrpLu5Y5IP66jo6nRXtjhUsOUU0YT-KmbZdBn9B99pU2dOBq3ULA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213611835756%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwMzk5MDkxNiwiZXhwIjoxNTE5NTQyOTE2fQ.ikbmDEWf3Dq13YUVFsMe2cdEbPRdnlgPdDZrpLu5Y5IP66jo6nRXtjhUsOUU0YT-KmbZdBn9B99pU2dOBq3ULA; _csrf=LOsZGOO/mm2B2JozYriLyw==; OA=E4eh3tNl9NWarJ4Y31bZEXIv9yKM6SUxcX1pN+nB+od5WqG5g1K6ElWDa15r0QZA; _csrf_bk=d5d1f21fe308c0bcef808affd21c47bf; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1503657499,1503885346,1503885384,1503990835; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1503990866



#会弹出验证码的Cookie:
#TYCID=9b93e2e078ba11e7b908f565a2117175; uccid=ea09126cde05fc87d81f8231a5e8dc9c; aliyungf_tc=AQAAAHnfeGheNQYAbfLidPGeZJKOMTYq; csrfToken=p39DzfosI2qFTxBoogx5LqvU; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwNDY2NTQ1NCwiZXhwIjoxNTIwMjE3NDU0fQ.8u-Au0aAn5MyXrix48u6DvHGFwVjsrllrId39o8HQlI6cvPo-oTnWTOegW_boTwGvqAIB0ssP6J1SGF0XesbUw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213611835756%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwNDY2NTQ1NCwiZXhwIjoxNTIwMjE3NDU0fQ.8u-Au0aAn5MyXrix48u6DvHGFwVjsrllrId39o8HQlI6cvPo-oTnWTOegW_boTwGvqAIB0ssP6J1SGF0XesbUw; _csrf=B9ES3O+Z9la9GI+x/Xv5mA==; OA=E4eh3tNl9NWarJ4Y31bZEXIv9yKM6SUxcX1pN+nB+od5WqG5g1K6ElWDa15r0QZA; _csrf_bk=d5d1f21fe308c0bcef808affd21c47bf; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1504488419,1504490224,1504661619,1504665360; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1504665406; token=3492cc4eb29547228bcfd7705d7b3bf1; _utm=966889f8a0754885adfc4d6dad759d1f

#1731199001
#
def invest_soup_to_list(soup_list):#这个函数用来取对外投资里面有时候会出现的没有数据的情况:转化成none
    right_list = []
    for ele in soup_list:
        try:
            data = ele.text.replace(' ', '').replace('\n', '').replace('>', '').strip()
            right_list.append(data)
        except Exception as e:
            right_list.append('')
    return right_list



def baseinfo(soup):
    try:
        print('爬取基本信息！')
        baseinfo_dict = {}
        # soup = soup_main_page
        the_soup_legalPerson = soup.find('div',attrs = {'id':'_container_baseInfo'})
        legalPersonName = the_soup_legalPerson.find('div',class_ = 'new-c3 f18 overflow-width').get('title')
        the_soup_1 = soup.find('a',attrs={'event-name':'企业详情-数据更新'})
        regNumber = the_soup_1.get("reg-number") #工商注册号
        updatetime = the_soup_1.get("update-time")#天眼查更新时间
        the_soup_2 = soup.find_all('td', class_="basic-td")
        the_data_list_1 = [x.text.replace(' ','').replace('\n','').strip() for x in the_soup_2]
        the_soup = soup.find('div', attrs={'id': '_container_baseInfo'})
        the_soup_3 = the_soup.find_all('div', attrs={'class': 'baseinfo-module-content-value'})
        data_3_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_3]
        regCapital = data_3_list[0]#注册资本
        establishTime = data_3_list[1]#成立时间
        regStatus = data_3_list[2]#经营状态

        creditCode = the_data_list_1[2][7:]#统一信用代码
        orgNumber = the_data_list_1[1][7:]#组织机构代码
        taxIdNumber = the_data_list_1[4][7:]#纳税人识别号
        companyOrgType = the_data_list_1[3][5:]#企业类型
        industry = the_data_list_1[5][3:]#行业
        fromTimetoTime = the_data_list_1[6][5:]#营业期限
        approvedTime = the_data_list_1[7][5:]#核准日期
        regInstitute = the_data_list_1[8][5:]#登记机关
        regLocation = the_data_list_1[9][5:]#注册地址
        businessScope = the_data_list_1[10][5:].replace(chr(39),'')#经营范围,把里面西安的单引号取消了
        state = judge_whether_on_list(soup)
        baseinfo_dict['regCapital'] = regCapital
        baseinfo_dict['establishTime'] = establishTime
        baseinfo_dict['regStatus'] = regStatus
        baseinfo_dict['regNumber'] = regNumber
        baseinfo_dict['updatetime'] = updatetime
        baseinfo_dict['creditCode'] = creditCode
        baseinfo_dict['orgNumber'] = orgNumber
        baseinfo_dict['IdNumber'] = taxIdNumber
        baseinfo_dict['companyOrgType'] = companyOrgType
        baseinfo_dict['industry'] = industry
        baseinfo_dict['fromTimetoTime'] = fromTimetoTime
        baseinfo_dict['approvedTime'] = approvedTime
        baseinfo_dict['regInstitute'] = regInstitute
        baseinfo_dict['regLocation'] = regLocation
        baseinfo_dict['businessScope'] = businessScope
        baseinfo_dict['is_volatility'] = state
        baseinfo_dict['legalPersonName'] = legalPersonName
    except Exception as e:
        print('爬取基本信息出错或基本信息为空！')
        return {}
    else:
        return baseinfo_dict









#主要人员
def staff(soup):
    print('爬取主要人员！')
    try:
        result = []#用来装组装好的字典
        # soup = soup_main_page
        # print(soup)
        the_soup = soup.find_all('a',attrs={'event-name':'企业详情-主要人员'})
        name_list = [x.text.replace(' ','').replace('\n','').strip() for x in the_soup]
        the_soup_2 = soup.find_all('div',class_ = 'in-block f14 new-c5 pt9 pl10 overflow-width vertival-middle')
        typeJoin_list = [x.text.replace(' ','').replace('\n','').replace('>','').strip() for x in the_soup_2]
        the_soup_3 = soup.find_all('a',attrs={'event-name2':'人员详情-点击量-主要人员'})
        toco_list = [x.text.replace(' ','').replace('\n','').replace('>','').strip() for x in the_soup_3]
        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['typeJoin'] = typeJoin_list[i]
            the_dict['toco'] = toco_list[i]
            result.append(the_dict)
    except Exception as e:
        print('爬取主要人员出错或主要人员为空！')
        return []
    else:
        return result






#股东信息
def holder(soup):
    print('爬取股东信息！')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_holder'})
        the_soup_1 = the_soup.find_all('a', attrs={'class': 'in-block vertival-middle overflow-width'})
        holder_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        the_soup_2 = the_soup.find_all('a', attrs={'class': 'point company_vip_color'})
        toco_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        the_soup_3 = the_soup.find_all('span', class_="c-money-y")
        percent_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_3]
        the_soup_4 = the_soup.find_all('span', class_="")
        money_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_4]
        for i in range(len(holder_list)):
            the_dict = {}
            the_dict['name'] = holder_list[i]
            the_dict['percent'] = percent_list[i]
            the_dict['toco'] = toco_list[i]
            the_dict['amount'] = money_list[i]
            result.append(the_dict)
    except Exception as e:
        print('爬取股东信息出错或股东信息为空！')
        return {}
    else:
        return result





#对外投资
def invest(soup):
    print('爬取对外投资！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_invest'})
        the_soup_1 = the_soup.find_all('a',attrs = {'event-name':'企业详情-对外投资'})
        name_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        the_soup_2 = the_soup.find_all('a',attrs = {'class':'point new-c4'})
        legalPersonName_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        the_soup_3 = the_soup.find_all('span',class_ = "pl10 pr10 pb3 f13 float-right linkBtnClor")
        toco_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_3]
        the_soup_4 = the_soup.find_all('td')
        data_list_all = []
        for ele in the_soup_4:
            data = ele.find('span',attrs = {'class':''})
            data_list_all.append(data)
        del data_list_all[::7]
        del data_list_all[::6]
        regCapital_soup = data_list_all[::5]
        regCapital_list = invest_soup_to_list(regCapital_soup)
        amount_soup = data_list_all[1::5]
        amount_list = invest_soup_to_list(amount_soup)
        establishTime_soup = data_list_all[3::5]
        establishTime_list = invest_soup_to_list(establishTime_soup)
        regStatus_soup = data_list_all[4::5]
        regStatus_list = invest_soup_to_list(regStatus_soup)
        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['legalPersonName'] = legalPersonName_list[i]
            the_dict['toco'] = toco_list[i]
            the_dict['regCapital'] = regCapital_list[i]
            the_dict['amount'] = amount_list[i]
            the_dict['regStatus'] = regStatus_list[i]

            result.append(the_dict)
    except Exception as e:
        print('爬取对外投资出错或对外投资为空！')
        print(e)
        return []
    else:
        return result








#变更记录,这里暂时先爬取第一页的
def changeinfo(soup):
    print('爬取变更记录')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_changeinfo'}).find('tbody').find_all('div')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').replace('\r', '').strip() for x in the_soup]
        date_list = data_list[::4]
        changeItem_list = data_list[1::4]
        contentBefore_list = data_list[2::4]
        contentAfter_list = data_list[3::4]
        for i in range(len(date_list)):
            the_dict = {}
            the_dict['changeTime'] = date_list[i]
            the_dict['changeItem'] = changeItem_list[i]
            the_dict['contentBefore'] = contentBefore_list[i]
            the_dict['contentAfter'] = contentAfter_list[i]
            result.append(the_dict)
    except Exception as e:
        print('爬取变更记录出错或变更记录为空！')
        return []
    else:
        return result




cookies_from_table = 'TYCID=9b93e2e078ba11e7b908f565a2117175; uccid=ea09126cde05fc87d81f8231a5e8dc9c; aliyungf_tc=AQAAAFX81w1TIg0AbfLidHUGYBRoXCTr; csrfToken=FvhvDqhYzGLFwvHW27LJxGQN; bannerFlag=true; RTYCID=82886310c704490ab248adf7f2979be1; token=8623512cbd484c05b200449f5d07e065; _utm=68fd5a19253a4920bf2fcc7a8f8e270e; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwMzk5MDkxNiwiZXhwIjoxNTE5NTQyOTE2fQ.ikbmDEWf3Dq13YUVFsMe2cdEbPRdnlgPdDZrpLu5Y5IP66jo6nRXtjhUsOUU0YT-KmbZdBn9B99pU2dOBq3ULA%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213611835756%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwMzk5MDkxNiwiZXhwIjoxNTE5NTQyOTE2fQ.ikbmDEWf3Dq13YUVFsMe2cdEbPRdnlgPdDZrpLu5Y5IP66jo6nRXtjhUsOUU0YT-KmbZdBn9B99pU2dOBq3ULA; _csrf=LOsZGOO/mm2B2JozYriLyw==; OA=E4eh3tNl9NWarJ4Y31bZEXIv9yKM6SUxcX1pN+nB+od5WqG5g1K6ElWDa15r0QZA; _csrf_bk=d5d1f21fe308c0bcef808affd21c47bf; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1503657499,1503885346,1503885384,1503990835; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1503990866'

#企业年报
def annualreport(code,need_cookies):#企业年报,这个函数用来取公司年报,最多可能有4个年报
    annual_report_dict_list = []
    print('爬取企业年报！请等待')
    # the_cookies = request.form['Cookie']  # selenium这个不需要cookie
    # the_cookies = cookies_from_table
    try:
        for i in range(4):#年报最多有4个,#这里发现2352479167只有3个,所以报错
            print('正在爬取{}年的企业年报!'.format(2016-i))
            complete_urls = 'https://www.tianyancha.com/reportContent/{}/{}'.format(code,2016-i)
            # print(complete_urls)
            annual_report_dict = {}
            soup_all = get_page_source(complete_urls,need_cookies)
            the_soup_1 = soup_all.find('table', class_="table").find_all('td')
            the_data_list_1 = [x.text for x in the_soup_1]
            basic_information_dict = {}
            credit_number_or_register_number = the_data_list_1[1]  # 统一社会信用代码/注册号
            company_name = the_data_list_1[3]  # 企业名称
            telephone_number = the_data_list_1[5]  # 企业联系电话
            postcode = the_data_list_1[7]  # 邮政编码
            company_status = the_data_list_1[9]  # 企业经营状态
            people_owned = the_data_list_1[11]  # 从业人数
            email_address = the_data_list_1[13]  # 电子邮箱
            whether_have_a_website_or_online_store = the_data_list_1[15]  # 是否有网站或者网店
            company_address = the_data_list_1[17]  # 企业通信地址
            whether_have_investment_info = the_data_list_1[19]  # 企业是否有投资信息或购买其他公司股权
            basic_information_dict['reportYear'] = '{}'.format(2016-i)
            basic_information_dict['creditCode'] = credit_number_or_register_number
            basic_information_dict['companyName'] = company_name
            basic_information_dict['phoneNumber'] = telephone_number
            basic_information_dict['postcode'] = postcode
            basic_information_dict['manageState'] = company_status
            basic_information_dict['employeeNum'] = people_owned
            basic_information_dict['email'] = email_address
            basic_information_dict['whether_have_a_website_or_online_store'] = whether_have_a_website_or_online_store
            basic_information_dict['postalAddress'] = company_address
            basic_information_dict['outboundInvestmentList'] = whether_have_investment_info
            try :  # 有的年报没有网站或网店信息
                the_soup_2 = soup_all.find('tr', attrs={'ng-repeat': "web in items.webInfoList track by $index"}).find_all(
                    'td')
                the_data_list_2 = [x.text for x in the_soup_2]
                the_type = the_data_list_2[0]  # 类型
                the_name = the_data_list_2[1]
                the_website = the_data_list_2[2]
                website_dict = {}
                website_dict['webType'] = the_type
                website_dict['name'] = the_name
                website_dict['website'] = the_website
            except Exception as e:
                print('a', e)
                website_dict = {}
                pass
            try:
                the_soup_3 = soup_all.find_all('tr', attrs={
                    'ng-repeat': "holder in items.shareholderList track by $index"})  # .find_all('td')
                the_data_list_3 = [x.find_all('td') for x in the_soup_3]
                shareholder_list = []
                for single_soup in the_data_list_3:
                    shareholder_dict = {}
                    single_data_list = [x.text for x in single_soup]
                    shareholder_dict['investorName'] = single_data_list[0]
                    shareholder_dict['subscribeAmount'] = single_data_list[1]
                    shareholder_dict['subscribeTime'] = single_data_list[2]
                    shareholder_dict['subscribeType'] = single_data_list[3]
                    shareholder_dict['paidAmount'] = single_data_list[4]
                    shareholder_dict['paidTime'] = single_data_list[5]
                    shareholder_dict['paidType'] = single_data_list[6]
                    shareholder_list.append(shareholder_dict)
            except Exception as e:
                print('b', e)
                shareholder_list = []
                pass
            try:
                # print('股东及出资信息:',shareholder_list)
                the_soup_4_all = soup_all.find_all('table', class_="table")
                the_soup_4 = the_soup_4_all[3]
                the_soup_4_1 = the_soup_4.find_all('td')
                the_data_list_4 = [x.text for x in the_soup_4_1]
                company_capital_information_dict = {}
                total_capital = the_data_list_4[1]
                owner_equity = the_data_list_4[3]
                total_sales = the_data_list_4[5]
                total_profit = the_data_list_4[7]
                main_revenue = the_data_list_4[9]
                net_profit = the_data_list_4[11]
                total_tax = the_data_list_4[13]
                total_debt = the_data_list_4[15]
                company_capital_information_dict['totalAssets'] = total_capital
                company_capital_information_dict['totalEquity'] = owner_equity
                company_capital_information_dict['totalSales'] = total_sales
                company_capital_information_dict['totalProfit'] = total_profit
                company_capital_information_dict['primeBusProfit'] = main_revenue
                company_capital_information_dict['retainedProfit'] = net_profit
                company_capital_information_dict['totalTax'] = total_tax
                company_capital_information_dict['totalLiability'] = total_debt
            except Exception as e:
                print('c', e)

                company_capital_information_dict = {
                    'totalAssets': '企业选择不公示',
                    'totalEquity': '企业选择不公示',
                    'totalSales': '企业选择不公示',
                    'totalProfit': '企业选择不公示',
                    'primeBusProfit': '企业选择不公示',
                    'retainedProfit': '企业选择不公示',
                    'totalTax': '企业选择不公示',
                    'totalLiability': '企业选择不公示'
                }
            try:
                the_soup_5 = soup_all.find_all('tr',
                                               attrs={'ng-repeat': "equity in items.equityChangeInfoList track by $index"})
                the_td_soup = [x.find_all('td') for x in the_soup_5]
                equity_change_dict_list = []
                for single_soup_2 in the_td_soup:
                    the_data_list_5 = [x.text for x in single_soup_2]
                    # print(the_data_list_5)
                    equity_change_dict = {}
                    equity_change_dict['investorName'] = the_data_list_5[0]
                    equity_change_dict['ratioBefore'] = the_data_list_5[1]
                    equity_change_dict['ratioAfter'] = the_data_list_5[2]
                    equity_change_dict['changeTime'] = the_data_list_5[3]
                    # print(equity_change_dict)
                    equity_change_dict_list.append(equity_change_dict)
                    # print('股权变更信息:',equity_change_dict_list)
            except Exception as e:
                print('d', e)
                pass
            try:
                the_soup_6 = soup_all.find_all('tr',
                                               attrs={'ng-repeat': "change in items.changeRecordList track by $index"})
                the_td_soup_2 = [x.find_all('td') for x in the_soup_6]
                modified_information_dict_list = []
                for single_soup_3 in the_td_soup_2:
                    the_data_list_6 = [x.text.replace('\t','').replace(' ', '').replace('\n', '').replace('>', '').replace('\r', '').strip() for x in single_soup_3]###
                    modified_information_dict = {}
                    modified_information_dict['changeTime'] = the_data_list_6[0]
                    modified_information_dict['changeItem'] = the_data_list_6[1]



                    import re
                    re_br = re.compile('<br\s*?/?>')
                    the_data_list_6[2] = re_br.sub('', the_data_list_6[2])  #
                    the_data_list_6[3] = re_br.sub('', the_data_list_6[3])  #

                    blank_line = re.compile('\n+')
                    the_data_list_6[2] = blank_line.sub('', the_data_list_6[2])
                    the_data_list_6[3] = blank_line.sub('', the_data_list_6[3])

                    re_h = re.compile('</?\w+[^>]*>')
                    the_data_list_6[2] = re_h.sub('', the_data_list_6[2])
                    the_data_list_6[3] = re_h.sub('', the_data_list_6[3])





                    modified_information_dict['contentBefore'] = the_data_list_6[2]
                    modified_information_dict['contentAfter'] = the_data_list_6[3]
                    modified_information_dict_list.append(modified_information_dict)
            except Exception as e:
                print('d', e)
                pass
            finally:
                annual_report_dict['webInfoList'] = website_dict
                annual_report_dict['shareholderList'] = shareholder_list
                annual_report_dict['baseInfo'] = dict(basic_information_dict,**company_capital_information_dict)
                annual_report_dict['equityChangeInfoList '] = equity_change_dict_list
                annual_report_dict['changeRecordList'] = modified_information_dict_list
                COLLECTION_NAME = company_name + complete_urls[-4:]
                annual_report_dict_list.append(annual_report_dict)

    except Exception as e:
        print(e)
        pass


    return annual_report_dict_list





#分支机构
def branch(soup):
    print('爬取分支机构！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_branch'}).find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup]
        data_list = data_list if (len(data_list))%4 == 0 else data_list[:-2]#这个地方的list有时候会多出'共','页'两字,所以这样处理
        name_list = data_list[::4]
        legalPersonName_list = data_list[1::4]
        regStatus_list = data_list[2::4]
        estiblishTime_list = data_list[3::4]
        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['legalPersonName'] = legalPersonName_list[i]
            the_dict['regStatus'] = regStatus_list[i]
            the_dict['estiblishTime'] = estiblishTime_list[i]
            result.append(the_dict)
    except Exception:
        print('爬取分支机构出错或者分支机构为空')
        return []
    else:
        return result






#融资历史
def findHistoryRongzi(soup):
    print('爬取融资历史！')
    try:
        result = []
        the_soup = soup.find('div',attrs = {'id':'_container_rongzi'})
        the_soup_td = the_soup.find_all('td')
        data_list_all = []
        for ele in the_soup_td:
            data = ele.find('span', attrs={'class': 'text-dark-color '})
            data_list_all.append(data)
        date_soup = data_list_all[::7]
        date_list = invest_soup_to_list(date_soup)
        round_soup = data_list_all[1::7]
        round_list = invest_soup_to_list(round_soup)
        value_soup = data_list_all[2::7]
        value_list = invest_soup_to_list(value_soup)
        money_soup = data_list_all[3::7]
        money_list = invest_soup_to_list(money_soup)
        share_soup = data_list_all[4::7]
        share_list = invest_soup_to_list(share_soup)
        investorName_soup = data_list_all[5::7]
        investorName_list = invest_soup_to_list(investorName_soup)
        newsUrl_soup = data_list_all[6::7]
        newsUrl_list = invest_soup_to_list(newsUrl_soup)
        for i in range(len(date_list)):
            the_dict = {}
            the_dict['date'] = date_list[i]
            the_dict['round'] = round_list[i]
            the_dict['money'] = money_list[i]
            the_dict['value'] = value_list[i]
            the_dict['share'] = share_list[i]
            the_dict['investorName'] = investorName_list[i]
            the_dict['newsUrl'] = newsUrl_list[i]
            result.append(the_dict)


    except Exception as e:
        print('爬取融资历史出错或融资历史为空！')
        return []
    else:
        return result






#核心团队
def findTeamMember(soup):
    print('爬取核心团队！')
    try:
        result = []
        the_soup = soup.find('div',attrs = {'id':'_container_teamMember'})
        the_name_soup = the_soup.find_all('div',class_ = 'team-name')
        name_list = invest_soup_to_list(the_name_soup)
        the_title_soup = the_soup.find_all('div',class_ = 'team-title')
        title_list = invest_soup_to_list(the_title_soup)
        the_team_item_soup = the_soup.find_all('div',class_ = 'team-item')
        desc_list = []
        icon_list = []
        for ele in the_team_item_soup:
            desc_soup = ele.find_all('span',class_ = 'text-dark-color')
            desc_txt = invest_soup_to_list(desc_soup)
            desc_list.append(desc_txt)
            icon_txt = ele.find_all('img')[0].get('src')
            icon_list.append(icon_txt)

        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['title'] = title_list[i]
            the_dict['desc'] = desc_list[i]
            the_dict['iconOssPath'] = icon_list[i]
            result.append(the_dict)

    except Exception:
        print('爬取核心团队出错或核心团队为空')
        return []
    else:
        return result





#企业业务
def getProductInfo(soup):#企业业务
    print('爬取企业业务！')
    try:
        result = []
        the_soup = soup.find('div',attrs = {'id':'_container_firmProduct'})
        # print(the_soup)
        the_soup_list = the_soup.find_all('div',class_ = 'product-item')
        product_list = []
        hangye_list = []
        yewu_list = []
        icon_list = []
        for ele in the_soup_list:
            product_text = ele.find('span',class_ = 'title')
            product_list.append(product_text.text)
            hangye_text = ele.find('div',class_ = 'hangye')
            hangye_list.append(hangye_text.text)
            yewu_text = ele.find('div',class_ = 'yeweu overflow-width')
            yewu_list.append(yewu_text.text)
            try:
                icon_text = ele.find_all('img')[0].get('src')
                icon_list.append(icon_text)
            except Exception as e:
                icon_text = 'none'
                icon_list.append(icon_text)


        for i in range(len(product_list)):
            the_dict = {}
            the_dict['product'] = product_list[i]
            the_dict['hangye'] = hangye_list[i]
            the_dict['yewu'] = yewu_list[i]
            the_dict['logoOssPath'] = icon_list[i]
            result.append(the_dict)
    except Exception as e:
        print('爬取企业业务出错或企业业务为空')
        print(e)
        return {}
    else:
        return result





#投资事件
def findTzanli(soup):
    print('爬取投资事件！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_touzi'}).find('tbody').find_all('tr')
        the_soup_2 = soup.find('div',attrs={'id':'_container_touzi'}).find('tbody').find_all('tr')
        the_icon_soup_list = [ele.find('img') for ele in the_soup_2]
        the_icon_list = [ele.get('src') for ele in the_icon_soup_list]
        the_data_list_1 = [x.find_all('span',attrs = {'class':'text-dark-color'}) for x in the_soup]
        the_data_list_2 = [x.find_all('a') for x in the_soup]
        the_data_list_3 = [x.find_all('span', class_ = '') for x in the_soup]
        tzdate_list = []
        lunci_list = []
        money_list = []
        organization_name_list = []
        product_list = []
        location_list = []
        hangye1_list = []
        yewu_list = []
        for i in range(len(the_data_list_1)):
            the_single_data_list_1 = the_data_list_1[i]
            data_list_1 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_single_data_list_1]
            the_single_data_list_2 = the_data_list_2[i]
            data_list_2 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_single_data_list_2]
            the_single_data_list_3 = the_data_list_3[i]
            data_list_3 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_single_data_list_3]
            tzdate_list.append(data_list_1[0])
            lunci_list.append(data_list_1[1])
            money_list.append(data_list_1[2])
            organization_name_list.append(data_list_2[:-1])
            product_list.append(data_list_2[-1])
            location_list.append(data_list_3[1])
            hangye1_list.append(data_list_3[-1])
        for i in range(len(tzdate_list)):
            the_dict = {}
            the_dict['tzdate'] = tzdate_list[i]
            the_dict['lunci'] = lunci_list[i]
            the_dict['money'] = money_list[i]
            the_dict['organization_name'] = organization_name_list[i]
            the_dict['product'] = product_list[i]
            the_dict['location'] = location_list[i]
            the_dict['hangye1'] = hangye1_list[i]
            the_dict['iconOssPath'] = the_icon_list[i]
            result.append(the_dict)
    except Exception as e:
        print('爬取投资事件出错或者投资事件为空')
        print(e)
        return []
    else:
        return result




#竞品信息
def findJingpin(soup):#竞品信息
    print('爬取竞品信息！')
    try:
        result = []
        the_soup_list = soup.find('div',attrs={'id':'_container_jingpin'}).find_all('tr')
        the_soup_list.remove((the_soup_list[0]))
        the_jingpinProduct_list = [ele.find('img').get('alt') for ele in the_soup_list]
        the_iconOssPath_list = [ele.find('img').get('src') for ele in the_soup_list]
        all_data_soup_list = [x.find_all('td',class_ = '') for x in the_soup_list]
        value_soup_list = [x.find_all('td',class_ = 'val') for x in the_soup_list]

        value_list = []
        for value_soup in value_soup_list:
            value_list.append(value_soup[0].text)
        location_list = []
        round_list = []
        hangye_list = []
        yewu_list = []
        setupDate_list = []
        for all_data_soup in all_data_soup_list:
            all_data = [ele.text for ele in all_data_soup][-5:]
            location = all_data[0]
            round = all_data[1]
            hangye = all_data[2]
            yewu = all_data[3]
            setupDate = all_data[4]
            location_list.append(location)
            round_list.append(round)
            hangye_list.append(hangye)
            yewu_list.append(yewu)
            setupDate_list.append(setupDate)

        for i in range(len(the_jingpinProduct_list)):
            the_dict = {}
            the_dict['location'] = location_list[i]
            the_dict['round'] = round_list[i]
            the_dict['hangye'] = hangye_list[i]
            the_dict['yewu'] = yewu_list[i]
            the_dict['setupDate'] = setupDate_list[i]
            the_dict['jingpinProduct'] = the_jingpinProduct_list[i]
            the_dict['iconOssPath'] = the_iconOssPath_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取竞品信息出错或者竞品信息为空！')
        print(e)
        return []
    else:
        return result





def get_lawsuit_urls_list(soup):
    the_soup = soup.find('div', attrs={'id': '_container_lawsuit'}).find('tbody').find_all('a',attrs = {'event-name':'企业详情-法律诉讼'})
    lawsuit_urls_single_list = [x.get('href') for x in the_soup]
    lawsuit_urls_complete_list = ['http://www.tianyancha.com' + ele for ele in lawsuit_urls_single_list]
    return lawsuit_urls_complete_list






#获取诉讼内容
content_list = []
def get_lawsuit_content(complete_lawsuit_urls_list):
    the_cookies = request.form['Cookie']
    for lawsuit_urls in complete_lawsuit_urls_list:
        print('dddddddddddddddddddddddddddddddddddddddddddddd')
        print(the_cookies)
        print(lawsuit_urls)
        soup = get_page_source(lawsuit_urls,the_cookies)
        print(soup)




#法律诉讼
def get_lawsuit_basic_info(soup):
    print('爬取法律诉讼！')
    try:
        result = []
        date_list = []
        type_list = []
        data_text_list = []
        lawsuit_titles_list = []
        soup_case_number_list = []
        the_soup = soup.find('div',attrs={'id':'_container_lawsuit'}).find('tbody').find_all('tr')
        the_data_list_1 = [x.find_all('span') for x in the_soup]
        the_data_list_2 = [x.find_all('a', attrs = {'event-name':'企业详情-法律诉讼'}) for x in the_soup]
        lawsuit_urls_list = get_lawsuit_urls_list(soup)
        for i in range(len(the_data_list_1)):
            the_single_data_list_1 = the_data_list_1[i]
            data_list_1 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_single_data_list_1]
            the_single_data_list_2 = the_data_list_2[i]
            data_list_2 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_single_data_list_2]
            date_list.append(data_list_1[0])
            type_list.append(data_list_1[1])
            soup_case_number_list.append(data_list_1[2])
            lawsuit_titles_list.append(data_list_2[0])
        for i in range(len(date_list)):
            the_dict = {}
            the_dict['submittime'] = date_list[i]
            the_dict['title'] = lawsuit_titles_list[i]
            the_dict['casetype'] = type_list[i]
            the_dict['caseno'] = soup_case_number_list[i]
            the_dict['lawsuitUrl'] = lawsuit_urls_list[i]
            result.append(the_dict)
    except Exception:
        print('爬取爬取法律诉讼出错或者爬取法律诉讼为空!')
        return []
    else:
        return result






#法律公告
def courtAnnouncement(soup):
    print('爬取法律公告！')
    try:
        result = []
        the_soup = soup.find_all('span',attrs={'class':'float-right text-click-color point companyinfo_show_more_btn'})
        courtAnnouncement_list = [x.get('onclick')[14:].lstrip('(').rstrip(')') for x in the_soup]
        courtAnnouncement_list = [eval(ele) for ele in courtAnnouncement_list]
    except Exception:
        print('爬取法律公告出错或者没有法律公告！')
        return {}
    else:
        return courtAnnouncement_list




#失信人
def dishonest(soup):
    print('爬取失信人！')
    try:
        result = []
        the_soup = soup.find_all('span',attrs={'ng-click':'dishonestOpen(item)'})
        dishonest_dict_content_list = [eval(x.get('onclick')[18:]) for x in the_soup]
        result = dishonest_dict_content_list
    except Exception:
        print('爬取失信人出错或者没有失信人！')
        return {}
    else:
        return result





#被执行人
def zhixinginfo(soup):
    print('爬取被执行人')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_zhixing'}).find('tbody').find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup]
        caseCreateTime_list = data_list[::4]
        execMoney_list = data_list[1::4]
        caseCode_list = data_list[2::4]
        execCourtName_list = data_list[3::4]
        for i in range(len(caseCreateTime_list)):
            the_dict = {}
            the_dict['caseCreateTime'] = caseCreateTime_list[i]
            the_dict['execMoney'] = execMoney_list[i]
            the_dict['caseCode'] = caseCode_list[i]
            the_dict['execCourtName'] = execCourtName_list[i]
            result.append(the_dict)
    except Exception:
        print('爬取被执行人出错或者没有被执行人！')
        return []
    else:
        return result






#经营异常
def abnormal(soup):
    print('爬取经营异常！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_abnormal'})
        the_soup = the_soup.find_all('span')
        data_list = [x.text.replace(' ','').replace('\n','').replace('>','').strip() for x in the_soup]
        putDate_list = data_list[::6]
        putReason_list = data_list[1::6]
        putDepartment_list = data_list[2::6]
        removeDate_list = data_list[3::6]
        removeReason_list = data_list[4::6]
        removeDepartment_list = data_list[5::6]

        for i in range(len(putDate_list)):
            the_dict = {}
            the_dict['putDate'] = putDate_list[i]
            the_dict['putReason'] = putReason_list[i]
            the_dict['putDepartment'] = putDepartment_list[i]
            the_dict['removeDate'] = removeDate_list[i]
            the_dict['removeReason'] = removeReason_list[i]
            the_dict['removeDepartment'] = removeDepartment_list[i]
            result.append(the_dict)

    except Exception:
        print('爬取经营异常出错或者经营异常为空！')
        return []
    else:
        return result













#行政处罚
def punishmentInfo(soup):
    print('爬取行政处罚')
    try:
        result = []
        the_soup = soup.find('span',attrs={'event-name':'company-detail-punishPopup'}).get('onclick')[15:]
        the_dict = (eval(the_soup))
        result.append(the_dict)
    except Exception:
        print('爬取行政处罚出错或者经营异常为空')
        return []
    else:
        return result






#严重违法
def illegalinfo(soup):
    the_dict = {}
    return the_dict






#股权出质
def equityInfo(soup):
    print('爬取股权出质！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_equity'}).find_all('span',class_ = 'text-click-color point companyinfo_show_more_btn')
        data_list_equityPopup = [ele.get('onclick') for ele in the_soup]
        data_list = [(ele[15:].lstrip("('").rstrip("')")).replace('null', '"null"') for ele in data_list_equityPopup]
        data_dict_list = [eval(ele) for ele in data_list]
        result = data_dict_list

    except Exception:
        print('爬取股权出质出错或者股权出质为空！')
        return {}
    else:
        return result






#动产抵押
def mortgageInfo(soup):
    print('爬取股权出质！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_mortgage'}).find_all('span',class_ = ' text-click-color point companyinfo_show_more_btn')
        data_list_MortgagePopup = [ele.get('onclick') for ele in the_soup]
        data_list = [(ele[17:].lstrip("('").rstrip("')")).replace('null', '"null"') for ele in data_list_MortgagePopup]
        data_dict_list = [eval(ele) for ele in data_list]
        result = data_dict_list

    except Exception:
        print('爬取股权出质出错或者股权出质为空！')
        return {}
    else:
        return result






#欠税公告
def ownTax(soup):
    print('爬取欠税公告！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_towntax'})
        the_soup = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup]
        publishDate_list = data_list[::6]
        taxIdNumber_list = data_list[1::6]
        taxCategory_list = data_list[2::6]
        newOwnTaxBalance_list = data_list[3::6]
        ownTaxBalance_list = data_list[4::6]
        tax_authority_list = data_list[5::6]

        for i in range(len(publishDate_list)):
            the_dict = {}
            the_dict['publishDate'] = publishDate_list[i]
            the_dict['taxIdNumber'] = taxIdNumber_list[i]
            the_dict['taxCategory'] = taxCategory_list[i]
            the_dict['newOwnTaxBalance'] = newOwnTaxBalance_list[i]
            the_dict['ownTaxBalance'] = ownTaxBalance_list[i]
            the_dict['tax_authority'] = tax_authority_list[i]
            result.append(the_dict)

    except Exception:
        print('爬取欠税公告出错或者欠税公告为空！')
        return []
    else:
        return result







#招投标
def bids(soup,need_cookies):
    print('爬取招投标')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_bid'}).find('tbody')
        title_soup = the_soup.find_all('a',attrs = {'event-name':'企业详情-招投标'})
        title_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in title_soup]
        purchaser_time_soup = the_soup.find_all('span',class_ = "")
        purchaser_time_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in purchaser_time_soup]
        createTime_list = purchaser_time_list[::2]
        purchaser_list = purchaser_time_list[1::2]
        links_soup = the_soup.find_all('a',attrs = {'event-name':'企业详情-招投标'})
        bids_links_list = ['https://www.tianyancha.com' + x.get('href') for x in links_soup]
        bids_content_list = [get_page_source(ele,need_cookies) for ele in bids_links_list]
        content_list = []
        for content_soup in bids_content_list:
            the_soup = content_soup.find('div',attrs={'id':'web-content'})
            content = the_soup.text
            content_list.append(content)
        for i in range(len(title_list)):
            the_dict = {}
            the_dict['createTime'] = createTime_list[i]
            the_dict['title'] = title_list[i]
            the_dict['purchaser'] = purchaser_list[i]
            the_dict['link'] = bids_links_list[i]
            the_dict['content'] = content_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取招投标出错或者招投标为空！')
        print(e)
        return []
    else:
        return result






#债券信息
def bond(soup):
    print('爬取债券信息')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_bond'}).find('tbody').find_all('span',class_ = 'text-click-color point companyinfo_show_more_btn')
        data_list_openBondPopup = [ele.get('onclick') for ele in the_soup]
        data_list = [(ele[13:].lstrip("('").rstrip("')")).replace('null', '"null"') for ele in data_list_openBondPopup]
        data_dict_list = [eval(ele) for ele in data_list]
        result = data_dict_list

    except Exception as e:
        print('爬取债券信息出错或者债券信息为空！')
        print(e)
        return []
    else:
        return result





#购地信息
def purchaseLand(soup):
    print('爬取购地信息')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_purchaseland'}).find_all('span',class_ = 'text-click-color point companyinfo_show_more_btn')
        data_list_purchaselandPopup = [ele.get('onclick') for ele in the_soup]
        data_list = [(ele[17:]).replace('null', '"null"').replace(';','').replace(' ','') for ele in data_list_purchaselandPopup]
        data_dict_list = [eval(ele) for ele in data_list]
        result = data_dict_list

    except Exception as e:
        print('爬取购地信息出错或者购地信息为空！')
        print(e)
        return []
    else:
        return result



#招聘信息
def employments(soup):
    print('爬取招聘信息！')
    try:
        result = []
        the_soup  = soup.find('div',attrs={'id':'_container_recruit'}).find('tbody')
        the_soup = the_soup.find_all('span',attrs = {'event-name':'企业详情-招聘'})
        data_list_openBondPopup = [ele.get('onclick') for ele in the_soup]
        data_list = [ele[13:-1].rstrip(")") for ele in data_list_openBondPopup]
        data_list = [eval(ele) for ele in data_list]
        result = data_list
        for i in range(len(data_list)):
            try:
                data_list[i]['experience'] = data_list[i]['experience'].lstrip('[').rstrip(']').replace(chr(34),'')
            except Exception as e:
                pass

        print(result)
    except Exception as e:
        print('爬取招聘信息或者招聘信息为空！')
        print(e)
        return []
    else:
        return result





#税务评级
def taxCredit(soup):
    print('爬取税务评级！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_taxcredit'}).find('tbody')
        the_soup = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup]
        year_list = data_list[::5]
        grade_list = data_list[1::5]
        idNumber_list = data_list[3::5]
        evalDepartment_list = data_list[4::5]

        for i in range(len(year_list)):
            the_dict = {}
            the_dict['year'] = year_list[i]
            the_dict['grade'] = grade_list[i]
            the_dict['idNumber'] = idNumber_list[i]
            the_dict['evalDepartment'] = evalDepartment_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取税务评级或者税务评级为空！')
        print(e)
        return []
    else:
        return result






#抽查检查
def checkInfo(soup):
    print('爬取抽查检查！')
    try:
        result = []
        # print(soup)
        the_soup = soup.find('div',attrs={'id':'_container_check'}).find('tbody')
        the_soup = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup]
        print(data_list)
        checkDate_list = data_list[::4]
        checkOrg_list = data_list[1::4]
        checkType_list = data_list[2::4]
        checkResult_list = data_list[3::4]
        for i in range(len(checkDate_list)):
            the_dict = {}
            the_dict['checkDate'] = checkDate_list[i]
            the_dict['checkOrg'] = checkOrg_list[i]
            the_dict['checkType'] = checkType_list[i]
            the_dict['checkResult'] = checkResult_list[i]
            result.append(the_dict)


    except Exception as e:
        print('爬取抽查检查或者抽查检查为空！')
        print(e)
        return []
    else:
        return result





#产品信息
def appbkInfo(soup):
    print('爬取产品信息！')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_product'})
        the_soup_1 = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        name_list = data_list[::5][:-1]
        filterName_list = data_list[1::5][:-1]
        type_list = data_list[2::5]
        classes_list = data_list[3::5]
        the_soup_brief = the_soup.find_all('span',class_ = ' point companyinfo_show_more_btn')
        brief_str_list = [ele.get('onclick')[11:-1] for ele in the_soup_brief]
        brief_dict_list = [eval(ele)['brief'] for ele in brief_str_list]
        icon_soup_list = the_soup.find_all('img')
        icon_list = [ele.get('src') for ele in icon_soup_list]

        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['filterName'] = filterName_list[i]
            the_dict['type'] = type_list[i]
            the_dict['classes'] = classes_list[i]
            the_dict['brief'] = brief_dict_list[i]
            the_dict['icon'] = icon_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取产品信息或者产品信息为空！')
        print(e)
        return []
    else:
        return result




#资质证书
def qualification(soup):
    print('爬取资质证书！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_certificate'}).find('tbody')
        the_soup = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup]
        licenceType_list = data_list[::4]
        licenceNum_list = data_list[1::4]
        issueDate_list = data_list[2::4]
        toDate_list = data_list[3::4]

        for i in range(len(licenceType_list)):
            the_dict = {}
            the_dict['licenceType'] = licenceType_list[i]
            the_dict['licenceNum'] = licenceNum_list[i]
            the_dict['issueDate'] = issueDate_list[i]
            the_dict['toDate'] = toDate_list[i]

            result.append(the_dict)

    except Exception as e:
        print('爬取资质证书或者资质证书为空！')
        print(e)
        return []
    else:
        return result


#商标信息
def tm(soup):
    print('爬取商标信息！')
    try:
        result = []
        # print(soup.prettify())
        the_soup = soup.find('div',attrs={'id':'_container_tmInfo'}).find('tbody')
        # print(the_soup)
        the_soup_1 = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        # print((data_list))
        appDate_list = data_list[::5]
        tmName_list = data_list[1::5]
        regNo_list = data_list[2::5]
        intCls_list = data_list[3::5]
        status_list = data_list[4::5]
        icon_soup_list = the_soup.find_all('img')
        icon_list = [ele.get('src') for ele in icon_soup_list]


        for i in range(len(appDate_list)):
            the_dict = {}
            the_dict['appdate'] = appDate_list[i]
            the_dict['tmName'] = tmName_list[i]
            the_dict['regNo'] = regNo_list[i]
            the_dict['intCls'] = intCls_list[i]
            the_dict['status'] = status_list[i]
            the_dict['tmPic'] = icon_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取商标信息或者商标信息为空！')
        print(e)
        return []
    else:
        return result




#专利
def patents(soup):
    print('爬取专利！')
    try:
        result = []
        # print(soup)
        the_soup = soup.find('div',attrs={'id':'_container_patent'}).find('tbody')
        the_soup_list = the_soup.find_all('span',class_ = 'point float-right companyinfo_show_more_btn')
        patents_str_list = [ele.get('onclick')[15:] for ele in the_soup_list]
        patents_dict_list = [eval(ele) for ele in patents_str_list]

        for ele in patents_dict_list:
            result.append(ele)

    except Exception as e:
        print('爬取专利出错或者专利为空！')
        print(e)
        return []
    else:
        return result




#著作权
def copyReg(soup):
    print('爬取著作权！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_copyright'}).find('tbody')
        the_soup_list = the_soup.find_all('span',class_ = 'point float-right companyinfo_show_more_btn')
        patents_str_list = [ele.get('onclick')[18:] for ele in the_soup_list]
        patents_dict_list = [eval(ele) for ele in patents_str_list]

        for ele in patents_dict_list:
            result.append(ele)

    except Exception as e:
        print('爬取著作权出错或者著作权为空！')
        print(e)
        return []
    else:
        return result



#网站备案
def icp(soup):
    print('网站备案！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_icp'}).find('tbody')
        the_soup_1 = the_soup.find_all('span')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        the_soup_webSite = the_soup.find_all('a',class_ = 'in-block company-max-width overflow-width vertival-middle text-click-color')
        webSite_list = [ele.text for ele in the_soup_webSite]
        the_soup_ym = the_soup.find_all('td')[3::7]
        the_ym_list = [ele.text for ele in the_soup_ym]
        examineDate_list = data_list[::5]
        companyType_list = data_list[1::5]
        liscense_list = data_list[2::5]
        regnum_list = data_list[3::5]
        catnum_list = data_list[4::5]

        for i in range(len(examineDate_list)):
            the_dict = {}
            the_dict['examineDate'] = examineDate_list[i]
            the_dict['webName'] = companyType_list[i]
            the_dict['liscense'] = liscense_list[i]
            the_dict['regnum'] = regnum_list[i]
            the_dict['companyType'] = catnum_list[i]
            the_dict['webSite'] = webSite_list[i]
            the_dict['ym'] = the_ym_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取网站备案出错或者网站备案为空！')
        print(e)
        return []
    else:
        return result












#股票行情
def volatility(soup):
    print('爬取股票行情！')
    try:
        the_soup = soup.find('div',attrs={'id':'_container_volatilityNum'})
        the_soup_1 = the_soup.find_all('td')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        the_soup_2 = the_soup.find_all('span')
        data_list_2 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        tmaxprice = data_list[1] #涨停价
        tminprice = data_list[3] #跌停价
        topenprice = data_list[5] #今开
        pprice = data_list[7]#昨收
        thighprice = data_list[9]#最高
        tlowprice = data_list[11]#最低
        tvalue = data_list[13]#总市值
        flowvalue = data_list[15]#流通市值
        tamount = data_list[17]#成交量
        tamounttotal = data_list[19]#成交额
        tvaluep = data_list[21]
        fvaluep = data_list[23]
        trange = data_list[25]
        tchange = data_list[27]
        stockname = data_list_2[0]
        stockcode = data_list_2[1][1:-1]
        timeshow = data_list_2[6][5:]
        hexm_float_rate = data_list_2[5][1:-1]
        hexm_float_price = data_list_2[4]
        hexm_curPrice = data_list_2[3]

        the_dict = {}
        the_dict['tmaxprice'] = tmaxprice
        the_dict['tminprice'] = tminprice
        the_dict['topenprice'] = topenprice
        the_dict['pprice'] = pprice
        the_dict['thighprice'] = thighprice
        the_dict['tlowprice'] = tlowprice
        the_dict['tvalue'] = tvalue
        the_dict['flowvalue'] = flowvalue
        the_dict['tamount'] = tamount
        the_dict['tamounttotal'] = tamounttotal
        the_dict['tvaluep'] = tvaluep
        the_dict['fvaluep'] = fvaluep
        the_dict['trange'] = trange
        the_dict['tchange'] = tchange
        the_dict['stockname'] = stockname
        the_dict['stockcode'] = stockcode
        the_dict['timeshow'] = timeshow
        the_dict['hexm_float_rate'] = hexm_float_rate
        the_dict['hexm_float_price'] = hexm_float_price
        the_dict['hexm_curPrice'] = hexm_curPrice


    except Exception as e:
        print('爬取股票行情出错或者股票行情为空！')
        print(e)
        return {}
    else:
        return the_dict





#企业简介
def companyInfo(soup):
    print('爬取企业简介！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'nav-main-stockNum'}).find('tbody')
        the_soup_1 = the_soup.find_all('td',attrs = {'colspan':'3'})
        data_list_1 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        engName = data_list_1[0].replace(chr(39),'')#企业的英文名,把可能出现的单引号去掉
        usedName = data_list_1[1]
        controllingShareholder = data_list_1[2]
        actualController = data_list_1[3]#实际控制人
        finalController = data_list_1[4]#最终控制人
        the_soup_2 = the_soup.find_all('td',attrs = {'width':'35%'})
        data_list_2 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        industry = data_list_2[0]
        mainBusiness = data_list_2[1]
        the_soup_3 = the_soup.find_all('a',class_ = "in-block vertival-middle overflow-width")
        data_list_3 = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_3]
        the_soup_4 = the_soup.find_all('td')
        registeredCapital = the_soup_4[17].text
        employeesNum = the_soup_4[19].text


        chairman = data_list_3[0]
        secretaries = data_list_3[1]
        legal = data_list_3[2]
        generalManager = data_list_3[3]
        the_dict = {}
        the_dict['engName'] = engName
        the_dict['usedName'] = usedName
        the_dict['controllingShareholder'] = controllingShareholder
        the_dict['actualController'] = actualController
        the_dict['finalController'] = finalController
        the_dict['industry'] = industry
        the_dict['mainBusiness'] = mainBusiness
        the_dict['chairman'] = chairman
        the_dict['secretaries'] = secretaries
        the_dict['legal'] = legal
        the_dict['generalManager'] = generalManager
        the_dict['registeredCapital'] = registeredCapital
        the_dict['employeesNum'] = employeesNum
        result.append(the_dict)


    except Exception as e:
        print('爬取企业简介出错或者企业简介为空！')
        print(e)
        return []
    else:
        return result






#高管信息
def seniorExecutive(soup):
    print('爬取高管信息！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_seniorPeople'}).find('tbody')
        the_soup = the_soup.find_all('span',attrs={'class':'text-click-color point float-right companyinfo_show_more_btn'})
        the_new_soup = [ele.get('onclick') for ele in the_soup]
        data_list = [ele[16:] for ele in the_new_soup]
        data_dict_list = [eval(ele) for ele in data_list]
        result = data_dict_list


    except Exception as e:
        print('爬取高管信息出错或者高管信息为空！')
        print(e)
        return []
    else:
        return result






#参股控股
def holdingCompany(soup):
    print('爬取参股控股！')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_holdingCompany'}).find('tbody')
        the_soup_2 = the_soup.find_all('td')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        name_list = data_list[::7]
        relationship_list = data_list[1::7]
        participationRatio_list = data_list[2::7]
        investmentAmount_list = data_list[3::7]
        profit_list = data_list[4::7]
        reportMerge_list = data_list[5::7]
        mainBusiness_list = data_list[6::7]

        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['relationship'] = relationship_list[i]
            the_dict['participationRatio'] = participationRatio_list[i]
            the_dict['investmentAmount'] = investmentAmount_list[i]
            the_dict['profit'] = profit_list[i]
            the_dict['reportMerge'] = reportMerge_list[i]
            the_dict['mainBusiness'] = mainBusiness_list[i]
            result.append(the_dict)

    except Exception:
        print('爬取参股控股出错或者参股控股为空！')
        print(Exception)
        return []
    else:
        return result






#上市公告
def announcement(soup):
    print('爬取上市公告！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_announcement'}).find('tbody')
        the_soup_1 = the_soup.find_all('td')
        date_title_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        time_list = date_title_list[::2]
        title_list = date_title_list[1::2]
        for i in range(len(time_list)):
            the_dict = {}
            the_dict['time'] = time_list[i]
            the_dict['title'] = title_list[i]
            result.append(the_dict)

    except Exception:
        print('爬取上市公告出错或者上市公告为空！')
        print(Exception)
        return []
    else:
        return result




#十大股东
def shareholder(soup):
    print('十大股东！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'_container_topTenNum'}).find('tbody')
        the_soup_2 = the_soup.find_all('td')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        the_soup_3 = soup.find('div',attrs={'id':'_container_topTenNum'})
        the_soup_4 = the_soup_3.find('div',class_ = 'float-left tabItemNor new-c4 point tabItemActive')
        publishDate = the_soup_4.text
        name_list = data_list[::6]
        holdingNum_list = data_list[1::6]
        holdingChange_list = data_list[2::6]
        tenPercent_list = data_list[3::6]
        actual_list = data_list[4::6]
        shareType_list = data_list[5::6]

        for i in range(len(name_list)):
            the_dict = {}
            the_dict['name'] = name_list[i]
            the_dict['tenTotal'] = holdingNum_list[i]
            the_dict['holdingChange'] = holdingChange_list[i]
            the_dict['proportion'] = tenPercent_list[i]
            the_dict['actual'] = actual_list[i]
            the_dict['shareType'] = shareType_list[i]
            the_dict['publishDate'] = publishDate
            result.append(the_dict)

    except Exception:
        print('爬取十大股东出错或者十大股东为空！')
        print(Exception)
        return []
    else:
        return result





#发行相关
def issueRelated(soup):
    print('发行相关！')
    try:
        result = []
        the_soup = soup.find('div',attrs={'id':'nav-main-issueRelatedNum'}).find('tbody')
        the_soup_1 = the_soup.find_all('td')
        data_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        issueDate = data_list[1]
        listingDate = data_list[3]
        issueNumber = data_list[5]
        issuePrice = data_list[7]
        ipoRatio = data_list[9]
        expectedToRaise = data_list[11]
        openingPrice = data_list[13]
        rate = data_list[15]
        actualRaised = data_list[17]
        name = data_list[19]
        shang_shi_bao_jian_ren = data_list[21]
        history = data_list[23]
        the_dict = {}
        the_dict['issueDate'] = issueDate
        the_dict['listingDate'] = listingDate
        the_dict['issueNumber'] = issueNumber
        the_dict['issuePrice'] = issuePrice
        the_dict['ipoRatio'] = ipoRatio
        the_dict['expectedToRaise'] = expectedToRaise
        the_dict['openingPrice'] = openingPrice
        the_dict['rate'] = rate
        the_dict['actualRaised'] = actualRaised
        the_dict['name'] = name
        the_dict['shang_shi_bao_jian_ren'] = shang_shi_bao_jian_ren
        the_dict['history'] = history
        result.append(the_dict)


    except Exception:
        print('爬取十大股东出错或者十大股东为空！')
        print(Exception)
        return []
    else:
        return result





#股本结构
def shareStructure(soup):
    print('爬取股本结构')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_shareStructure'})
        the_soup_1 = the_soup.find('tbody')
        the_soup_2 = the_soup_1.find_all('td')
        data_list = [ele.text for ele in the_soup_2]
        pubDate = data_list[0]
        shareAll = data_list[1]
        ashareAll = data_list[2]
        noLimitShare = data_list[3]
        limitShare = data_list[4]
        changeReason = data_list[8]
        the_dict = {}
        the_dict['pubDate'] = pubDate
        the_dict['shareAll'] = shareAll
        the_dict['ashareAll'] = ashareAll
        the_dict['noLimitShare'] = noLimitShare
        the_dict['limitShare'] = limitShare
        the_dict['changeReason'] = changeReason
        result.append(the_dict)

    except Exception as e:
        print('爬取股本结构出错或股本结构为空')
        print(e)
        return []
    else:
        return result





#股本变动
def equityChange(soup):
    print('爬取股本变动')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_equityChange'})
        the_soup_1 = the_soup.find('tbody')
        the_soup_2 = the_soup_1.find_all('td')
        data_list = [ele.text for ele in the_soup_2]
        changeDate_list = data_list[::5]
        changeReason_list = data_list[1::5]
        afterAll_list = data_list[2::5]
        afterNoLimit_list = data_list[3::5]
        afterLimit_list = data_list[4::5]
        for i in range(len(changeDate_list)):
            the_dict = {}
            the_dict['changeDate'] = changeDate_list[i]
            the_dict['changeReason'] = changeReason_list[i]
            the_dict['afterAll'] = afterAll_list[i]
            the_dict['afterNoLimit'] = afterNoLimit_list[i]
            the_dict['afterLimit'] = afterLimit_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取股本变动出错或股本变动为空')
        print(e)
        return []
    else:
        return result



#分红情况
def bonusInfo(soup):
    print('爬取分红情况！')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_bonus'})
        the_soup_1 = the_soup.find('tbody')
        the_soup_2 = the_soup_1.find_all('td')
        data_list = [ele.text for ele in the_soup_2]
        boardDate_list = data_list[::10]
        shareholderDate_list = data_list[1::10]
        implementationDate_list = data_list[2::10]
        introduction_list = data_list[3::10]
        asharesDate_list = data_list[4::10]
        acuxiDate_list = data_list[5::10]
        adividendDate_list = data_list[6::10]
        progress_list = data_list[7::10]
        payment_list = data_list[8::10]
        dividendRate_list = data_list[9::10]
        for i in range(len(boardDate_list)):
            the_dict = {}
            the_dict['boardDate'] = boardDate_list[i]
            the_dict['shareholderDate'] = shareholderDate_list[i]
            the_dict['implementationDate'] = implementationDate_list[i]
            the_dict['introduction'] = introduction_list[i]
            the_dict['asharesDate'] = asharesDate_list[i]
            the_dict['acuxiDate'] = acuxiDate_list[i]
            the_dict['adividendDate'] = adividendDate_list[i]
            the_dict['progress'] = progress_list[i]
            the_dict['payment'] = payment_list[i]
            the_dict['dividendRate'] = dividendRate_list[i]
            result.append(the_dict)

    except Exception as e:
        print('爬取分红情况出错或分红情况为空')
        print(e)
        return []
    else:
        return result


#配股情况
def allotment(soup):
    print('爬取配股情况')
    try:
        result = []
        the_soup = soup.find('div', attrs={'id': '_container_allotment'})
        the_soup_1 = the_soup.find('tbody')
        the_soup_2 = the_soup_1.find_all('td')
        data_list = [ele.text for ele in the_soup_2]
        progress = data_list[1]
        issueCode = data_list[3]
        name = data_list[5]
        proportion = data_list[7]
        issueDate = data_list[9]
        pubDate = data_list[11]
        price = data_list[13]
        sDate = data_list[15]
        announceDate = data_list[17]
        actualRaise = data_list[19]
        proportionalLimit = data_list[21]
        exDate = data_list[23]
        saDate = data_list[25]
        raiseCeiling = data_list[27]
        registerDate = data_list[29]
        dDate = data_list[31]
        the_dict = {}
        the_dict['progress'] = progress
        the_dict['issueCode'] = issueCode
        the_dict['name'] = name
        the_dict['proportion'] = proportion
        the_dict['issueDate'] = issueDate
        the_dict['pubDate'] = pubDate
        the_dict['price'] = price
        the_dict['sDate'] = sDate
        the_dict['announceDate'] = announceDate
        the_dict['actualRaise'] = actualRaise
        the_dict['proportionalLimit'] = proportionalLimit
        the_dict['exDate'] = exDate
        the_dict['saDate'] = saDate
        the_dict['raiseCeiling'] = raiseCeiling
        the_dict['registerDate'] = registerDate
        the_dict['dDate'] = dDate
        result.append(the_dict)

    except Exception as e:
        print('爬取配股情况出错或配股情况为空')
        print(e)
        return []
    else:
        return result


# soup_main_page,company_url_code = get_page_source_selenium('https://www.tianyancha.com/company/2326916680')
#有失信人:https://www.tianyancha.com/company/35027356,北京爱旅伟邦科技有限公司
#有法律公告:https://www.tianyancha.com/company/2309977828,国水投资集团西安风电设备股份有限公司
#有被执行人:https://www.tianyancha.com/company/197070433,航天精工股份有限公司
#有经营异常:https://www.tianyancha.com/company/27412800,北京途虎信息技术有限公司
#有股权出质:https://www.tianyancha.com/company/664692849,湖北省宏源药业科技股份有限公司
#有动产抵押:https://www.tianyancha.com/company/2348888298,常州市新港热电有限公司
#有欠税公告:https://www.tianyancha.com/company/546136510,武汉远东绿世界集团有限公司

#这个函数在统计每个字段的个数时被调用到
def translator(need_list):
    tran_list = []
    for ele in need_list:
        if ele == '发行相关':
            ele = 'issueRelatedNum'
            tran_list.append(ele)
        elif ele == '配股情况':
            ele = 'allotmentNum'
            tran_list.append(ele)
        elif ele == '股票行情':
            ele = 'volatilityNum'
            tran_list.append(ele)
        elif ele == '企业简介':
            ele = 'stockNum'
            tran_list.append(ele)
        elif ele == '基本信息':
            ele = 'baseInfo'
            tran_list.append(ele)
        elif ele == '企业关系':
            ele = 'graphInfo'
            tran_list.append(ele)
        elif ele == '高管信息':
            ele = 'seniorExecutiveNum'
            tran_list.append(ele)
        elif ele == '参股控股':
            ele = 'holdingCompanyNum'
            tran_list.append(ele)
        elif ele == '上市公告':
            ele = 'announcementNum'
            tran_list.append(ele)
        elif ele == '十大股东':
            ele = 'topTenNum'
            tran_list.append(ele)
        elif ele == '股本结构':
            ele = 'shareStructureNum'
            tran_list.append(ele)
        elif ele == '股本变动':
            ele = 'equityChangeNum'
            tran_list.append(ele)
        elif ele == '分红情况':
            ele = 'bonusInfoNum'
            tran_list.append(ele)
        elif ele == '主要人员':
            ele = 'staffCount'
            tran_list.append(ele)
        elif ele == '股东信息':
            ele = 'holderCount'
            tran_list.append(ele)
        elif ele == '对外投资':
            ele = 'inverstCount'
            tran_list.append(ele)
        elif ele =='变更记录' :
            ele = 'changeCount'
            tran_list.append(ele)
        elif ele =='企业年报':
            ele = 'reportCount'
            tran_list.append(ele)
        elif ele =='招聘':
            ele ='recruitCount'
            tran_list.append(ele)
        elif ele == '税务评级':
            ele = 'taxCreditCount'
            tran_list.append(ele)
        elif ele == '著作权':
            ele = 'cpoyRCount'
            tran_list.append(ele)
        elif ele == '十大流通':
            ele = 'topTenFloat'
            tran_list.append(ele)
        elif ele == '分支机构':
            ele = 'branchCount'
            tran_list.append(ele)
        elif ele == '融资历史':
            ele = 'companyRongzi'
            tran_list.append(ele)
        elif ele == '核心团队':
            ele = 'companyTeammember'
            tran_list.append(ele)
        elif ele == '企业业务':
            ele = 'companyProduct'
            tran_list.append(ele)
        elif ele == '投资事件':
            ele = 'jigouTzanli'
            tran_list.append(ele)
        elif ele == '竞品信息':
            ele = 'companyJingpin'
            tran_list.append(ele)
        elif ele == '法律诉讼':
            ele = 'lawsuitCount'
            tran_list.append(ele)
        elif ele == '法院公告':
            ele = 'courtCount'
            tran_list.append(ele)
        elif ele == '失信人':
            ele = 'dishonest'
            tran_list.append(ele)
        elif ele == '被执行人':
            ele = 'zhixing'
            tran_list.append(ele)
        elif ele == '经营异常':
            ele = 'abnormalCount'
            tran_list.append(ele)
        elif ele == '行政处罚':
            ele = 'punishment'
            tran_list.append(ele)
        elif ele == '严重违法':
            ele = 'illegalCount'
            tran_list.append(ele)
        elif ele == '股权出质':
            ele = 'equityCount'
            tran_list.append(ele)
        elif ele == '动产抵押':
            ele = 'mortgageCount'
            tran_list.append(ele)
        elif ele == '欠税公告':
            ele = 'ownTaxCount'
            tran_list.append(ele)
        elif ele == '招投标':
            ele = 'bidCount'
            tran_list.append(ele)
        elif ele == '债券信息':
            ele = 'bondCount'
            tran_list.append(ele)
        elif ele == '购地信息':
            ele = 'goudiCount'
            tran_list.append(ele)
        elif ele == '抽查检查':
            ele = 'checkCount'
            tran_list.append(ele)
        elif ele == '产品信息':
            ele = 'productinfo'
            tran_list.append(ele)
        elif ele == '资质证书':
            ele = 'qualification'
            tran_list.append(ele)
        elif ele == '专利':
            ele = 'patentCount'
            tran_list.append(ele)
        elif ele == '网站备案':
            ele = 'icpCount'
            tran_list.append(ele)
        elif ele == '商标信息':
            ele = 'tm'
            tran_list.append(ele)
        else:
            print('没有这个字段！')
            pass
    return tran_list






#爬取每个字段的个数！
def count(soup):
    print('爬取字段个数！')
    try:
        result = []
        the_soup_1 = soup.find_all('div', attrs={'class': 'company-nav-item-enable canClick'})
        data_list_enable = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        the_soup_2 = soup.find_all('div', attrs={'class': 'company-nav-item-disable'})
        data_list_disabled = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        data_list_with_0 = [ele[:-1] for ele in data_list_disabled if ele[-1]=='0']
        data_list_with_none_1 = [ele for ele in data_list_disabled if ele[-1] !='0']
        # print('0000000000000000000000000000000000000000000000000000000000',data_list_with_0)#数字为0的
        # print(data_list_with_none_1)#disable里面没有数字的
        the_soup_num = soup.find_all('span',class_ ='c9')
        the_num_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_num]

        data_list_with_none_2 = [ele for ele in data_list_enable if ele[-1] not in ['0','1','2','3','4','5','6','7','8','9','+']]
        # print(data_list_with_none_2)
        data_list_with_none_all = data_list_with_none_1+data_list_with_none_2#所有的没有数字的
        # print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn',data_list_with_none_all)
        # print(the_num_list)
        data_list_with_the_num_raw_1 = [ele[:-1] for ele in data_list_enable if ele[-1] in ['0','1','2','3','4','5','6','7','8','9','+']]
        data_list_with_the_num_1 = [ele for ele in data_list_with_the_num_raw_1 if ele[-1] not in ['0','1','2','3','4','5','6','7','8','9']]
        data_list_with_the_num_raw_2 = [ele[:-1] for ele in data_list_with_the_num_1 if ele[-1] in ['0','1','2','3','4','5','6','7','8','9']]
        # print(data_list_with_the_num_raw_1)
        data_list_with_the_num_raw_2 = [ele[:-1] if ele[-1] in ['0','1','2','3','4','5','6','7','8','9'] else ele for ele in data_list_with_the_num_raw_1]
        data_list_with_the_num_raw_3 = [ele[:-1] if ele[-1] in ['0','1','2','3','4','5','6','7','8','9'] else ele for ele in data_list_with_the_num_raw_2]
        data_list_with_the_num = [ele[:-1] if ele[-1] in ['0','1','2','3','4','5','6','7','8','9'] else ele for ele in data_list_with_the_num_raw_3]
        # print('9999999999999999999999999999999999999999999999999999999999',data_list_with_the_num)
        eng_data_list_with_0 = translator(data_list_with_0)
        eng_data_list_with_none_all = translator(data_list_with_none_all)
        eng_data_list_with_the_num = translator(data_list_with_the_num)
        # print('0000000000000000000000000000000000',eng_data_list_with_0)
        the_0_list = []
        for i in range(len(eng_data_list_with_0)):
            the_0_list.append('0')
        the_0_dict = dict(zip(eng_data_list_with_0,the_0_list))
        # print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn',eng_data_list_with_none_all)
        the_none_list = []
        for i in range(len(eng_data_list_with_none_all)):
            the_none_list.append('none')
        the_none_dict = dict(zip(eng_data_list_with_none_all,the_none_list))
        # print('9999999999999999999999999999999999',eng_data_list_with_the_num)
        the_number_dict = dict(zip(eng_data_list_with_the_num,the_num_list))
        print('dddddddddddddddddddddddd')
        print(the_number_dict)
        count_info = dict(the_number_dict,**the_none_dict,**the_0_dict)
        result.append(count_info)

    except Exception as e:
        print('爬取个数情况出错或个数为空')
        print(e)
        return []
    else:
        return result






#股权结构
def equityRatio(equityRatio_url,need_cookies):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36",
        "Cookie": need_cookies}
    html = requests.get(equityRatio_url, headers=headers)
    result = html.text
    result_null_with_double_quotation_marks = result.replace('null', '"null"').replace('true', '"true"').replace('false','"false"')
    result_dict = eval(result_null_with_double_quotation_marks)
    return result_dict['data']





########################################################################################################################
##下面是各个字段的数量##
def staff_count(soup):
    print('爬取主要人员数量！')
    result = {}
    try:

        the_soup = soup.find('div',attrs={'tyc-event-ch':'CompangyDetail.zhuyaorenyuan'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['staff'] = number
        return result

    except Exception as e:
        print('爬取主要人员出错或主要人员为空！')
        return {'staff':'0'}






def holder_count(soup):
    print('爬取股东数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-holderCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['holder'] = number
        return result

    except Exception as e:
        print('爬取股东出错或股东为空！')
        return {'holder':'0'}


def invest_count(soup):
    print('爬取对外投资数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-inverstCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['invest'] = number
        return result

    except Exception as e:
        print('爬取对外投资数量出错或对外投资数量为空！')
        return {'invest':'0'}




def changeinfo_count(soup):
    print('爬取变更记录数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-changeCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['changeinfo'] = number
        return result

    except Exception as e:
        print('爬取变更记录数量出错或变更记录数量为空！')
        return {'changeinfo':'0'}






def annualreport_count(soup):
    print('爬取企业年报数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-reportCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['annualreport'] = number
        return result

    except Exception as e:
        print('爬取企业年报数量出错或企业年报数量为空！')
        return {'annualreport_count':'0'}





def branch_count(soup):
    print('爬取分支机构数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-branchCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['branch'] = number
        return result

    except Exception as e:
        print('爬取分支机构数量出错或分支机构数量为空！')
        return {'branch':'0'}






def findHistoryRongzi_count(soup):
    print('爬取融资历史数量！')
    result = {}
    try:
        # print(soup.prettify())
        the_soup = soup.find('div',attrs={'id':'nav-main-companyRongzi'})
        # print(the_soup)
        number = the_soup.find('span',class_ = "intro-count").text
        print(number)
        result['findHistoryRongzi'] = number
        return result

    except Exception as e:
        print('爬取融资历史数量出错或融资历史数量为空！')
        return {'findHistoryRongzi':'0'}





def findTeamMember_count(soup):
    print('爬取核心团队数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-companyTeammember'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['findTeamMember'] = number
        return result

    except Exception as e:
        print('爬取核心团队数量出错或核心团队数量为空！')
        return {'findTeamMember':'0'}





def getProductInfo_count(soup):
    print('爬取企业业务数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-companyProduct'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['getProductInfo'] = number
        return result

    except Exception as e:
        print('爬取企业业务数量出错或企业业务数量为空！')
        return {'getProductInfo':'0'}





def findTzanli_count(soup):
    print('爬取投资事件数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-jigouTzanli'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['findTzanli'] = number
        return result

    except Exception as e:
        print('爬取投资事件数量出错或投资事件数量为空！')
        return {'findTzanli':'0'}





def findJingpin_count(soup):
    print('爬取竞品信息数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-companyJingpin'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['findJingpin'] = number
        return result

    except Exception as e:
        print('爬取竞品信息数量出错或竞品信息数量为空！')
        return {'findJingpin':'0'}





def lawSuit_count(soup):
    print('爬取法律诉讼数量！')
    result = {}
    try:
        # print(soup.prettify())
        the_soup = soup.find('div',attrs={'id':'nav-main-lawsuitCount'})
        # print(the_soup)
        number = the_soup.find('span',class_ = "intro-count").text
        # print(number)
        result['lawSuit'] = number
        return result

    except Exception as e:
        print('爬取法律诉讼数量出错或法律诉讼数量为空！')
        return {'lawSuit':'0'}


def courtAnnouncement_count(soup):
    print('爬取法院公告数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-courtCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['courtAnnouncement'] = number
        return result

    except Exception as e:
        print('爬取法院公告数量出错或法院公告数量为空！')
        return {'courtAnnouncement':'0'}




def dishonest_count(soup):
    print('爬取失信人数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-dishonest'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['dishonest'] = number
        return result

    except Exception as e:
        print('爬取失信人数量出错或失信人数量为空！')
        return {'dishonest':'0'}





def zhixinginfo_count(soup):
    print('爬取被执行人数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-zhixing'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['zhixinginfo'] = number
        return result

    except Exception as e:
        print('爬取被执行人数量出错或被执行人数量为空！')
        return {'zhixinginfo':'0'}





def abnormal_count(soup):
    print('爬取经营异常数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-abnormalCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['abnormal'] = number
        return result

    except Exception as e:
        print('爬取经营异常数量出错或经营异常数量为空！')
        return {'abnormal':'0'}






def illegalinfo_count(soup):
    print('爬取严重违法数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-illegalinfoCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['illegalinfo'] = number
        return result

    except Exception as e:
        print('爬取严重违法数量出错或严重违法数量为空！')
        return {'illegalinfo':'0'}






def equityInfo_count(soup):
    print('爬取股权出质数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-equityCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['equityInfo'] = number
        return result

    except Exception as e:
        print('爬取股权出质数量出错或股权出质数量为空！')
        return {'equityInfo':'0'}





def mortgageInfo_count(soup):
    print('爬取动产抵押数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-mortgageCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['mortgageInfo'] = number
        return result

    except Exception as e:
        print('爬取动产抵押数量出错或动产抵押数量为空！')
        return {'mortgageInfo':'0'}






def ownTax_count(soup):
    print('爬取欠税公告数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-ownTaxCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['ownTax'] = number
        return result

    except Exception as e:
        print('爬取欠税公告数量出错或欠税公告数量为空！')
        return {'ownTax':'0'}






def bids_count(soup):
    print('爬取招投标数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-bidCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['bids'] = number
        return result

    except Exception as e:
        print('爬取招投标数量出错或招投标数量为空！')
        return {'bids':'0'}




def bond_count(soup):
    print('爬取债券信息数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-bondCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['bond'] = number
        return result

    except Exception as e:
        print('爬取债券信息数量出错或债券信息数量为空！')
        return {'bond':'0'}





def purchaseLand_count(soup):
    print('爬取购地信息数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-purchaseLandCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['purchaseLand'] = number
        return result

    except Exception as e:
        print('爬取购地信息数量出错或购地信息数量为空！')
        return {'purchaseLand':'0'}






def employments_count(soup):
    print('爬取招聘数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-recruitCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['employments'] = number
        return result

    except Exception as e:
        print('爬取招聘数量出错或招聘数量为空！')
        return {'employments':'0'}





def taxCredit_count(soup):
    print('爬取税务评级数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-taxCreditCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['taxCredit'] = number
        return result

    except Exception as e:
        print('爬取税务评级数量出错或税务评级数量为空！')
        return {'taxCredit':'0'}





def checkInfo_count(soup):
    print('爬取税务评级数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-checkCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['checkInfo'] = number
        return result

    except Exception as e:
        print('爬取税务评级数量出错或税务评级数量为空！')
        return {'checkInfo':'0'}





def appbkInfo_count(soup):
    print('爬取产品信息数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-productinfo'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['appbkInfo'] = number
        return result

    except Exception as e:
        print('爬取产品信息数量出错或产品信息数量为空！')
        return {'appbkInfo':'0'}






def tm_count(soup):
    print('爬取商标信息数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-tmCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['tm'] = number
        return result

    except Exception as e:
        print('爬取商标信息数量出错或商标信息数量为空！')
        return {'tm':'0'}





def patents_count(soup):
    print('爬取专利数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-patentCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['patents'] = number
        return result

    except Exception as e:
        print('爬取专利数量出错或专利数量为空！')
        return {'patents':'0'}



def copyReg_count(soup):
    print('爬取软件著作权数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-cpoyRCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['copyReg'] = number
        return result

    except Exception as e:
        print('爬取软件著作权数量出错或软件著作权数量为空！')
        return {'copyReg':'0'}


def icp_count(soup):
    print('爬取网站备案数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-icpCount'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['icp'] = number
        return result

    except Exception as e:
        print('爬取网站备案数量出错或网站备案数量为空！')
        return {'icp':'0'}




def seniorExecutive_count(soup):
    print('爬取高管信息数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-seniorExecutiveNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['seniorExecutive'] = number
        return result

    except Exception as e:
        print('爬取高管信息数量出错或高管信息数量为空！')
        return {'seniorExecutive':'0'}


def holdingCompany_count(soup):
    print('爬取参股控股数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-holdingCompanyNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['holdingCompany'] = number
        return result

    except Exception as e:
        print('爬取参股控股数量出错或参股控股数量为空！')
        return {'holdingCompany':'0'}




def announcement_count(soup):
    print('爬取上市公告数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-announcementNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['announcement'] = number
        return result

    except Exception as e:
        print('爬取上市公告数量出错或上市公告数量为空！')
        return {'announcement':'0'}





def shareholder_count(soup):
    print('爬取十大股东数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-topTenNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['shareholder'] = number
        return result

    except Exception as e:
        print('爬取十大股东数量出错或十大股东数量为空！')
        return {'shareholder':'0'}





def tenTradable_shareholder_count(soup):
    print('爬取发行相关数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-tenTradableNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['tenTradable_shareholder'] = number
        return result

    except Exception as e:
        print('爬取发行相关数量出错或发行相关数量为空！')
        return {'tenTradable_shareholder':'0'}



def issueRelated_count(soup):
    print('爬取十大流通股东数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-issueRelatedNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['issueRelated_shareholder'] = number
        return result

    except Exception as e:
        print('爬取十大流通股东数量出错或十大流通股东数量为空！')
        return {'issueRelated_shareholder':'0'}





def shareStructure_count(soup):
    print('爬取股本结构数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-shareStructureNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['shareStructure_shareholder'] = number
        return result

    except Exception as e:
        print('爬取股本结构数量出错或股本结构数量为空！')
        return {'shareStructure_shareholder':'0'}






def equityChange_count(soup):
    print('爬取股本变动数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-equityChangeNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['equityChange_shareholder'] = number
        return result

    except Exception as e:
        print('爬取股本变动数量出错或股本变动数量为空！')
        return {'equityChange_shareholder':'0'}





def bonusInfo_count(soup):
    print('爬取分红情况数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-bonusInfoNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['bonusInfo_shareholder'] = number
        return result

    except Exception as e:
        print('爬取分红情况数量出错或分红情况数量为空！')
        return {'bonusInfo_shareholder':'0'}





def allotmen_count(soup):
    print('爬取配股情况数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-allotmentNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['allotmen'] = number
        return result

    except Exception as e:
        print('爬取配股情况数量出错或配股情况数量为空！')
        return {'allotmen':'0'}




def volatility_count(soup):
    print('爬取股票行情数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-volatilityNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['volatility'] = number
        return result

    except Exception as e:
        print('爬取股票行情数量出错或股票行情数量为空！')
        return {'volatility':'0'}





def companyInfo_count(soup):
    print('爬取企业简介数量！')
    result = {}
    try:
        the_soup = soup.find('div',attrs={'id':'nav-main-stockNum'})
        number = the_soup.find('span',class_ = "intro-count").text
        result['companyInfo'] = number
        return result

    except Exception as e:
        print('爬取企业简介数量出错或企业简介数量为空！')
        return {'companyInfo':'0'}




#所有的字段的个数的信息
def the_new_count_info(soup):
    the_count_info = {}
    staff_count_dict = staff_count(soup)
    holder_count_dict = holder_count(soup)
    # print(holder_count_dict)
    invest_count_dict = invest_count(soup)
    changeinfo_count_dict = changeinfo_count(soup)
    annualreport_count_dict = annualreport_count(soup)
    branch_count_dict = branch_count(soup)
    findHistoryRongzi_count_dict = findHistoryRongzi_count(soup)
    findTeamMember_count_dict = findTeamMember_count(soup)
    getProductInfo_count_dict = getProductInfo_count(soup)
    findTzanli_count_dict = findTzanli_count(soup)
    findJingpin_count_dict = findJingpin_count(soup)
    lawSuit_count_dict = lawSuit_count(soup)
    courtAnnouncement_count_dict = courtAnnouncement_count(soup)
    dishonest_count_dict = dishonest_count(soup)
    zhixinginfo_count_dict = zhixinginfo_count(soup)
    abnormal_count_dict = abnormal_count(soup)
    illegalinfo_count_dict = illegalinfo_count(soup)
    equityInfo_count_dict = equityInfo_count(soup)
    mortgageInfo_count_dict = mortgageInfo_count(soup)
    ownTax_count_dict = ownTax_count(soup)
    bids_count_dict = bids_count(soup)
    bond_count_dict = bond_count(soup)
    purchaseLand_count_dict = purchaseLand_count(soup)
    employments_count_dict = employments_count(soup)
    taxCredit_count_dict = taxCredit_count(soup)
    checkInfo_count_dict = checkInfo_count(soup)
    appbkInfo_count_dict = appbkInfo_count(soup)
    tm_count_dict = tm_count(soup)
    patents_count_dict = patents_count(soup)
    copyReg_count_dict = copyReg_count(soup)
    icp_count_dict = icp_count(soup)
    seniorExecutive_count_dict = seniorExecutive_count(soup)
    holdingCompany_count_dict = holdingCompany_count(soup)
    announcement_count_dict = announcement_count(soup)
    shareholder_count_dict = shareholder_count(soup)
    tenTradable_shareholder_count_dict = tenTradable_shareholder_count(soup)
    issueRelated_count_dict = issueRelated_count(soup)
    shareStructure_count_dict = shareStructure_count(soup)
    equityChange_count_dict = equityChange_count(soup)
    bonusInfo_count_dict = bonusInfo_count(soup)
    allotmen_count_dict = allotmen_count(soup)
    volatility_count_dict = volatility_count(soup)
    companyInfo_count_dict = companyInfo_count(soup)

    the_count_info['staff'] = staff_count_dict['staff']
    the_count_info['holder'] = holder_count_dict['holder']
    the_count_info['invest'] = invest_count_dict['invest']
    the_count_info['changeinfo'] = changeinfo_count_dict['changeinfo']
    the_count_info['annualreport'] = annualreport_count_dict['annualreport']
    the_count_info['branch'] = branch_count_dict['branch']
    the_count_info['findHistoryRongzi'] = findHistoryRongzi_count_dict['findHistoryRongzi']
    the_count_info['findTeamMember'] = findTeamMember_count_dict['findTeamMember']
    the_count_info['getProductInfo'] = getProductInfo_count_dict['getProductInfo']
    the_count_info['findTzanli'] = findTzanli_count_dict['findTzanli']
    the_count_info['findJingpin'] = findJingpin_count_dict['findJingpin']
    the_count_info['lawSuit'] = lawSuit_count_dict['lawSuit']
    the_count_info['courtAnnouncement'] = courtAnnouncement_count_dict['courtAnnouncement']
    the_count_info['dishonest'] = dishonest_count_dict['dishonest']
    the_count_info['zhixinginfo'] = zhixinginfo_count_dict['zhixinginfo']
    the_count_info['abnormal'] = abnormal_count_dict['abnormal']
    the_count_info['illegalinfo'] = illegalinfo_count_dict['illegalinfo']
    the_count_info['equityInfo'] = equityInfo_count_dict['equityInfo']
    the_count_info['mortgageInfo'] = mortgageInfo_count_dict['mortgageInfo']
    the_count_info['ownTax'] = ownTax_count_dict['ownTax']
    the_count_info['bids'] = bids_count_dict['bids']
    the_count_info['bond'] = bond_count_dict['bond']
    the_count_info['purchaseLand'] = purchaseLand_count_dict['purchaseLand']
    the_count_info['employments'] = employments_count_dict['employments']
    the_count_info['taxCredit'] = taxCredit_count_dict['taxCredit']
    the_count_info['checkInfo'] = checkInfo_count_dict['checkInfo']
    the_count_info['appbkInfo'] = appbkInfo_count_dict['appbkInfo']
    the_count_info['tm'] = tm_count_dict['tm']
    the_count_info['patents'] = patents_count_dict['patents']
    the_count_info['copyReg'] = copyReg_count_dict['copyReg']
    the_count_info['icp'] = icp_count_dict['icp']
    the_count_info['seniorExecutive'] = seniorExecutive_count_dict['seniorExecutive']
    the_count_info['holdingCompany'] = holdingCompany_count_dict['holdingCompany']
    the_count_info['announcement'] = announcement_count_dict['announcement']
    the_count_info['shareholder'] = shareholder_count_dict['shareholder']
    the_count_info['tenTradable_shareholder'] = tenTradable_shareholder_count_dict['tenTradable_shareholder']
    the_count_info['issueRelated'] = issueRelated_count_dict['issueRelated_shareholder']
    the_count_info['shareStructure'] = shareStructure_count_dict['shareStructure_shareholder']
    the_count_info['equityChange'] = equityChange_count_dict['equityChange_shareholder']
    the_count_info['bonusInfo'] = bonusInfo_count_dict['bonusInfo_shareholder']
    the_count_info['allotmen'] = allotmen_count_dict['allotmen']
    the_count_info['volatility'] = volatility_count_dict['volatility']
    the_count_info['companyInfo'] = companyInfo_count_dict['companyInfo']
    return the_count_info











##########################################################################################################################################################
def change_a_new_Cookie(invalid_cookies):
    conn = pymysql.connect(host='192.168.1.89', port=3306, user='root', passwd='password', db='pe', charset='utf8')#设置charset来防止mongodb里面取到乱码
    cur = conn.cursor()#创建游标
    SQL_select_all_2 = "UPDATE sg_cookie SET status = 0 WHERE cookie = '{}'".format(invalid_cookies)
    print(SQL_select_all_2)
    cur.execute(SQL_select_all_2)
    conn.commit()
    cur.close()





def get_all_data_dict_str(company_code,the_cookies):
    all_data_dict = {}
    # company_code = request.form['cid']
    # the_cookies = request.form['Cookie']#selenium这个不需要cookie
    the_url = 'https://www.tianyancha.com/company/'+company_code
    equityRatio_url = 'https://www.tianyancha.com/equity/equityratio.json?id={}'.format(company_code)
    print('正在捉取的url是:',the_url)

    #取到网页源码以后可能有3种情况
    #1.Cookie时间太长失效的情形(不是弹出验证码),据观察天眼查里面的Cookie大约一周以后会失效
    #2.Cookie没有失效,但是请求的过于频繁,导致网页弹出源代码的情形
    #3.可以正常获取数据的情形

    # soup_main_page = get_page_source(the_url,the_cookies)
    baseinfo_dict = baseinfo(soup_main_page)
    main_staff = staff(soup_main_page)
    holder_info = holder(soup_main_page)
    invest_info = invest(soup_main_page)
    change_info = changeinfo(soup_main_page)
    annualreport_info = annualreport(company_code,the_cookies)
    branch_info = branch(soup_main_page)
    findHistoryRongzi_info = findHistoryRongzi(soup_main_page)
    findTeamMember_info = findTeamMember(soup_main_page)
    getProductInfo_info = getProductInfo(soup_main_page)
    findTzanli_info = findTzanli(soup_main_page)
    findJingpin_info = findJingpin(soup_main_page)
    # complete_lawsuit_urls_list = get_lawsuit_urls_list(soup_main_page)
    # print(complete_lawsuit_urls_list)
    # get_lawsuit_content(complete_lawsuit_urls_list)
    lawsuit_info = get_lawsuit_basic_info(soup_main_page)
    courtAnnouncement_info = courtAnnouncement(soup_main_page)
    dishonest_info = dishonest(soup_main_page)
    zhixinginfo_info = zhixinginfo(soup_main_page)
    abnormal_info = abnormal(soup_main_page)
    punishmentInfo_info = punishmentInfo(soup_main_page)
    illegalinfo_info = illegalinfo(soup_main_page)
    equityInfo_info = equityInfo(soup_main_page)
    mortgageInfo_info = mortgageInfo(soup_main_page)
    ownTax_info = ownTax(soup_main_page)
    bids_info = bids(soup_main_page,the_cookies)
    bond_info = bond(soup_main_page)
    purchaseLand_info = purchaseLand(soup_main_page)
    employments_info = employments(soup_main_page)
    taxCredit_info = taxCredit(soup_main_page)
    checkInfo_info = checkInfo(soup_main_page)
    appbkInfo_info = appbkInfo(soup_main_page)
    qualification_info = qualification(soup_main_page)
    tm_info = tm(soup_main_page)
    patents_info = patents(soup_main_page)
    copyReg_info = copyReg(soup_main_page)
    icp_info = icp(soup_main_page)
    volatility_info = volatility(soup_main_page)
    companyInfo_info = companyInfo(soup_main_page)
    seniorExecutive_info = seniorExecutive(soup_main_page)
    holdingCompany_info =  holdingCompany(soup_main_page)
    announcement_info = announcement(soup_main_page)
    shareholder_info = shareholder(soup_main_page)
    issueRelated_info = issueRelated(soup_main_page)
    shareStructure_info = shareStructure(soup_main_page)
    equityChange_info = equityChange(soup_main_page)
    bonusInfo_info = bonusInfo(soup_main_page)
    allotment_info = allotment(soup_main_page)###################
    # count_info = count(soup_main_page)
    equityRatio_info = equityRatio(equityRatio_url,the_cookies)
    count_info = the_new_count_info(soup_main_page)
    print(count_info)
    # updatetime = get_updatetime(soup_main_page)


    all_data_dict['baseinfo'] = baseinfo_dict#基本信息
    all_data_dict['staff'] = main_staff#主要人员
    all_data_dict['holder'] = holder_info#股东信息
    all_data_dict['invest'] = invest_info
    all_data_dict['changeinfo'] = change_info
    all_data_dict['annualreport'] = annualreport_info
    all_data_dict['branch'] = branch_info
    all_data_dict['findHistoryRongzi'] = findHistoryRongzi_info
    all_data_dict['findTeamMember'] = findTeamMember_info
    all_data_dict['getProductInfo'] = getProductInfo_info
    all_data_dict['findTzanli'] = findTzanli_info
    all_data_dict['findJingpin'] = findJingpin_info
    all_data_dict['lawSuit'] = lawsuit_info
    all_data_dict['courtAnnouncement'] = courtAnnouncement_info
    all_data_dict['dishonest'] = dishonest_info
    all_data_dict['zhixinginfo'] = zhixinginfo_info
    all_data_dict['abnormal'] = abnormal_info
    all_data_dict['punishmentInfo'] = punishmentInfo_info
    all_data_dict['illegalinfo'] = illegalinfo_info
    all_data_dict['equityInfo'] = equityInfo_info
    all_data_dict['mortgageInfo'] = mortgageInfo_info
    all_data_dict['ownTax'] = ownTax_info
    all_data_dict['bids'] = bids_info
    all_data_dict['bond'] = bond_info
    all_data_dict['purchaseLand'] = purchaseLand_info
    all_data_dict['employments'] = employments_info
    all_data_dict['taxCredit'] = taxCredit_info
    all_data_dict['checkInfo'] = checkInfo_info
    all_data_dict['appbkInfo'] = appbkInfo_info
    all_data_dict['qualification'] = qualification_info
    all_data_dict['tm'] = tm_info
    all_data_dict['patents'] = patents_info
    all_data_dict['copyReg'] = copyReg_info
    all_data_dict['icp'] = icp_info
    all_data_dict['volatility'] = volatility_info
    all_data_dict['companyInfo'] = companyInfo_info
    all_data_dict['seniorExecutive'] = seniorExecutive_info
    all_data_dict['holdingCompany'] = holdingCompany_info
    all_data_dict['announcement'] = announcement_info
    all_data_dict['shareholder'] = shareholder_info
    all_data_dict['issueRelated'] = issueRelated_info
    all_data_dict['shareStructure'] = shareStructure_info
    all_data_dict['equityChange'] = equityChange_info
    all_data_dict['bonusInfo'] = bonusInfo_info
    all_data_dict['allotment'] = allotment_info
    all_data_dict['count_info'] = count_info
    all_data_dict['equityRatio'] = equityRatio_info
    # all_data_dict['mysql_updatetime'] = updatetime


    all_data_dict_str = json.dumps(all_data_dict,ensure_ascii=False)
    # all_data_dict_str = str(all_data_dict)
    return all_data_dict_str




result = get_all_data_dict_str('176277626','aliyungf_tc=AQAAAON7dk61GAYAbfLidH9WUXRG/FVA;csrfToken=gwjM6R4GDpbk_LLWVahk0J5m;TYCID=9ecbde40977811e7b5e02bd9acd5314e;uccid=530df41ef52d5d353180b1c09cb2efb5;ssuid=1658604870;tyc-user-info={"token":"eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODcwMTc4MDI1MSIsImlhdCI6MTUwNTE5MjkxMywiZXhwIjoxNTIwNzQ0OTEzfQ.MtkEmRmavz0fFp1UXS4V1XtcF-FLRWo3F1bubfoJkbzwx_ndmyVg4FfB4Ky9vw800s0tT_8s1cxaYaqNkDRLDA","integrity":"0%","state":"0","vnum":"0","onum":"0","mobile":"18701780251"};auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxODcwMTc4MDI1MSIsImlhdCI6MTUwNTE5MjkxMywiZXhwIjoxNTIwNzQ0OTEzfQ.MtkEmRmavz0fFp1UXS4V1XtcF-FLRWo3F1bubfoJkbzwx_ndmyVg4FfB4Ky9vw800s0tT_8s1cxaYaqNkDRLDA;_csrf=j0BF7WMN0JgETy/uoLpHtA==;OA=YCBOCiyel30b/GvnGZdsuhTSyrHHzN3Y421rjNYpNag=;_csrf_bk=9e474d7ad73a2628f22bbde098f2a6fd;Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1505193001;Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1505193008')
print(result)
the_dict = eval(result)
print(the_dict)
print(the_dict['employments'][0]['experience'])

# while 1:
#     result = abnormal(soup_main_page)
#     print(result)
#     print('sss')
#     time.sleep(1)
# while 1:
#     result = abnormal(soup_main_page)
#     print(result)
#     time.sleep(1)


# print(len(result))
# for ele in result:
#     print(ele)
#     print(type(ele))
# print(result)
# str_1 = '   '
# print(str_1)
# print(len(str_1))

# import datetime
# print(datetime.date(2000,1,1))
# print(type(datetime.date(2000,1,1)))

# def get_updatetime(soup):
#     print('爬取更新时间！')
#     try:
#         updatetime = soup.find('span',class_ = 'updatetimeComBox').text
#
#     except Exception as e:
#         print('爬取为空！')
#         print(e)
#         return []
#     else:
#         return updatetime
#
#
#
# result = get_updatetime(soup_main_page)
# print(result)
# print(result)
# for ele in result:
#     print(ele)
# print(result)



# the_list = [11,22,33,44,55]
# for ele in the_list:
#     print(the_list.index(ele))
# import numpy as np
# import random
#
# # r = random.randint(4,4)
# # print(r)
# a = np.mat('1,2,2;6,6,2;1,5,1')
# print(a)
# a_inv = (a.I)
# print(a_inv)
# I = np.dot(a,a_inv)
#
# print(I)