from socket import *

HOST = 'localhost'
PORT = 21567
BUFFERSIZE = 1024
ADDR = (HOST,PORT)

tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)

while True:
	data = raw_input()
	if not data:
		break
	tcpCliSock.send(data)
	data = tcpCliSock.recv(BUFFERSIZE)
	if not data:
		break
	print data
	
tcpCliSock.close()