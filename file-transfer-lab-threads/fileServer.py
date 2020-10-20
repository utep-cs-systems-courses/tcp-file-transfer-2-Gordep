#! /usr/bin/env python3


###################################
#Code snippet from frameForkServer.py

import sys
sys.path.append("../lib")       # for params
import re, socket, params, os
from framedSock import framedSend, framedReceive

switchesVarDefaults = (
    (('-l', '--listenPort') ,'listenPort', 50001),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )

progname = "echoserver"
paramMap = params.parseParams(switchesVarDefaults)

debug, listenPort = paramMap['debug'], paramMap['listenPort']

if paramMap['usage']:
    params.usage()

lsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # listener socket
bindAddr = ("127.0.0.1", listenPort)
lsock.bind(bindAddr)
lsock.listen(5)
print("listening on:", bindAddr)

#####################################
#Code snippet from frameThreadServer
from threading import Thread, Lock;

lock = Lock()
class Server(Thread):
    def __init__(self, sockAddr):
        Thread.__init__(self)
        self.sock, self.addr = sockAddr
        #self.fsock = EncapFramedSock(sockAddr)
    def run(self):
        print("new thread handling connection from", self.addr)
        payload = framedReceive(self.sock, debug)
        while True:
            #payload = self.fsock.receive(debug)
            if debug:
                print("rec'd: ", payload)
            if not payload:
                if debug: print(f"thread connected to {addr} done")
                self.fsock.close()
                return          # exit

            lock.acquire()

##################################################

            payload = payload.decode()

            fileContents = payload.encode()
            #payload += b"!"

            outputFile = open("fileTest.txt",'wb+')
            outputFile.write(fileContents)
            outputFile.close()
            print("fileTest outputted")






################




###################
#code snippet from frameThreadServer 
while True:
    sockAddr = lsock.accept()
    server = Server(sockAddr)
    server.start()
###################