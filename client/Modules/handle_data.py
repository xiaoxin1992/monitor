#! /usr/bin/evn python
#! _*_coding:utf-8 _*_
"""
用于处理采集的数据，并调用发送模块
"""
import sys,client,os
import log
def send_data():
    main_path = os.path.dirname(sys.path[0].strip())
    cron_status = main_path + "/tmp/monitor_cron.status"
    cron_data = main_path +"/tmp/monitor_info.dat"
    
    with open(cron_data) as f:
        data = f.read()
    with open(cron_status,'r') as s_f:
        status = s_f.read()
    if len(status) == 0:
        try:
            f  = open(cron_status,'w')
            f.write('0')
            f.close()
        except Exception,e:
            log.log(e)
        sys.exit(1)
    if int(status.strip()) is not 0 or not data.__len__():
        log.log('Not collect data')
        return 0
   
    if client.send_data(data) is 0:
        try:
            f = open(cron_data,'w')
            f.write('')
            f.close() 
        except Exception,e:
            log.log(e)
            sys.exit(1)


