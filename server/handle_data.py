import json,sys

def handle(data):
    try:
        print json.loads(data)
    except ValueError,e:
        return -1
