#encoding:utf8
import requests
from bs4 import BeautifulSoup
import pymongo
import time


MONGO_HOST = 'localhost'
MONGO_PORT = 27017
conn=pymongo.MongoClient(MONGO_HOST,MONGO_PORT)
db=conn.crawls_soccer #数据库的名字叫做crawls_soccer
COLLECTION_PREMIER_LEAGUE = 'premier_league'#表名



def sleep_3():
    print('现在准备抓取英超联赛数据,Sleep 3 seconds now!')
    time.sleep(3)
    print('现在开始抓取！')


def premier_league():
    sleep_3()
    URL = 'http://liansai.500.com/zuqiu-3822/jifen-9848/'
    r = requests.get(URL)
    html_source_code = r.text#取得网址的源代码
    soup = BeautifulSoup(html_source_code,'lxml')#添加一个解析器
    team_ranks_list = []#球队排名列表
    team_name_list = []#球队名称列表
    team_match_finished_list = []#完成的轮次
    win_list = []#赢球轮数
    draw_list = []#平局轮数
    lose_list = []#输球轮数
    goals_scored_list = []#进球数
    goals_lost_list = []#失球数
    list_5_1 = []#排名第1的球队的近5轮的战绩
    list_5_2 = []#排名第2的球队的近5轮的战绩
    list_5_3 = []
    list_5_4 = []
    list_5_5 = []
    list_5_6 = []
    list_5_7 = []
    list_5_8 = []
    list_5_9 = []
    list_5_10 = []
    list_5_11 = []
    list_5_12 = []
    list_5_13 = []
    list_5_14 = []
    list_5_15 = []
    list_5_16 = []
    list_5_17 = []
    list_5_18 = []
    list_5_19 = []
    list_5_20 = []
    list_5_list = []
    # print(soup.find_all('td')[146])

    # for links in soup.find_all('span')[90]:
    #     print(links.get('title'))
    for tags in(soup.find_all('td')[131:471:17]):
        team_ranks = (int(tags.text))#取得球队排名,转化成整型为了数据库方便进行排序
        team_ranks_list.append(team_ranks)
    # print(team_ranks_list)
    for tags in(soup.find_all('td')[132:472:17]):
        team_name = tags.text#取得球队名
        team_name_list.append(team_name)
    # print(team_name_list)
    for tags in(soup.find_all('td')[133:473:17]):
        team_match_finished = int(tags.text)#完赛轮数
        team_match_finished_list.append(team_match_finished)
    # print(team_match_finished_list)
    for tags in(soup.find_all('td')[134:474:17]):
        win = int(tags.text)#赢球论述
        win_list.append(win)
    # print(win_list)
    for tags in(soup.find_all('td')[135:475:17]):
        draw = int(tags.text)#平局轮数
        draw_list.append(draw)
    # print(draw_list)
    for tags in(soup.find_all('td')[136:476:17]):
        lose = int(tags.text)#输球轮数
        lose_list.append(lose)
    # print(lose_list)
    for tags in(soup.find_all('td')[137:477:17]):
        goals = int(tags.text)#进球数
        goals_scored_list.append(goals)
    # print(goals_scored_list)
    for tags in(soup.find_all('td')[138:478:17]):
        goals_lost = int(tags.text)#失球数
        goals_lost_list.append(goals_lost)
    # print(goals_lost_list)
    average_goals = [round(a,2) for a in list((float(a)/float(b) for a,b in zip(goals_scored_list,team_match_finished_list)))]#场均进球数
    # print(average_goals)
    average_lost_goals = [round(a,2) for a in list((float(a)/float(b) for a,b in zip(goals_lost_list,team_match_finished_list)))]#场均失球数
    # print(average_lost_goals)
    win_ratio = [round(a, 3) for a in list((float(a) / float(b) for a, b in zip(win_list, team_match_finished_list)))]#胜率
    # print(win_ratio)
    draw_ratio = [round(a, 3) for a in list((float(a) / float(b) for a, b in zip(draw_list, team_match_finished_list)))]#平率
    # print(draw_ratio)
    lose_ratio = [round(a, 3) for a in list((float(a) / float(b) for a, b in zip(lose_list, team_match_finished_list)))]#负率
    # print(lose_ratio)
    scores = [int(a)*3+int(b)*1 for a,b in zip(win_list,draw_list)]#积分
    # print(scores)
    # for tags in soup.find_all('span')[90:94]:
    #     print(tags.get('title'))
    for tags in soup.find_all('span')[90:94]:
        list_5_1.append(tags.get('title'))#排名第1的球队的最近战绩
    # print(list_5_1)
    for tags in soup.find_all('span')[99:103]:
        list_5_2.append(tags.get('title'))#排名第二的球队的最近5场战绩
    for tags in soup.find_all('span')[108:112]:
        list_5_3.append(tags.get('title'))
    for tags in soup.find_all('span')[117:121]:
        list_5_4.append(tags.get('title'))
    for tags in soup.find_all('span')[126:130]:
        list_5_5.append(tags.get('title'))
    for tags in soup.find_all('span')[135:139]:
        list_5_6.append(tags.get('title'))
    for tags in soup.find_all('span')[144:148]:
        list_5_7.append(tags.get('title'))
    for tags in soup.find_all('span')[153:157]:
        list_5_8.append(tags.get('title'))
    for tags in soup.find_all('span')[162:166]:
        list_5_9.append(tags.get('title'))
    for tags in soup.find_all('span')[171:175]:
        list_5_10.append(tags.get('title'))
    for tags in soup.find_all('span')[180:184]:
        list_5_11.append(tags.get('title'))
    for tags in soup.find_all('span')[189:193]:
        list_5_12.append(tags.get('title'))
    for tags in soup.find_all('span')[198:202]:
        list_5_13.append(tags.get('title'))
    for tags in soup.find_all('span')[207:211]:
        list_5_14.append(tags.get('title'))
    for tags in soup.find_all('span')[216:220]:
        list_5_15.append(tags.get('title'))
    for tags in soup.find_all('span')[225:229]:
        list_5_16.append(tags.get('title'))
    for tags in soup.find_all('span')[234:238]:
        list_5_17.append(tags.get('title'))
    for tags in soup.find_all('span')[243:274]:
        list_5_18.append(tags.get('title'))
    for tags in soup.find_all('span')[252:256]:
        list_5_19.append(tags.get('title'))
    for tags in soup.find_all('span')[261:265]:
        list_5_20.append(tags.get('title'))
    list_5_list.append(list_5_1)#每一只球队的最近战绩形成了一个list,把这20个list放进一个大的list里面,方便后边取
    list_5_list.append(list_5_2)
    list_5_list.append(list_5_3)
    list_5_list.append(list_5_4)
    list_5_list.append(list_5_5)
    list_5_list.append(list_5_6)
    list_5_list.append(list_5_7)
    list_5_list.append(list_5_8)
    list_5_list.append(list_5_9)
    list_5_list.append(list_5_10)
    list_5_list.append(list_5_11)
    list_5_list.append(list_5_12)
    list_5_list.append(list_5_13)
    list_5_list.append(list_5_14)
    list_5_list.append(list_5_15)
    list_5_list.append(list_5_16)
    list_5_list.append(list_5_17)
    list_5_list.append(list_5_18)
    list_5_list.append(list_5_19)
    list_5_list.append(list_5_20)
    # print(list_5_list)
    data_dict_list = [] #这里定义一个list来装字典,这个list里面的每一条元素是一个字典
    for i in range(20):
        item = dict()
        item['排名'] = team_ranks_list[i]
        item['队名'] = team_name_list[i]
        item['完赛'] = team_match_finished_list[i]
        item['胜'] = win_list[i]
        item['平'] = draw_list[i]
        item['负'] = lose_list[i]
        item['积分'] = scores[i]
        item['进球数'] = goals_scored_list[i]
        item['失球数'] = goals_lost_list[i]
        item['场均进球数'] = average_goals[i]
        item['场均失球数'] = average_lost_goals[i]
        item['胜率'] = win_ratio[i]
        item['平率'] = draw_ratio[i]
        item['负率'] = lose_ratio[i]
        item['最近5场比赛战绩'] = list_5_list[i]
        data_dict_list.append(item)
    # print(data_dict_list)
    for item in data_dict_list:
        print(item)#打印出抓取的内容
        db[COLLECTION_PREMIER_LEAGUE].update_one({'队名':item['队名']}, {'$set': item}, upsert=True)
    print('抓取英超联赛积分榜完毕！！')






        # for links in soup.find_all('td'):
    #     # if ''
    #     # print(links.text,links.get('href'))
    #     print(links.text)

        # print(links.get('href'))



premier_league()





