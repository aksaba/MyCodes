import csv
import pprint
import matplotlib
from matplotlib import pyplot as plt
infile = open('FitData.csv','r')
time = []
temp = []
for row in csv.reader(infile):
	time.append(row[0])	
	temp.append(row[1])

infile.close()

pprint.pprint(time)
#pprint.pprint(temp)

#plt.plot(time,temp,label='line one', linewidth=2)

#plt.title('Temperature Profile')
#plt.ylabel('T (K)')
#plt.xlabel('t (s)')
#plt.legend()

#plt.show()
