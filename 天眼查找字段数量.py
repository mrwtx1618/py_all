#encoding:utf-8


import requests
from bs4 import BeautifulSoup
import time

the_url = 'https://www.tianyancha.com/company/22822'
the_cookies = 'TYCID=9b93e2e078ba11e7b908f565a2117175; uccid=ea09126cde05fc87d81f8231a5e8dc9c; RTYCID=7bdf957e6de34780ba0280def398e1e1; aliyungf_tc=AQAAAFoIDBcgQwoAbfLidGaK0vPf6Pzl; csrfToken=drNMUUKES3Dwz4AE_BNBNm8c; tyc-user-info=%257B%2522token%2522%253A%2522eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwMzM3MDUzMiwiZXhwIjoxNTE4OTIyNTMyfQ.M_CT6li2jBPN7PgsPk7zdS6HNNfF9Y420EtQ6fGECDD2jJa5MseyNfKBGGL7aA_Z1L9cMO6eEDgTZgdvV4pqEw%2522%252C%2522integrity%2522%253A%25220%2525%2522%252C%2522state%2522%253A%25220%2522%252C%2522vnum%2522%253A%25220%2522%252C%2522onum%2522%253A%25220%2522%252C%2522mobile%2522%253A%252213611835756%2522%257D; auth_token=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzYxMTgzNTc1NiIsImlhdCI6MTUwMzM3MDUzMiwiZXhwIjoxNTE4OTIyNTMyfQ.M_CT6li2jBPN7PgsPk7zdS6HNNfF9Y420EtQ6fGECDD2jJa5MseyNfKBGGL7aA_Z1L9cMO6eEDgTZgdvV4pqEw; _csrf=Nf/vU1W/Xnnh8gIlxPGDCg==; OA=E4eh3tNl9NWarJ4Y31bZEXo/aZpS/hTDM4dsXJuIIF/mEYkUuwHEW+l/Qn8H0jeb; _csrf_bk=14dcc8b2a1f29fcfe82b9bf277123665; Hm_lvt_e92c8d65d92d534b0fc290df538b4758=1502676268,1503281645,1503299041,1503370496; Hm_lpvt_e92c8d65d92d534b0fc290df538b4758=1503370518'


def get_page_source(need_url,need_cookies):
    proxy = {'http': 'http://110.73.15.65:8123'}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22 Safari/537.36 SE 2.X MetaSr 1.0','Referer':'https://www.tianyancha.com/search?key=%E4%B8%8A%E6%B5%B7%E7%86%99%E9%A3%8E%E7%94%B5%E5%AD%90%E5%95%86%E5%8A%A1%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&checkFrom=searchBox','Cookie':need_cookies}
    html = requests.get(need_url, headers=headers,proxies = proxy)
    soup = BeautifulSoup(html.content, 'lxml')
    return soup





def count(soup):
    print('个数！')
    try:
        result = []
        # print(soup)
        # the_soup = soup.find('div',attrs={'class':''})
        # the_soup_soup = soup.find('div',class_ = "b-c-white new-border position-rel")
        # print(the_soup_soup)
        the_soup_1 = soup.find_all('div', attrs={'class': 'company-nav-item-enable canClick'})
        data_list_enable = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_1]
        the_soup_2 = soup.find_all('div', attrs={'class': 'company-nav-item-disable'})
        data_list_disabled = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_2]
        # print(data_list_enable)
        # print(data_list_disabled)
        data_list_with_0 = [ele[:-1] for ele in data_list_disabled if ele[-1]=='0']
        data_list_with_none_1 = [ele for ele in data_list_disabled if ele[-1] !='0']
        print('0000000000000000000000000000000000000000000000000000000000',data_list_with_0)#数字为0的
        # print(data_list_with_none_1)#disable里面没有数字的
        the_soup_num = soup.find_all('span',class_ ='c9')
        the_num_list = [x.text.replace(' ', '').replace('\n', '').replace('>', '').strip() for x in the_soup_num]

        data_list_with_none_2 = [ele for ele in data_list_enable if ele[-1] not in ['0','1','2','3','4','5','6','7','8','9','+']]
        # print(data_list_with_none_2)
        data_list_with_none_all = data_list_with_none_1+data_list_with_none_2#所有的没有数字的
        print('nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn',data_list_with_none_all)
        print(the_num_list)
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

soup_main_page = get_page_source(the_url,the_cookies)
count_info = count(soup_main_page)

# print(count_info)


print(soup_main_page.prettify())





