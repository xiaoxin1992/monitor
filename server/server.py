#!/usr/bin/env python
# coding=utf-8
import SocketServer,sys,logging,log,handle_data

HOST='0.0.0.0'
PORT=45100
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
            if handle_data.handle(all_data.strip()):
                self.request.sendall("Message is invalid")
    
	    
       #self.client_address[0]

if __name__ == "__main__":
    log.log('Server runing...')
    try:
        server = SocketServer.ThreadingTCPServer((HOST,PORT),MytcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print
        sys.exit(0)
    except Exception,e:
        print e
        sys.exit(-1)

