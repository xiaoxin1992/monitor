# monitor
主要用于监控Linux 操作系统的系统状态
程序分为client 和server
server 接受数据并且存入mysql数据中
client 可以根据指定的插件采集数据发送到服务端






服务端说明
配置文件路径 config/config.py
启动脚本
mtstart start
mtstart stop

需要安装mysql数据库
需要安装MySQL-python.rpm 包


初始化
执行 install/init.sql  进行数据库初始化
然后执行
mtstart start  启动服务







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
