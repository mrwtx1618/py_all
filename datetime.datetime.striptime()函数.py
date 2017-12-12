import datetime
import time
date_str = '20040130190102.mmm'
correct_date_format = datetime.datetime.strptime('20040130190102.mmm','%Y%m%d%H%M%S.mmm')
print correct_date_format
print correct_date_format.timetuple()
unix_time = time.mktime(correct_date_format.timetuple())
print unix_time










