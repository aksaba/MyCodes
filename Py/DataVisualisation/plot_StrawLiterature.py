import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "serif"
data_path="H:/Dropbox/Research/Experiment/Results/Paper1/StrawLit.csv"
types = ['int','f8','int','f8']
data=np.genfromtxt(data_path,dtype=types,names=True, delimiter=',')

plt.scatter(data['McCabePerp_year'],data['McCabePerp'])
plt.scatter(data['McCabePara_year'],data['McCabePara'])

plt.axis([1990,2010,0.02,0.2])

plt.xlabel("Year")
plt.ylabel("k (W/mK)")

plt.suptitle("State-of-the-art in thermal conductivity measurement of Straw")
plt.show()
