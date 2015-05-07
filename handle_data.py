#! /usr/bin/evn python
#! _*_coding:utf-8 _*_
"""
用于处理采集的数据，并调用发送模块
"""
import json,sys
cron_status = "./tmp/monitor_cron.status"
cron_data = "./tmp/monitor_info.dat"
def json_dumps(data):
    data_string = json.dumps(data)
    return data_string



with open(cron_data) as f:
    data =f.read()



for x in data.split('+'):
    print x
    b = json.loads(x.strip())
    break



#print b



