import csv
import pprint

infile = open('FitData.csv','r')
time = []
temp = []
for row in csv.reader(infile):
	time.append(row[0])	
	temp.append(row[1])

infile.close()

pprint.pprint(time)
pprint.pprint(temp)


