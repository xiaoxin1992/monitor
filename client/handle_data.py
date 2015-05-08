#! /usr/bin/evn python
#! _*_coding:utf-8 _*_
"""
用于处理采集的数据，并调用发送模块
"""
import sys,client
cron_status = "./tmp/monitor_cron.status"
cron_data = "./tmp/monitor_info.dat"
with open(cron_data) as f:
    data =f.read()
with open(cron_status,'r') as s_f:
    status = s_f.read()
if int(status.strip()) is not 0 or not data:
    sys.exit(0)
if client.send_data(data) is 0:
    f = open(cron_data,'w')
    f.write('')
    f.close()
    print "send ok"  


