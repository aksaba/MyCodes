import urllib
import os
k=0
myPath="f:/temp"



for i in range(201105,201106):
	for j in range (145,500):
		filename = "local-filename_{a}_{b}.jpg".format(a=i,b=j)
		fullfilename = os.path.join(myPath, filename)
		url=urllib.urlretrieve("https://www.nastol.com.ua/images/{a}/nastol.com.ua_{b}.jpg".format(a=i,b=j),fullfilename)
		statinfo = os.stat(fullfilename)
		print i,"\t",j,"\t",statinfo.st_size
		#print statinfo.st_size
		if statinfo.st_size < 100000:
			os.remove(fullfilename)

#print("https://www.nastol.com.ua/images/{a}/nastol.com.ua_{b}.jpg")
