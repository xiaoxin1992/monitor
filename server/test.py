#!/usr/bin/env python
# coding=utf-8

import time
from multiprocessing import Process 
from Modules.server import start

#server.start()

"""
def func(msg):
    for i in xrange(3):
        print msg
        time.sleep(1)
"""
if __name__ == "__main__":
    p = Process(target=start)
    p.start()
    p.join()
