#! coding:utf-8
import json,sys,time,my_db
import json
def data_flush_database(data):
    """
    变量定义
    """
    select_host_data=None
    select_host_sql=None
    insert_host_sql=None
    update_host_sql=None
    select_server_data = None
    updae_server_sql = None
    insert_host_sql = None
    select_server_sql = None
    
    """
        用于把数据更新到数据库中
    """
    select_host_sql = """select id from monitor_host_info where id=%s and ip='%s'""" %(data['id'],data['host'])
    insert_host_sql = """insert into monitor_host_info(id,ip,host_info,alive,time)  values(%s,'%s','%s',%s,'%s')""" % (data['id'],data['host'],data['host_info'],1,data['time'])
    update_host_sql = """update monitor_host_info set alive=1,time='%s' where id=%s and ip='%s'""" % (data['time'],data['id'],data['host'])
    mysql = my_db.mysql()
    if mysql.connect() is 1:
        return 1
    select_host_data = mysql.select(select_host_sql)
    if len(select_host_data) == 0:
        mysql.insert_update_delete(insert_host_sql)  
    else:
        mysql.insert_update_delete(update_host_sql) 
    if len(select_host_data) != 0:
        select_server_sql = """select id from monitor_host_server where host_id=%s and command_name='%s'""" % (select_host_data[0][0],data['cmd_name'])
        select_server_data = mysql.select(select_server_sql)
        if len(select_server_data) == 0:
            insert_host_sql = """insert into monitor_host_server(host_id,command_name,data,code,time) values(%s,'%s','%s',%s,'%s')""" % (select_host_data[0][0],data['cmd_name'],data['data'],data['code'],data['time'])
            mysql.insert_update_delete(insert_host_sql)
        else:
            updae_server_sql = """update monitor_host_server set data='%s',code=%s,time='%s' where host_id=%s and command_name='%s';""" % (data['data'],data['code'],data['time'],select_host_data[0][0],data['cmd_name'])
            mysql.insert_update_delete(updae_server_sql)
    mysql.close()
    
def handle(data,ip):
    try:
        data = json.loads(data)
    except ValueError,e:
        return -1
    now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    for x in data:
        #if x['id'] is config_data['id']:
        data_flush_database({'id':x['id'],'host':ip,'host_info':x['host_info'],'cmd_name':x['cmd_name'],'data':x['data'],'code':x['code'],'time':now_time})

    