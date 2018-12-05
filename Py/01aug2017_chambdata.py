

#
#	Code plots experiment data on ax1 and reference lines on ax2 of the same plot
#




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

fig1, ax1 = plt.subplots()

ax2 = ax1.twinx()
x,y1,y2,y3,y4,y5,y6,y7,y8,y9,y10,y11,y12= np.loadtxt("C:/Users/AKS/Documents/GitHub/MyCodes/Py/01aug2017_chambdata.csv",unpack=True, delimiter=',',skiprows=1)
#ax1.plot(x,y1,label="101_Temp")
#ax1.plot(x,y2,label="102_Temp")
#ax1.plot(x,y3,label="103_Temp")
#ax1.plot(x,y4,label="104_Temp")
#ax1.plot(x,y5,label="105_Temp")
#ax1.plot(x,y6,label="106_Temp")
ax1.plot(x,y7,label="T1_Temp")
ax1.plot(x,y8,label="T2_Temp")
#ax1.plot(x,y9,label="109_Temp")
#ax1.plot(x,y10,label="112_Temp")
#ax1.plot(x,y11,label="113_Temp")
#ax1.plot(x,y12,label="114_Temp")
#ax1.plot(x,y13,label="115_Temp")
ax1.plot(x,y9,label="HTU21D_1_Temp")
ax2.plot(x,y10,'r--',label="HTU21D_1_%RH")
ax1.plot(x,y11,label="HTU21D_2_Temp")
ax2.plot(x,y12,'b--',label="HTU21D_2_%RH")

ax1.set_ylim([22,38])
ax1.set_xlim([0,115.25])

xref1, yref1 = [0, 115.25], [25, 25]
xref2, yref2 = [0, 115.25], [80, 80]
ax1.plot(xref1, yref1,'k-',label="Set Temp")
ax2.plot(xref2, yref2,'k--',label="Set %RH")

#ax1.annotate('Set Temperature', xy=(90, 40), xytext=(90, 39.5)) #arrowprops=dict(facecolor='black', shrink=0.05))
#ax2.annotate('Set Rel. Humidity', xy=(90, 25), xytext=(90, 25.3))

ax1.set_xlabel('time (min)')
ax1.set_ylabel('Temp (C)')
ax2.set_ylabel('%RH')

lines = ax1.get_lines() + ax2.get_lines()
plt.legend(lines, [line.get_label() for line in lines], bbox_to_anchor=(1.03, 1), loc="best", borderaxespad=3.5)
plt.tight_layout(rect=[0, 0, 0.8, 1],h_pad=0.5)


#fig.savefig('test2png.png', dpi=100)


plt.show()
