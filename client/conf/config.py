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


