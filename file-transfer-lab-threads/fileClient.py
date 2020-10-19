#! /usr/bin/env python3

# Client
import socket, sys, re, os

#########################################
#Code snippet from framedClient 
sys.path.append("../lib")
import params

# For proxy
from framedSock import framedSend, framedReceive


switchesVarDefaults = (
    (('-s', '--server'), 'server', "127.0.0.1:50001"),
    (('-d', '--debug'), "debug", False), # boolean (set if present)
    (('-?', '--usage'), "usage", False), # boolean (set if present)
    )
    
progname = "fileClient"
paramMap = params.parseParams(switchesVarDefaults)

server, usage, debug  = paramMap["server"], paramMap["usage"], paramMap["debug"]


if usage:
    params.usage()
    
# Client connection to server
# Split server into local host and port
try:
   serverHost, serverPort = re.split(":", server)
   serverPort = int(serverPort)
except:
   print("Can't parse server:port from  '%s'" % server)
   sys.exit(1)


#end of code snippet
############################################ 
# Code snippet from framedClient

addrFamily = socket.AF_INET
socktype = socket.SOCK_STREAM
addrPort = (serverHost, serverPort)

s = socket.socket(addrFamily, socktype)

if s is None:
    print('could not open socket')
    sys.exit(1)

s.connect(addrPort)

while True:
    
    try:
        fileName = input("Enter file name to transfer: ")
        file = open(fileName,"rb") ### use RB?

    except Exception as e:
        print(e)
        sys.exit(1)

    #File to transfer
    fileContent = file.read()#(1024)

    #s.sendall()

    #framedSend(s, b"hello world", debug)

    framedSend(s,str(fileContent).encode(), debug)




