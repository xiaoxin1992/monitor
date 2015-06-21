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

bee-server start  启动服务

程序存放路径必须是
/data/monitor
目前，还没有写到配置文件






客户端程序


配置文件位置
./conf/config.py


配置完成后
启动服务
 bin 目录下

bee-client start


存放路径必须是/data/monitor
目前还没有写到配置文

