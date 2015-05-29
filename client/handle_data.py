#! /usr/bin/evn python
#! _*_coding:utf-8 _*_
"""
用于处理采集的数据，并调用发送模块
"""
import sys,client
main_path = sys.path[0]
cron_status = main_path + "/tmp/monitor_cron.status"
cron_data = main_path +"/tmp/monitor_info.dat"
with open(cron_data) as f:
    data =f.read()
with open(cron_status,'r') as s_f:
    status = s_f.read()
if len(status) == 0:
    f  = open(cron_status,'w')
    f.write('0')
    f.close()
    sys.exit(1)
if int(status.strip()) is not 0 or not data:
    sys.exit(0)
if client.send_data(data) is 0:
    f = open(cron_data,'w')
    f.write('')
    f.close()
    print "send ok"  


