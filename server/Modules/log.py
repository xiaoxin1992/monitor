#!/usr/bin/env python
# coding=utf-8
import logging
from conf.config import server_global
log_path = server_global['log_path']
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

