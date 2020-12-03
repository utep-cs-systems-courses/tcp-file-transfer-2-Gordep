#! /usr/bin/env python3

# Client
import socket, sys, re, os

#########################################
#Code snippet from framedClient 
sys.path.append("../lib")
import params

# For proxy
#from framedSock import framedSend, framedReceive

from EncapFramedSock import EncapFramedSock


####NEW ############
port = input("Would you like to use the stammer proxy? (y/n)\n")
if 'y' in port:
    port = "50000"
else:
    port = "50001"

####NEW ############
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

s = None
sa = None
fsock = None
for res in socket.getaddrinfo(serverHost, serverPort, socket.AF_UNSPEC, socket.SOCK_STREAM):
    af, socketType, proto, cannonname, sa = res
    try:
        print("Creating Socket: af=%d, type=%d, proto=%d" % (af, socketType, proto))
        s = socket.socket(af, socketType, proto)
    except socket.error as msg:
        print(" error: %s" % msg)
        s = None
        continue
    try:
        print("Attempting to connect to %s" % repr(sa))
        s.connect(sa)
        fsock = EncapFramedSock((s, sa))
    except socket.error as msg:
        print("Error: %s" % msg)
        s.close()
        s = None
        continue
    break

if s is None:
    print("Could not open socket")
    sys.exit(1)

files = os.listdir(os.curdir)
print(files)
try:
    fileName = input("Enter file name to transfer: ")
    file = open(fileName,"rb") ### use RB?

except Exception as e:
    print(e)
    sys.exit(1)

#File to transfer
fileContent = file.read()#(1024)

try:
    #sends file info to server
    fsock.send(str(fileContent).encode())
except BrokenPipeError:
    print("Disconnected from server")
    sys.exit(0)

fsock.send(str(fileContent).encode(),debug)

sys.exit(0)


