#!/usr/bin/env python
# coding=utf-8
import socket,time
def send_data(data):
    HOST,PORT = 'localhost',45100
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
	sock.connect((HOST,PORT))
	if sock.sendall(data) is None:
	    return 0
    except socket.error,e:
	print e
	return -1
    finally:
	sock.close()

