#! /usr/bin/env python3

# Client
import socket, sys, re, os

#########################################
#Code snippet from framedClient 
sys.path.append("../lib")
import params
################################################ CHANGE THIS
# For proxy
sys.path.append("../framed-echo")
from framedSock import framedSend, framedReceive
###############################################

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
   host, serverPort = re.split(":", server)
   port = int(serverPort)
except:
   print("Can't parse server:port from  '%s'" % server)
   sys.exit(1)


#end of code snippet
############################################ 

