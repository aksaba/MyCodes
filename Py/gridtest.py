import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from matplotlib.font_manager import FontProperties

plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
plt.rcParams['axes.xmargin'] = 0.
plt.rcParams['axes.ymargin'] = 0.
plt.rcParams["font.family"] = "serif"
plt.rcParams["figure.figsize"] = (10,6)

#fontP = FontProperties()
#fontP.set_size('smaller')

#fig1, ax1 = plt.subplots()

#ax2 = ax1.twinx()
x,y1,y2,y3,y4,y5= np.loadtxt('gridtest.csv',unpack=True, delimiter=',',skiprows=1)
plt.plot(x,y1,label="Mesh1")
plt.plot(x,y2,label="Mesh2")
plt.plot(x,y3,label="Mesh3")
plt.plot(x,y4,label="Mesh4")
plt.plot(x,y5,'k-',label="Analytical")

#ax1.set_ylim([25,40]) 
#ax1.set_xlim([0,130.25])

plt.xlabel('time (s)')
plt.ylabel('Temp (C)')

plt.legend()
plt.tight_layout(rect=[0, 0, 1, 1],h_pad=0.5)


#fig.savefig('test2png.png', dpi=100)


plt.show()



