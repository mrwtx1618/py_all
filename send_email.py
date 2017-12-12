#encoding:utf8
import smtplib #smtplib提供了一种方便的途径发送电子邮件，对smtp协议进行了简单的封装
from email.mime.text import MIMEText
import os
_user = "2191667180@qq.com"
_pswd = "uqkeexhtomnfebce"
_to = "742750341@qq.com"

#使用MIMEText构造符合smtp协议的header及body
msg = MIMEText("利用python自动发送一封试验邮件http://blog.csdn.net/menglei8625/article/details/7721746")
msg["Subject"] = "This is a test email"
msg["From"] = _user
msg["To"] = _to

s = smtplib.SMTP_SSL("smtp.qq.com", 465) #连接smtp邮件服务器，端口默认是25
s.login(_user, _pswd) #登录服务器
s.sendmail(_user, _to, msg.as_string())
s.quit()
os.system('pause')


'''
SMTP(Simple Mail Transfer Protocol)
邮件传送代理(Mail Transfer Agent,MTA)程序使用SMTP协议来发送电子邮件到接收者
的邮件服务器。
SMTP协议只能用来发送邮件，不能用来接收邮件
大多数的邮件发送服务器(Outgoing Mail Server)都是使用SMTP协议。
SMTP协议的默认TCP端口号是25
'''






























