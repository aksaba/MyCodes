# Python Keywords

#   and
#   as 	assert 	break 	class 	continue
#   def 	del 	elif 	else 	except 	exec
#   finally 	for 	from 	global 	if 	import
#   in 	is 	lambda 	not 	or 	pass
#   print 	raise 	return 	try 	while 	with
#   yield

time = 200
k=0.1
a=2.5e-6
x=0.01
L=0.02
L01 = 0
L001 = 0
q=30
T0 = 273.15
i=1
check1 = 0
check2 = 0
import math
from scipy import special
Tid = T0 + ((2*q)/(k))*(( math.sqrt((a*time)/math.pi)*math.exp(-(x*x)/(4*a*time)))-(x/2)*special.erfc(x/math.sqrt(4*a*time)))
print Tid

sume=0
coeff=0
costerm=0
expterm=0
for n in range(1,25):

    coeff = math.pow((-1),(n+1))*(2/(n*n*math.pi*math.pi))
    math.costerm = math.cos((n*math.pi*x)/L)
    expterm = math.exp(-(n*n*math.pi*math.pi*a*time)/(L*L))
    sume = sume + coeff*costerm*expterm
else: pass
T = T0 + ((q*L)/(1*k))*(((a*time)/(L*L)) - (((L*L)-(3*x*x))/(6*L)) + L*sume)
delt_percent = (math.fabs(T-Tid)/Tid)*100;
print T
print delt_percent
