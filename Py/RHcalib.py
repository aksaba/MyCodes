import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
from matplotlib.font_manager import FontProperties
from numpy import arange,array,ones
from scipy import stats

plt.rcParams['axes.autolimit_mode'] = 'round_numbers'
plt.rcParams['axes.xmargin'] = 0.
plt.rcParams['axes.ymargin'] = 0.
plt.rcParams["font.weight"] = 500
plt.rcParams["font.family"]="sans-serif"
plt.rcParams["font.size"] = 14
plt.rcParams["figure.dpi"] = 200
plt.rcParams["figure.figsize"] = (8,6)

#fontP = FontProperties()
#fontP.set_size('smaller')

#fig1, ax1 = plt.subplots()

#ax2 = ax1.twinx()
x,y= np.loadtxt('RHcalib.csv',unpack=True, delimiter=',',skiprows=1)


slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
line = slope*x+intercept

plt.plot(x,y,'o',x,line)

plt.ylim([30,100]) 
plt.xlim([30,100])

#plt.annotate('y =', slope, 'x +', intercept, xytext=(50, 15))
plt.annotate('y = ' , xy=(40,40), xytext=(50, 40))
plt.xlabel('Measured RH (%)')
plt.ylabel('Ref. RH (%)')

plt.legend()
plt.tight_layout(rect=[0, 0, 1, 1],h_pad=0.5)
plt.savefig('RHcalib.png', dpi=180)


plt.show()



