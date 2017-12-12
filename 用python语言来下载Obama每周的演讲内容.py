# -*- coding: UTF-8 -*-
"""首先打开这个目录页, 并且保存在content"""
import sys                                                              #系统函数模块
import urllib                                                           #url模块
url = "http://www.putclub.com//html/radio/presidentspeech/index.html"   #从网站的源代码中提取到url 把最后换成index
webpage = urllib.urlopen(url)                                           #打开一个url的方法，返回一个文件对象，然后可以进行类似文件对象的操作
print "Start Download..."                                               #显示开始下载
content = webpage.read()                                                #读取网页的内容
"""下面要做的是提取每一篇演讲的内容：具体思路是：搜索“center_box”之后，每个“href=”和“target”之间的内容。为什么是这两个之间，请看网页源码。

得到的就是每一篇的url，再在前面加上www.putclub.com就是每一篇文章的网址啦"""
print content.count("center_box")                                       #这句语句的运行结果是1 实际上打印出了内容里含有“center_box”的个数
index = content.find("center box")                                      #从这个网页的内容中来寻找带有"center box"的内容
content = content[content.find("center_box")+1:]
content = content[content.find("href=")+7:content.find("target")-2]
filename = content
url = "http://www.putclub.com/"+content
print content
print url
webpage = urllib.urlopen(url)
print "start download!"
content = webpage.read()
"""有了文章的url之后，同样的方法可以筛选内容"""
#print content
print content.count("<div class=\"content\"")
#content = content[content.find(",div class=\"content\""):]
content = content[content.find("<!--info end------->"):]
content =content[:content.find("<div class=\"dede_pages\"")-1]
filename = filename[filename.find("presidentspeech")+len("presidentspeech/"):]
"""最后保存并打印"""
filename = filename.replace('/',"-",filename.count("/"))
fp = open(filename,"w+")
fp.write(content)
fp.close
print content
