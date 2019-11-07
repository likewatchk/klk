import matplotlib.pyplot as plt
#import numpy as np
import pprint as ppr
from math import sin, cos, pi
#sList = np.arange(0,20,dtype=int)
x = [i for i in range(-10, 10)]
s = [2**v for v in x]
for i in x:
    if 2**i==max(s):
        maxad=i
for i in x:
    if 2**i==min(s):
        minad=i
plt.plot(x,s,linestyle='-',color='g' ,linewidth=3)
plt.scatter(maxad,max(s),200,c='r')
plt.scatter(minad,min(s),200,c='b')
plt.show()
#-------------------------------------------------
x2 = [0.01*i for i in range(-200, 201)]
y_sin = [sin(j*pi) for j in x2]
maxad2=[]
minad2=[]
mmax=[]
mmin=[]
for i in x2:
    if sin(i*pi)==max(y_sin):
        maxad2.append(i)
for i in x2:
    if sin(i*pi)==min(y_sin):
        minad2.append(i)
for i in range(len(maxad2)):
    mmax.append(max(y_sin))
for i in range(len(minad2)):
    mmin.append(min(y_sin))
plt.plot(x2,y_sin,linestyle='-',color='g' ,linewidth=3)
plt.scatter(maxad2,mmax,200,c='r')
plt.scatter(minad2,mmin,200,c='b')
plt.show()