#! /usr/bin/env python
# coding:utf-8

import MySQLdb,log
from conf.config import server_global


"""
myqsl 操作模块
a = mysql()
a.connect()
a.select("select  * from monitor_host_info")
a.insert_update_delete("insert into monitor_host_info values(1,'127.0.0.1','1');")
a.close()
"""

DB_HOST = server_global['databases']['db_host']
DB_PORT = int(server_global['databases']['db_port'])
DB_USER = server_global['databases']['db_user']
DB_PASS = server_global['databases']['db_pass']
DB_DATABASE= server_global['databases']['db_name']

class mysql(object):
    def __init__(self):
        self.DB_DATA=""
    def connect(self):
        try:
            self.mysql = MySQLdb.connect(DB_HOST,DB_USER,DB_PASS,DB_DATABASE,DB_PORT)
            self.cursor = self.mysql.cursor()
        except Exception,e:
            log.log(e)
            return 1
    def select(self,sql):
        try:
            self.cursor.execute(sql)
            self.DB_DATA = self.cursor.fetchall()
        except Exception,e:
            log.log(e)
        return self.DB_DATA
    def insert_update_delete(self,sql):
        try:
            self.cursor.execute(sql)
            self.mysql.commit()
        except Exception,e:
            self.mysql.rollback()
            log.log(e)
    def close(self):
        try:
            self.mysql.close()
        except Exception,e:
            log.log(e)
 
