import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from matplotlib.font_manager import FontProperties

plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
plt.rcParams['axes.xmargin'] = 0.
plt.rcParams['axes.ymargin'] = 0.

fontP = FontProperties()
fontP.set_size('smaller')

fig1, ax1 = plt.subplots()

yref = 25;
ax2 = ax1.twinx()
x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17= np.loadtxt('07july2017_chambdata.csv',unpack=True, delimiter=',',skiprows=1)
ax1.plot(x,y1,label="101_Temp")
ax1.plot(x,y2,label="102_Temp")
ax1.plot(x,y3,label="103_Temp")
ax1.plot(x,y4,label="104_Temp")
ax1.plot(x,y5,label="105_Temp")
ax1.plot(x,y6,label="106_Temp")
ax1.plot(x,y7,label="107_Temp")
ax1.plot(x,y8,label="108_Temp")
ax1.plot(x,y9,label="109_Temp")
ax1.plot(x,y10,label="110_Temp")
ax1.plot(x,y11,label="111_Temp")
ax1.plot(x,y12,label="112_Temp")
ax1.plot(x,y13,label="113_Temp")
ax1.plot(x,y14,label="114_Temp")
ax1.plot(x,y15,label="115_Temp")
ax1.plot(x,y16,label="HTU21D_Temp")
ax2.plot(x,y17,'b--',label="HTU21D_%RH")

ax1.set_ylim([23,35]) 
ax1.set_xlim([0,127.5])

xref1, yref1 = [0, 127.5], [25, 25]
xref2, yref2 = [0, 127.5], [40, 40]
ax1.plot(xref1, yref1,'k-')
ax2.plot(xref2, yref2,'k-')

ax1.annotate('Set Temperature', xy=(90, 25), xytext=(90, 25.1)) #arrowprops=dict(facecolor='black', shrink=0.05))
ax2.annotate('Set Rel. Humidity', xy=(90, 40), xytext=(90, 40.2))

ax1.set_xlabel('time (min)')
ax1.set_ylabel('Temp (C)')
ax2.set_ylabel('%RH')

#plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3,
#           ncol=2, mode="expand", borderaxespad=0.)
#plt.legend(loc='upper right')

lines = ax1.get_lines() + ax2.get_lines()
plt.legend(lines, [line.get_label() for line in lines],loc='center right',bbox_to_anchor=(1.27,0.5),prop=fontP)

fig = plt.gcf()
fig.set_size_inches(10.5, 6.5)

#fig.savefig('test2png.png', dpi=100)

plt.show()



