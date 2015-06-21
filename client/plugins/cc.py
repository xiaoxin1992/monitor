#! /usr/bin/env python
import psutil,time,sys
from datetime import datetime, timedelta 
uptime = int(time.time() - psutil.boot_time())
uptime1 = timedelta(seconds=uptime)
print uptime1
sys.exit(2)
