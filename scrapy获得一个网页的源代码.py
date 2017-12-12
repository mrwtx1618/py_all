# -*- coding: utf-8 -*-
#通过cmd行命令来创建这个基础的spider，然后再在这个spider的基础之上进行改写
#www.dmoz.org/Computers/Programming/Languages/Python/Books/
#www.dmoz.org/Computers/Programming/Languages/Python/Resources/
import scrapy


class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.org"]
    start_urls = ('http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
    			  'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
    			  'http://www.sohu.com/',
    			  'https://www.bet365.com/#/IP/'
    	)

    def parse(self, response):
        filename = response.url.split('/')[-2] + ".html"
        with open(filename,'wb') as fp:
        	fp.write(response.body)

#完成了爬取以上两个网页的源代码        	
# -*- coding: utf-8 -*-
#通过cmd行命令来创建这个基础的spider，然后再在这个spider的基础之上进行改写
#www.dmoz.org/Computers/Programming/Languages/Python/Books/
#www.dmoz.org/Computers/Programming/Languages/Python/Resources/
import scrapy


class DmozSpiderSpider(scrapy.Spider):
    name = "dmoz_spider"
    allowed_domains = ["dmoz.org"]
    start_urls = ('http://www.dmoz.org/Computers/Programming/Languages/Python/Books/',
                  'http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/',
                  'http://www.sohu.com/',
                  'https://www.bet365.com/#/IP/'
        )

    def parse(self, response):
        filename = response.url.split('/')[-2] + ".html"
        with open(filename,'wb') as fp:
            fp.write(response.body)

#完成了爬取以上两个网页的源代码            
