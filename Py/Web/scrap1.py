from lxml import html
import requests
import os
from bs4 import BeautifulSoup
f = open('helloworld.md','w')
for i in range(0,1000):
	print i
	page = requests.get('https://alpha.wallhaven.cc/wallpaper/{0}'.format(i))
	c = page.content
	soup = BeautifulSoup(c,"lxml")
	#print soup.prettify()
	download_folder = "downloads"

	
	allimages =soup.find_all('img',{'id':'wallpaper'})
	for image in allimages:
		#print image source
		print 
		
		f.write('![](http:'+image['src']+')\n')
		
	#with open(os.path.join(download_folder, os.path.basename(page)), "wb") as f:
	#	f.write(c.read())
f.close()
