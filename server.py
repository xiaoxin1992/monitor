#!/usr/bin/env python
# coding=utf-8
import SocketServer,sys,logging,log

HOST='0.0.0.0'
PORT=45100
class MytcpHandler(SocketServer.BaseRequestHandler):
    def handle(self):
       print self.request.recv(1024).strip()
       #self.client_address[0]

if __name__ == "__main__":
    log.log('Server runing...')
    try:
        server = SocketServer.ThreadingTCPServer((HOST,PORT),MytcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print
        sys.exit(0)

