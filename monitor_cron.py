#! /usr/bin/evn python
#! _*_coding:utf8 _*_

"""
监控插件调度程序
"""
import subprocess
import json,sys,os

conf_file = "./conf/cmd_exec.conf"
cron_status = "./tmp/monitor_cron.status"
cron_data = "./tmp/monitor_info.dat"
try:
    with open(conf_file) as f:
	    data = f.read()
except IOError,e:
    print e
    sys.exit(-1)
try:
    json_data = json.loads(data)
except ValueError,e:
    print e


def cmd_exec(cmd):
    data = subprocess.Popen(cmd.strip(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (stdoutdata,stderrdata)=data.communicate()
    return (stdoutdata,data.returncode)


for k,v in json_data.items():
    command_line = cmd_exec(v)
    f = open(cron_status,'w')
    f.write('1')
    f.close()
    f = open(cron_data,'a')
    cmd_data = {
	'name':"%s" % k,	
	'data':"%s" % command_line[0],
	'code':"%s" % command_line[1]
    }
    f.write("%s+" % cmd_data)
    f.close() 
