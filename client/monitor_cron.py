#! /usr/bin/evn python
#! _*_coding:utf8 _*_

"""
监控插件调度程序
"""
import subprocess
import json,sys,os
from conf.config import client_config
main_path = sys.path[0]
cron_status = main_path + "/tmp/monitor_cron.status"
cron_data = main_path + "/tmp/monitor_info.dat"
def cmd_exec(cmd):
    data = subprocess.Popen(cmd.strip(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (stdoutdata,stderrdata)=data.communicate()
    return (stdoutdata,data.returncode)

data_list = []
f = open(cron_status,'w')
f.write('1')
f.close()
for k,v in client_config['command'].items():
    command_line = cmd_exec(v)
    data_list.append({'id':client_config['id'],'host_info':client_config['host_info'],'cmd_name':"%s" % k,'data':"%s" % command_line[0],'code':"%s" % command_line[1]})
f = open(cron_data,'a')
f.write(json.dumps(data_list))
f.close()
f = open(cron_status,'w')
f.write('0')
f.close()
