# -*- coding: utf-8 -*-
import time
import datetime





def getyesterday():
    today = datetime.date.today()
    unt_yesterday = today - datetime.timedelta(days=1)
    #转换为字符，分片处理
    unt_yesterday = str(unt_yesterday)
    (timeyear, timemon, timeday) = unt_yesterday.split("-")
    #月份去0处理
    timemon = int(timemon)
    #返回格式yyyy-mm-dd
    yesterday = str(timeyear)+'-'+str(timemon)+'-'+str(timeday)
    return yesterday



getyesterday()
