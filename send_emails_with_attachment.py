#encoding:utf8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
import os
import datetime
import string
_user = "742750341@qq.com"
_pswd = "aabdllslwtsnbcee"
_to = "sogukeji@163.com, lijh@doudouxing.com, 742750341@qq.com, 13110180012@fudan.edu.cn"
_to = _to.split(",")
today = datetime.date.today()


msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = '%s选股票'%today
msgTxt = MIMEText("今天选取的股票")
msgRoot["From"] = _user
#msgRoot["To"] = _to

#添加附件,jpg类型的图片
#f1 = open('aaa.jpg','rb')
#msgimg = MIMEImage(f1.read())
#f1.close()
#msgimg.add_header('Content-Disposition', 'attachment', filename = 'aaa.jpg')
#msgRoot.attach(msgimg)
msgRoot.attach(msgTxt)


#添加附件,xlsx类型的附件，任何类型的附件都可以用MIMEApplication
f2 = open('%sstock.xlsx'%today,'rb')
msgexl = MIMEApplication(f2.read())
f2.close()
msgexl.add_header('Content-Disposition','attachment',filename = '%sstock.xlsx'%today)
msgRoot.attach(msgexl)

# part = MIMEText(open('aaa.jpg','rb').read(),'base64','utf-8')
# part["Content-Type"] = 'application/octet-stream'
# part["Content-Disposition"] = "attachment;filename = 'aaa.jpg'"
# print part
# msg.attach(part)

s = smtplib.SMTP_SSL("smtp.qq.com", 465)
s.login(_user, _pswd) #登录服务器
s.sendmail(_user, _to, msgRoot.as_string())
s.quit()
#os.system('pause')


'''
SMTP(Simple Mail Transfer Protocol)
邮件传送代理(Mail Transfer Agent,MTA)程序使用SMTP协议来发送电子邮件到接收者
的邮件服务器。
SMTP协议只能用来发送邮件，不能用来接收邮件
大多数的邮件发送服务器(Outgoing Mail Server)都是使用SMTP协议。
SMTP协议的默认TCP端口号是25
'''






























