#转换时间格式,把一个时间戳转换为yyyymmdd格式
def timetran(t):
    timestamp = t #t是一个时间戳,
    timearray = time.localtime(timestamp)
    the_time = time.strftime("%Y-%m-%d",timearray)
    return the_time