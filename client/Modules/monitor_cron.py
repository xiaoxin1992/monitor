#! /usr/bin/evn python
#! _*_coding:utf8 _*_

"""
监控插件调度程序
"""
import subprocess
import json,sys,os,time,log
from conf.config import srcipt,plugin_directory,info
from handle_data import send_data
from stat import ST_MODE
def check_srcipt_path():
    srcipt_list = []
    if not os.path.exists(plugin_directory):
        log.log("%s Does not exist" % plugin_directory)
        sys.exit(-1)
    for k,v in srcipt.items():
        srcipt_path = os.path.join(plugin_directory,v)
        if  os.path.exists(srcipt_path) :  
            if int(oct(os.stat(srcipt_path)[ST_MODE])[-3:]) not in [755,555,655]:
                log.log("%s No execute permissions (limits 755)" % srcipt_path)
            else:
               srcipt_list.append(k) 
        else:
            log.log("%s Does not exist" % srcipt_path)
            
    return srcipt_list
def write_data(file,data,write_type='w'):
    try:
        f = open(file,write_type)
        f.write(data)
        f.close()
    except Exception,e:
        log.log(e)
        return 1
def cmd_exec(cmd):
    data = subprocess.Popen(cmd.strip(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (stdoutdata,stderrdata)=data.communicate()
    return (stdoutdata,data.returncode)

def update_data():
    main_path = os.path.dirname(sys.path[0].strip())
    cron_status = os.path.join(main_path,"tmp/monitor_cron.status")
    cron_data = os.path.join(main_path,"tmp/monitor_info.dat")
    if not os.path.exists(os.path.join(main_path,"tmp")):
        try:
            os.mkdir(os.path.join(main_path,"tmp"))
        except Exception,e:
            log.log(e)
            sys.exit(-1)
    data_list = []
    write_data(cron_status,'1',write_type='w')
    srcipt_ok = check_srcipt_path()
    for k,v in srcipt.items():
        if k not in srcipt_ok:
            continue
        command_line = cmd_exec(os.path.join(plugin_directory,v))
        data_list.append({'type':'plugin','id':info['id'],'host_info':info['information'],'script_name':"%s" % k,'data':"%s" % command_line[0],'code':"%s" % command_line[1]})
    if data_list.__len__(): 
        write_data(cron_data,json.dumps(data_list,ensure_ascii=False),write_type='w')
        write_data(cron_status,'0',write_type='w')

def check_data():
    while True:
        try:
            update_data()
            send_data()
            time.sleep(int(info['submitted']))
        except Exception,e:
            log.log(e)
            break

