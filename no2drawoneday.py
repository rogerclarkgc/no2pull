# -*- coding: gbk -*- 
import string
from datetime import date, time, datetime, timedelta
from pandas import Series, DataFrame
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt

def drawOneDay(filename, period):
    now = datetime.now()
    #str_now = now.strftime('%Y-%m-%d')
    data = open(filename, "r+")
    location = ["奥体中心", "昌平镇", "定陵", "东四", "古城", "官园", "海淀区万柳",
            "怀柔镇", "农展馆", "顺义新城", "天坛", "万寿西宫", "None"]
    PNGPATH = 'E:/no2data/'
    TXTPATH = 'E:/no2data/txtfile/'
    for line in data.readlines():
        for loc in location:
            if (string.find(line, loc)!=-1):
                filename = TXTPATH + loc + period + ".txt"
                file_loc = open(filename, "a")
                print >> file_loc, line
                file_loc.close()
    data.close()

    count = 1
    for loc in location:
        tablename = TXTPATH + loc + period + ".txt"
        loc_data = open(tablename, "r+")
        loc_alllines = loc_data.readlines()
        loc_data.close()
        no21h = []
        timestamp = []

        for ob in loc_alllines:
            if (ob != '\n') & (string.find(ob, period)!=-1):
                obsplit = string.split(ob, sep = ',')
                no21h.append(int(obsplit[2]))
                t1 = datetime.strptime(obsplit[-1], '%Y-%m-%dT%H:%M:%SZ\n')
                timestamp.append(t1)
        loc_dict = {'no2.1h':no21h,
                'time':timestamp}
        loc_fram = DataFrame(loc_dict, index = timestamp)
        plt.figure(count)
        temp = loc_fram['no2.1h'].plot(title = period)
        temp.set_xlabel('time')
        temp.set_ylabel('No2/microgram')
        pngname = PNGPATH + loc + period + ".png"
        plt.savefig(pngname)
        plt.close(count)
        count += 1
