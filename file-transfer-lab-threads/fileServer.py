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


#####################################

from threading import Thread;


print("listening on:", bindAddr)












################
while True:
	sock, addr = lsock.accept()

	if not os.fork():

		print("connection from -",addr)
		payload = framedReceive(sock,debug)

		if not payload:
			print("no paylaod")
			sys.exit(0)

		if debug:
			print("rec'd: ", payload)

		payload = payload.decode()
		fileContents = payload.encode()
		#payload += b"!"

		outputFile = open("fileTest.txt",'wb+')
		outputFile.write(fileContents)
		outputFile.close()
		print("fileTest outputted")


