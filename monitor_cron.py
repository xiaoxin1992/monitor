#! /usr/bin/evn python
#! _*_coding:utf8 _*_
"""
监控插件调度程序
"""

import subprocess
import json,sys

conf_file = "./conf/cmd_exec.conf"


def cmd_exec(cmd):
    data = subprocess.Popen(cmd.strip(),shell=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    (stdoutdata,stderrdata)=data.communicate()
    return (stdoutdata,data.returncode)


#print exec_data

