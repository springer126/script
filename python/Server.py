# -*- coding: cp936 -*-
from socket import *    #����socket���е���������
from time import ctime  #����time����ͬʱ�ڱ��ؿ�ʹ��ctime���е���
import os,sys           #����os��sys��
HOST='localhost'	#��������
PORT=21567	 #����˿�
BUFSIZ=1024      #���建����
ADDR=(HOST,PORT) #����Ԫ��

tcpSerSock=socket(AF_INET,SOCK_STREAM)  #����socket
tcpSerSock.bind(ADDR)                   #����ַ���˿�Ԫ����socket��
tcpSerSock.listen(5)                    #�����û�����,���������Ϊ5

while True:                                 #��������ѭ��
    print "waiting ...."                    #��ӡ�ȴ��û�����ʱ��waiting
    try:	                            #�����ܵ��쳣
        tcpCliSock,addr=tcpSerSock.accept() #�����û�����
    except:	                            #�����쳣
        sys.exit(0)	                    #��������쳣��ֱ���˳�
  
    print 'come from :',addr #��ӡ�ͻ�����Ϣ
    
    while True: #��������ѭ��
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime(),data))#��������û���Ϣ�����ӵ�ǰʱ�䣡
        print [ctime()],':',data

tcpCliSock.close()
tcpSerSock.close() #��仰��Ȼ���ᱻִ��
