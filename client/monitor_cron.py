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
    sys.exit()


def cmd_exec(cmd):
    data = subprocess.Popen(cmd.strip(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (stdoutdata,stderrdata)=data.communicate()
    return (stdoutdata,data.returncode)

data_list = []
f = open(cron_status,'w')
f.write('1')
f.close()
for k,v in json_data['command'].items():
    command_line = cmd_exec(v)
    data_list.append({'id':json_data['id'],'host_info':json_data['host_info'],'cmd_name':"%s" % k,'data':"%s" % command_line[0],'code':"%s" % command_line[1]})
f = open(cron_data,'a')
f.write(json.dumps(data_list))
f.close()
f = open(cron_status,'w')
f.write('0')
f.close()
