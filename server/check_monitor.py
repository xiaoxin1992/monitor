#! /usr/bin/env python
import time,datetime
from Modules.sendmail import *
from Modules.log import *
from Modules.my_db import *
from conf.config import timeout_set
check_host_time = timeout_set['check_host_time']
check_server_time = timeout_set['check_server_time']
send_mail_time =  timeout_set['send_mail_time']
class check(object):
    def __init__(self):
        self.mysql = mysql()
        self.mysql.connect()
    def check_host(self):
        select_sql = """select * from monitor_host_info"""
        update_sql = """update monitor_host_info set alive = 0 where id=%s """
        host_on_alive = []
        for x in self.mysql.select(select_sql):
           if (datetime.datetime.now() - x[4]).seconds > check_host_time:
              host_on_alive.append({
                'ID':x[0],
                'IP':'%s' % x[1],
                'alive':x[2],
                'hostname':'%s' % x[3],
                'time':'%s' % x[4]
                })
              self.mysql.insert_update_delete(update_sql % x[0])
        return host_on_alive
    def check_server(self):
        host_info = None
        host_id = []
        host_info = self.check_host()
        for x  in host_info:
           host_id.append(x['ID'])
        select_sql = """select * from monitor_host_server"""
        select_host_sql = """select ip from monitor_host_info where id=%s"""
        select_host = mysql()
        select_host.connect()
        server_ret = []
        for x in self.mysql.select(select_sql):
            if x[0] in host_id or x[4] == 0:
                break
            server_ret.append({'host_id':x[0],
                    'host_ip':'%s' % (select_host.select(select_host_sql % x[0])[0]),
                    'server_id':x[1],
                    'server_name':'%s' % x[2],
                    'time':'%s' % x[3],
                    'code':x[4],
                    })
        select_host.close()
        return server_ret
    def close(self):
        self.mysql.close()
class send_mail(object):
    def __init__(self):
        pass
    def send_host_mail(self):
        subject = """
        HOST %s fault
        """
        
        message = """
            <h2>Hello, Following Host Fails</h2>
            <P>Host IP:%s<br />HostName:%s
            <br />Last Time:%s<br />Time:%s<br />Status:down<br /></P>
        """
        now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        host = check()
        for x  in host.check_host():
            sendmail(mail_subject=subject%(x['hostname']),
                             data=message%(x['IP'],x['hostname'],x['time'],now_time))
        host.close()
    def send_server_mail(self):
        subject = """
        HOST %s Server %s fault
        """
        now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
        message = """
            <h2>Hello, Following Server Fails</h2>
            <p>
                Host IP:%s <br />
                Server Name:%s <br />
                Time:%s
            </p>
        """
        server = check()
        for x in server.check_server():
            sendmail(mail_subject=subject%(x['host_ip'],x['server_name']),data=message %(x['host_ip'],x['server_name']
                                                                                             ,now_time))
        server.close()
try:
    while True:
        a = send_mail()
        a.send_host_mail()
        a.send_server_mail()
        try:
            time.sleep(send_mail_time)
        except IOError,e:
            log(e)
except:
    pass
    
