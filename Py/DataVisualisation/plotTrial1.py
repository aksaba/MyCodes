import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "serif"
data_path="H:/2018Simulations/November/TianCompared.csv"
types = ['f8','f8','f8','f8']
data=np.genfromtxt(data_path,dtype=types,names=True, delimiter=',')

plt.scatter(data['X1'],data['Y1'])
plt.scatter(data['X2'],data['Y2'])

plt.axis([0,1,-250,+250])

plt.xlabel("Distance from hot wall X=x/L")
plt.ylabel("Vertical velocity v (mm/s)")

plt.suptitle("Comparing current simulation with literature")
plt.show()
