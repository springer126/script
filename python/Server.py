# -*- coding: cp936 -*-
from socket import *    #导入socket包中的所有内容
from time import ctime  #导入time包，同时在本地可使用ctime进行调用
import os,sys           #导入os，sys包
HOST='localhost'	#定义主机
PORT=21567	 #定义端口
BUFSIZ=1024      #定义缓冲区
ADDR=(HOST,PORT) #定义元组

tcpSerSock=socket(AF_INET,SOCK_STREAM)  #生成socket
tcpSerSock.bind(ADDR)                   #将地址及端口元组与socket绑定
tcpSerSock.listen(5)                    #监听用户请求,最多连接数为5

while True:                                 #定义无限循环
    print "waiting ...."                    #打印等待用户输入时的waiting
    try:	                            #检测可能的异常
        tcpCliSock,addr=tcpSerSock.accept() #处理用户请求
    except:	                            #处理异常
        sys.exit(0)	                    #如果发生异常将直接退出
  
    print 'come from :',addr #打印客户端信息
    
    while True: #定义无限循环
        data=tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send('[%s] %s' %(ctime(),data))#否则回显用户信息并附加当前时间！
        print [ctime()],':',data

tcpCliSock.close()
tcpSerSock.close() #这句话依然不会被执行
