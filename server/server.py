#!/usr/bin/env python
# coding=utf-8
import SocketServer,sys
from Modules.log import *
from Modules.handle_data import *
from conf.config import server_global

HOST= server_global['listen_ip']
PORT=server_global['listen_port']
class MytcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        address = self.client_address[0].strip()
        all_data=""
        while 1:
            if address not in ['127.0.0.1']:
                self.request.sendall("Error:Server rejected the connection.\n")
                break
            data = self.request.recv(1024).strip()
            if not data:
                break
            all_data = all_data + data
        if len(all_data) != 0:
            if handle(all_data.strip(),self.client_address[0]):
                self.request.sendall("Message is invalid")
    
        
       #self.client_address[0]

if __name__ == "__main__":
    log('Server runing...')
    try:
        server = SocketServer.ThreadingTCPServer((HOST,PORT),MytcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print
        sys.exit(0)
    except Exception,e:
        print e
        sys.exit(-1)

