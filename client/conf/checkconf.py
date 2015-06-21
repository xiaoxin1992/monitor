# coding=utf-8

import os,sys,re,imp
server_root = os.path.dirname(sys.path[0].strip())
sys.path.append(server_root)
try:
    from conf.config import srcipt,info,client_root,plugin_directory,log_file,CONNECT
except Exception,e:
    print '\033[1;31;40m',"Configuration Syntax Error:%s" % e,'\033[0m'
    sys.exit(-1)

def printf(p_data,p_type=1):
    if p_type is 0:
        err_type = '\033[1;31;40m'
    else:
        err_type = '\033[1;32;40m'
    info_type = err_type
    print info_type,
    print p_data,
    print '\033[0m'
def Dict_Judge(data,data_type):
    error_num=0
    if type(data) is dict:
        for k,v in data.items():
            if data_type.keys()[0] is '*':
                if type(v) is not data_type['*']:
                    printf("Configuration error: '%s' Options must be an %s" % (k,data_type['*']),0)
                    error_num += 1
                continue
            for t_k,t_v in data_type.items():
                if k is t_k:
                    if type(v) is not t_v:
                        printf("Configuration error: '%s' Options must be an %s" % (k,t_v),0)
                        error_num += 1
    return error_num
def getconfig():
    error_num=0
    pattern = "\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}:\d{1,5}"
    try:
        if not re.search(r'%s' % pattern,CONNECT):
            printf("Configuration error: %s" % CONNECT,0)
            error_num += 1
    except  NameError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1
    except TypeError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1
    try:
        if type(client_root) is not str:
            printf("Configuration error: client_root Options must be an %s" % str,0)
            error_num += 1
    except  NameError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1 
    try:
        if type(plugin_directory) is not str:
            printf("Configuration error: plugin_directory Options must be an %s" % str,0)
            error_num += 1
    except  NameError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1
    try:
        if type(log_file) is not str:
            printf("Configuration error: log_file Options must be an %s" % str,0)
            error_num += 1
    except  NameError,e:
        printf("Configuration error: %s" % e,0)
        error_num += 1
    try:
       info_re =  Dict_Judge(info,{'id':int,'information':str,'submitted':int})
    except NameError,e:
        print  e
        error_num += 1
    try:
       srcipt_re =  Dict_Judge(srcipt,{'*':str})
    except NameError,e:
        print  e
        error_num += 1
    if not error_num and not info_re and not srcipt_re :
        #printf("Configuration  Success!")
        return 1
    else:
        return 0
#getconfig()