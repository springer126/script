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

r,w=os.pipe()	                            #����ܵ������̼�ͨ�žͿ����ˣ�

while True:                                 #��������ѭ��
    print "waiting ...."                    #��ӡ�ȴ��û�����ʱ��waiting
    try:	                            #�����ܵ��쳣
        tcpCliSock,addr=tcpSerSock.accept() #�����û�����
        os.write(w,"f")                     #�ڹܵ�һ��д���ַ���f��
    except:	                            #�����쳣
        sys.exit(0)	                    #��������쳣��ֱ���˳�
    if os.fork():	                    #�ڸ������еĴ���
        pass #��������
    else:	#���ӽ����еĴ���
        print 'come from :',addr #��ӡ�ͻ�����Ϣ
        while True: #��������ѭ��
            data=tcpCliSock.recv(BUFSIZ) #�ӿͻ��˽���1024��С������
            os.write(w,data) #������д�뵽������
            if not data: #����ͻ���û���κ����룬��ֱ�ӻس���Ctrl+D
                tcpSerSock.close()	#�رտͻ�������
                break	#��������ѭ��
                tcpCliSock.send('[%s] %s' %(ctime(),os.read(r,1024)))#��������û���Ϣ�����ӵ�ǰʱ�䣡

tcpSerSock.close() #��仰��Ȼ���ᱻִ��
