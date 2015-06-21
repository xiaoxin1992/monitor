#!/usr/bin/env python
# coding=utf-8
import logging,sys,os
from conf.config import log_file
#man_path = os.path.dirname(sys.path[0])
#man_path = sys.path[0]
#log_path = man_path + "/log/client.log"

def log(message=''):
    if not os.path.exists(os.path.dirname(log_file)):
        os.mkdir(os.path.dirname(log_file))
    #logger = logging.getLogger()
    format_name = '%(asctime)s - %(filename)s  - %(levelname)s - %(message)s'
    try:
        logging.basicConfig(filename=log_file,level=logging.INFO,format=format_name, datefmt='%Y-%m-%d %H:%M:%S')
    except Exception,e:
        print 
        print e
        sys.exit(-1)
    logging.info(message)
if __name__ == "__main__":
    log()
