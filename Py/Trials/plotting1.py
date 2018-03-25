import matplotlib

#Importing pyplot
from matplotlib import pyplot as plt

#Plotting to our canvas
#plt.plot([1,2,3],[4,5,1])

#Showing what we plotted
#plt.show()

x = [5,8,10]
y = [12,16,6]

x2 = [6,9,11]
y2 = [6,15,7]

plt.plot(x,y,label='line one', linewidth=2)
plt.plot(x2,y2,label='line two',linewidth=2)


plt.title('Epic Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
plt.legend()

plt.show()
