# coding = utf-8

import sys
import urllib2
import json
from datetime import date, time, datetime, timedelta

class No2API:

    def __init__(self, cityname = "beijing", token = "5j1znBVAsnSf5xQyNQyq"):
        self.city = cityname
        self.token = token
        self.url = "http://www.pm25.in/api/querys/no2.json?city="+ cityname + "&token=" + token
        self.url_all = "http://pm25.in/" + cityname
        self.timeformat = "%Y-%m-%d %X"
        self.pullData = []
    def startRequest(self):
        try:
            request = urllib2.Request(self.url)
            response = urllib2.urlopen(request)
            self.pullData = json.load(response, encoding = "utf-8")
            print "pulling NO2 data from pm25.in...."

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "URLopen error, reason:", e.reason
        if (len(self.pullData)< 13):
            print "The length of data is out of my expectation"

    def saveDataLog(self, filename = "NO2APIDATALOG.txt"):
        fpoint = open(filename, 'a')
        print "writing data log to:",filename
        for station in self.pullData:
            for item in station:
                print >> fpoint, item
                if(type(station[item]) == int):
                    print >> fpoint, station[item]
                elif(station[item] == None):
                    print >> fpoint, "None"
                else:
                    print >> fpoint,station[item].encode('gbk')
            print >> fpoint, "\n"
        print >> fpoint, "##########","pulling at:",datetime.now().strftime(self.timeformat),"##########","\n"
        fpoint.close()

    def saveNO2Data(self, filename = "NO2DATA.txt"):
        fno2 = open(filename, 'a')
        print "writing NO2 data to:", filename
        for station in self.pullData:
            no2_24h = station['no2_24h']
            no2 = station['no2']
            timepoint = station['time_point']
            no2_24h = str(no2_24h).decode('utf-8')
            no2 = str(no2).decode('utf-8')
            location = station['position_name']
            
            if (location == None):
                location = str(location).decode('utf-8')
            
            one_line = location + u',' + no2_24h + u',' + no2 + u',' + timepoint
            print >> fno2, one_line.encode('gbk')
        print >> fno2, "##########","pulling at:",datetime.now().strftime(self.timeformat),"##########","\n"
            
    
    def runspy(self):
        self.startRequest()
        self.saveNO2Data(filename = "NO2DATA.txt")
        self.saveDataLog(filename = "NO2APIDATALOG.txt")
        



def runtask(func, day=0, hour = 1, minute = 0, second = 0):

    now = datetime.now()
    str_now = now.strftime('%Y-%m-%d %H:%M:%S')
    print "Current time:%s\n" %str_now
    period = timedelta(days = day, hours = hour, minutes = minute, seconds = second)
    next_time = now + period
    str_next_time = next_time.strftime('%Y-%m-%d %H:%M:%S')
    print "Next run will start in:%s\n" %str_next_time
    while True:
        iter_now = datetime.now()
        str_iter_now = iter_now.strftime('%Y-%m-%d %H:%M:%S')
        if str(str_iter_now) == str(str_next_time):
            print "Start Runing task....%s\n" %str_iter_now
            func()
            print "Task Done!\n"
            iter_time = iter_now + period
            str_next_time = iter_time.strftime('%Y-%m-%d %H:%M:%S')
            print "Next run will start in:%s\n" %str_next_time
            continue
            
