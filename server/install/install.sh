#!/bin/bash
num=$(netstat -ano|grep mysql|grep -v grep|wc -l)
if [ $num -eq 0 ];then
    echo "mysql not install"
    exit 0
fi

mysql -h 127.0.0.1 -P 3306  -e "drop database monitor;"
mysql -h 127.0.0.1 -P 3306  -e "create database monitor;"
mysql -h 127.0.0.1 -P 3306 monitor < init.sql
