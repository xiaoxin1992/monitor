#!/usr/bin/env python
# coding=utf-8
server_global={
    #全局配置，主要服务端配置
    #listen_ip   监听IP
    #listen_port 监听端口
    #log_path     存放日志路径
    #databases 数据库相关设置
    #    db_host  数据库IP
    #    db_port  数据库端口
    #    db_user 数据库用户名
    #    db_pass 数据库密码
    #    db_name  数据库名
    'listen_ip':'0.0.0.0',
    'listen_port':45100,
    'log_path':'/log/start.log',
    'databases':{'db_host':'127.0.0.1','db_port':'3306','db_user':'root'
                 ,'db_pass':'','db_name':'monitor'}
    
}
contacts = {
        #联系人配置
        #smtp_server  stmp服务器
        #smtp_port  端口
        #smtp_user 登陆用户名
        #smtp_pass 登陆密码
        #smtp_show_name 发信件显示名称
        #to_mail  发送到那个邮箱可以写多个，中间以','隔开
        'smtp_server':'smtp.qq.com',
        'smtp_port':25,
        'smtp_user':'xxxx@qq.com',
        'smtp_pass':'xxxxxxx',
        'smtp_show_name':'监控邮箱',
        'to_mail':'xxx@qq.com,xxxxx@163.com'
}
timeout_set = {
               'check_host_time':300, #主机超市时间
               'check_server_time':300, #服务超时时间
               'send_mail_time':300 #发送告警邮件间隔
               }
