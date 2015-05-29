#!/usr/bin/env python
# coding=utf-8
sock_config = {
        'server_ip':'127.0.0.1', #远程服务器ip
        'server_port':45100 #远程服务器端口
}
client_config = {
    'id':1,
    'host_info':"mysql server", #服务器描述
    'command':{
        'cmd_name':'/root/cc.py', #cmd_name监控名称,监控脚本
        'mysql status':'/root/mysql_alive.sh', 
        'ntp':'/root/ntp.sh'}

}
