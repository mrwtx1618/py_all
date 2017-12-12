#encoding:utf8
import requests
from bs4 import BeautifulSoup
import time
today = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))



def SZS_Announcement():
	SH_URL = 'http://www.sse.com.cn/disclosure/listedinfo/announcement/s_docdatesort_desc_2016openpdf.htm' #https://mobile.188-sb.com/default.aspx?lng=2&zn=0&apptype=&appversion=&rnd=40821#type=Coupon;key=15323868262C1_10_0;
	s = requests.session() #先初始化一个session对象，然后用这个session对象进行访问
	req = s.get(SH_URL)
	html = req.content.decode('utf-8')
	soup = BeautifulSoup(html,'lxml')
	data = soup.find_all('em')
	#data = [x.a for x in data]
	#data = [{'url':x['href'], 'title':x['title'],'code':x.get_text().split(':')[0], 'updateTime':today} for x in data]
	print data
	# print soup

SZS_Announcement()




