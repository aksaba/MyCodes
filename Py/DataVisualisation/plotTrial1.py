import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "serif"

x1,y1,x2,y2=np.loadtxt("H:/2018Simulations/November/TianCompared.csv",unpack=True, delimiter=',',skiprows=1)
plt.plot(x1,y1,'b-')
plt.plot(x2,y2,'ro')

plt.axis([0,1,-250,+250])

plt.xlabel("Distance from hot wall X=x/L")
plt.ylabel("Vertical velocity v (mm/s)")

plt.suptitle("Comparing current simulation with literature")
plt.show()
