import re
import urllib
import urllib2

def readHtml(htmlurl):
	reader = urllib2.urlopen(htmlurl)
	content = reader.read()
	return content
#	print content
	
def downJPG(content):
	pattern = r'src="(.*?\.jpg)"'
	urlpat = re.compile(pattern)
	imgurls = re.findall(urlpat,content)
	x = 1
	for i in imgurls:
		urllib.urlretrieve(i,'pic%s.jpg' % x)
		x +=1
	
content = readHtml("http://tieba.baidu.com/tb/picture/index.html")
downJPG(content)
	
	