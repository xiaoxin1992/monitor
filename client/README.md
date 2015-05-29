客户端程序


配置文件位置
./conf/config.py

配置实例
client_config = {
    'id':1,  #  客户端id  唯一的
    'host_info':"mysql server", # 服务器描述
    'command':{'cmd_name':'/root/cc.py','mysql status':'/root/mysql_alive.sh'} #添加监控脚本
}

配置完成后，把
./send_data 加入到crontab  中 ，时间间隔小于服务器接受数据的时间


手动测试
执行./send_data

crontab -e
*/2 * * * * $path/client/send_data
