#! /usr/bin/evn python


import json


data = {'a':'A','b':(2,4),'c':3.0}

print "data:",repr(data)


data_string = json.dumps(data)

print "dump:",data_string



print "loads:",json.loads(data_string)['a']
