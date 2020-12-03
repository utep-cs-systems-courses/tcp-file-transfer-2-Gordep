#! /usr/bin/env python3


###################################
#Code snippet from frameForkServer.py
import re, socket, os, threading, sys
sys.path.append("../lib")       # for params
import params
######NEW#########
from threading import Thread, Lock
#############
#from framedSock import framedSend, framedReceive

from EncapFramedSock import EncapFramedSock


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
#####NEW ############
lock = threading.Lock()
##################


#Code snippet from frameThreadServer
from threading import Thread, Lock;

class Server(Thread):
    def __init__(self, sockAddr):
        Thread.__init__(self)
        self.sock, self.addr = sockAddr
        self.fsock = EncapFramedSock(sockAddr)
    def run(self):
        print("new thread handling connection from", self.addr)
        #payload = framedReceive(self.sock, debug)
        while True:
            lock.acquire()
            payload = self.fsock.receive(debug)
            payload = payload.decode()

            fileContents = payload.encode()
            #payload += b"!"

            outputFile = open("fileTest.txt",'wb+')
            outputFile.write(fileContents)
            outputFile.close()
            lock.release()
            print("fileTest outputted")
            sys.exit(0)



###################
#code snippet from frameThreadServer 
while True:
    sockAddr = lsock.accept()
    server = Server(sockAddr)
    server.start()
###################