#! coding=UTF8

"""
服务器主配置文件
"""
client_root = '/data/monitor/client'
log_file = """%s%s""" % (client_root,'/log/client.log')
CONNECT = "0.0.0.0:45100"
info = {
        'id':1,
        'information':'mysql server',
        'submitted':10
}
plugin_directory = """%s%s""" % (client_root,'/plugins')
srcipt = {
          'cmd_nama':'cc.py',
          'mysql status':'mysql_alive.sh'
}

sock_config = {
        'server_ip':'127.0.0.1', #远程服务器ip
        'server_port':45100 #远程服务器端口
}
client_config = {
    'id':1,
    'host_info':"mysql server", #服务器描述
    'send_time':30,           # 单位秒
    'command':{
        'cmd_name':'/root/cc.py', #cmd_name监控名称,监控脚本
        'mysql status':'/root/mysql_alive.sh' 
        }

}
