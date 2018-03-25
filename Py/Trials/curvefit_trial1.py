
import csv
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # for unequal plot boxes
import scipy.optimize
import math
from scipy import special


# c = csv.writer(open("tempML_py.csv", "wb"))


def semi_inf_model(time,k ,a):

    return 303.15 + ((2.0*1397.19)/(k))*(( np.sqrt((a*time)/np.pi)*math.exp(-(0.01*0.01)/(4.0*a*time)))-(0.01/2.0)*special.erfc(0.01/np.sqrt(4.0*a*time)))

#time = np.arange(60,80,1)
#time=time.transpose()
#T = np.array([303.181647, 303.1843961, 303.1872949, 303.190346, 303.1935517, 303.1969144, 303.2004362, 303.204119, 303.2079646,303.2119749,303.2161513,303.2204953,303.2250082,303.2296911,303.2345452,303.2395714,303.2447706,303.2501433,303.2556904,303.2614123]).transpose()
#ds  = np.array([0.2, 0.22, 0.24, 0.24, 0.25, 0.26, 0.26, 0.27, 0.28, 0.28, 0.29, 0.29, 0.29, 0.30, 0.30, 0.31, 0.31, 0.32, 0.32, 0.32]).transpose()
print(semi_inf_model(100,0.283,1.1e-7))

time, T, ds = np.loadtxt("temp.txt", skiprows=4, unpack=True)
k0 = 0.2
a0 = 1.0

nlfit, nlpcov = scipy.optimize.curve_fit(semi_inf_model,time, T, p0=[k0, a0],sigma=ds)

#k,a = nlfit
#dk,da = [np.sqrt(nlpcov[j,j]) for j in range(nlfit.size)]

#f_fit = np.linspace(300, 100., 310)
#s_fit = semi_inf_model(f_fit, k,a)

#resids = T - semi_inf_model(k, a,time)
#redchisqr = ((resids/ds)**2).sum()/float(f.size-6)



print time
print T
