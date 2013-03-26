#! /usr/bin/python

import urllib2
import urllib
from bs4 import BeautifulSoup

class Crawler:
	def __init__(self,word):
		self.word = word
	
	def getSiteUrls(self):
		url = "http://www.baidu.com/s"
		value = {'wd':self.word}
		encoded_param = urllib.urlencode(value)
		full_url = url+'?'+encoded_param
		response = urllib2.urlopen(full_url).read()
		siteUrls = BeautifulSoup(response).findAll('a')
		for x in siteUrls:
			print(x)
		


crawler = Crawler('wenhui')
crawler.getSiteUrls()

url = 'http://www.zhibo8.cc'
content = urllib2.urlopen(url).read()
soup = BeautifulSoup(content)
siteUrls = soup.findAll('a')

for x in siteUrls:
	print(x)

