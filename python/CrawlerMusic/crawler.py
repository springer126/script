﻿#! -*- coding:utf-8 -*-

import re
import urllib
import urllib2
import os,time
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def readHtml(htmlurl):
	reader = urllib2.urlopen(htmlurl)
	content = reader.read()
#	print(content.decode('gb2312').encode('utf-8'))
	return content

def downMusic(htmlurl):
	reader = urllib2.urlopen(htmlurl)
	content = reader.read()

	baseurl = 'http://www.5nd.com/'
	pattern = r'<a.+? href="/ting/(\d+\.htm)l">(.+?)</a>'
	reg = re.compile(pattern)
	links = re.findall(reg,content)

	for songs in links:
		link = baseurl+'mp3/'+songs[0]
	#	print(link)
		downpage = urllib2.urlopen(link)
		downcontent = downpage.read()
		downpat = r'<a class="downlink" href="(.+?)">.+?</a>'
		downreg = re.compile(downpat)
		songlinks = re.findall(downreg,downcontent)
		for i in songlinks:
		#	print(i)
			musicname = songs[1].decode('gb2312').encode('utf-8')
			name = 'songs/'+musicname+'.mp3'
			if(os.path.isfile(name)==False):
				urllib.urlretrieve(i,name)
				print(''+musicname+'.mp3 Finish download.')
			else:
				print(''+name+' is existed.')


def downJPG(content):
	pattern = r'src="(.*?\.jpg)"'
	urlpat = re.compile(pattern)
	imgurls = re.findall(urlpat,content)
	x = 1
	for i in imgurls:
		urllib.urlretrieve(i,'pic%s.jpg' % x)
		x +=1
	
#content = readHtml("http://tieba.baidu.com/tb/picture/index.html")
#downJPG(content)
downMusic("http://www.5nd.com/paihang/liuxinggequ.htm")
	