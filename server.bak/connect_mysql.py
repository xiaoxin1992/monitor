#!/usr/bin/env python
# coding=utf-8
"""
用于连接对mysql数据库进行操作
"""
import MySQLdb
HOST="127.0.0.1"
PORT=3306
USER="root"
PASSWORD=""
DB_NAME="mysql"
MySQLdb.connect(host=HOST,port=PORT,user=USER,passwd=PASSWORD,db=DB_NAME)
