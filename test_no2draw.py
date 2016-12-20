from datetime import date, time, datetime, timedelta
from no2drawoneday import *

now = datetime.now()
str_now = now.strftime('%Y-%m-%d %H:%M:%S')
print "Current time:%s\n" %str_now
period = timedelta(days = 0, hours = 12, minutes = 0, seconds = 0)
next_time = now + period
str_next_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
print "Next run will start in:%s\n" %str_next_time
while True:
        iter_now = datetime.now()
        str_iter_now = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(str_iter_now) == str(str_next_time):
            print "Start Runing task....%s\n" %str_iter_now
            period_str = iter_now - timedelta(days = 1)
            period_str = period_str.strftime('%Y-%m-%d')
            drawOneDay("NO2DATA.txt", period_str)
            print "Task Done!\n"
            iter_time = iter_now + period
            str_next_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print "Next run will start in:%s\n" %str_next_time
            continue
