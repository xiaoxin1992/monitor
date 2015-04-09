#!/usr/bin/env python
# coding=utf-8
import socket,time
HOST,PORT = 'localhost',45100
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    sock.connect((HOST,PORT))
    sock.sendall("send mail")
except socket.error,e:
    print e
finally:
    sock.close()
