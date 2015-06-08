#!/usr/bin/env python
# coding=utf-8
import logging,sys,os
man_path = os.path.dirname(sys.path[0])
#man_path = sys.path[0]
log_path = man_path + "/log/client.log"
def log(message=''):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler(log_path)
    formatter = logging.Formatter('%(asctime)s - %(filename)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    logger.info(message)
if __name__ == "__main__":
    log()
