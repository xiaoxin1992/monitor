# monitor
主要用于监控Linux 操作系统的系统状态
程序分为client 和server
server 接受数据并且存入mysql数据中
client 可以根据指定的插件采集数据发送到服务端






服务端说明
配置文件路径 config/config.py
启动脚本

需要安装mysql数据库
需要安装MySQL-python.rpm 包


初始化
执行 install/init.sql  进行数据库初始化
然后执行
monitorstart start  启动服务







客户端程序


配置文件位置
./conf/config.py


配置完成后
启动服务
 bin 目录下
 ./monitor_clinet  start／stop/ restart


