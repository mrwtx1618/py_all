#encoding:utf8
import logging  
logging.debug('debug message')  
logging.info('info message')  
logging.warning('warning message')  
logging.error('error message')  
logging.critical('critical message')  
'''
可见，默认情况下python的logging模块将日志打印到了标准输出中，且只显示了大于等于WARNING级别的日志，
这说明默认的日志级别设置为WARNING（日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET），
默认的日志格式为:
日志级别：Logger名称：用户输出消息
'''















































