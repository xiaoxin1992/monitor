# coding=utf-8
import re,os,sys
try:
    from conf.config import Listen,Server_Root,Log_File,databases,contacts,timeout_set
except Exception,e:
    print '\033[1;31;40m',"Configuration Syntax Error:%s" % e,'\033[0m'
    sys.exit(-1)

def printf(p_data,p_type=1):
    if p_type is 0:
        err_type = '\033[0;31;40m'
    else:
        err_type = '\033[0;32;40m'
    info_type = err_type
    print info_type,
    print p_data,
    print '\033[0m'

def data_check(data,data_type,date_type2=""):
    error_num = 0
    if data_type is not  dict:
        if type(data) is not data_type:
            printf("Configuration error: '%s' Options must be an %s" % (data,data_type),0)
            error_num += 1
    #print type(data_type)
    if data_type is dict:
        for k,v in data.items():
            if type(v) is not date_type2[k]:
                printf("Configuration error: '%s' Options must be an %s" % (v,date_type2[k]),0)
                error_num += 1
    return error_num
def checkconfig():
    error_num = 0
    pattern = "\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}"
    try:
        if not re.search(r'%s' % pattern,Listen):
            printf("Configuration error: %s" % Listen,0)
    except  NameError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1
    except TypeError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1
    error_num += data_check(Server_Root,str)
    error_num += data_check(Log_File,str)
    error_num += data_check(databases, dict,{'database_host':str,'database_port':int,'database_user':str,'database_password':str,'database':str})
    error_num += data_check(contacts, dict, {'smtp_server':str,'smtp_port':int,'smtp_user':str,'smtp_pass':str,'smtp_show_name':str,'to_mail':str})
    error_num += data_check(timeout_set, dict, {'check_host_time':int,'check_server_time':int,'send_mail_time':int})
    if not error_num:
        return 1
    else:
        return 0
