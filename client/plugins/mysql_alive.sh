#!/bin/bash
export LANG=zh_cn.utf-8
command_rel=$(mysqladmin -h 127.0.0.1 ping)
if [ "$command_rel" == "mysqld is alive" ];then
    echo $command_rel
    exit 0
else
    echo "mysql is shutdown"
    exit 1
fi
