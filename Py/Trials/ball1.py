# Python learning Program 1
# Reference : A Primer on Scientific Programming with Python
# Author : Hans Petter Langtangen

# Example 1

# Newton's second equation of motion

v0 = 5
g = 9.81
t = 0.6
y = v0*t-0.5*g*t**2
print y
print 'At t = %g s, the height of the ball is %.2f meters. ' %(t,y)

# %g : Print real number in compact format
# .2f : Print real number with 2 decimal points; f-floating point

print """ Text
 in
 several \n lines"""


print """
At t={t:g} s, a ball with
initial velocity v0={v0:.3E} m/s
is located at the height {y:.2f} m.
""".format(t=t, v0=v0, y=y)
