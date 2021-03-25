# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 14:49:41 2021

@author: caear
"""
import pylab as plt

mySamples = []
myLinear = []
myQuadratic = []
myCubic = []
myExponencial = []


for i in range(0, 30):
    mySamples.append(i)
    myLinear.append(i)
    myQuadratic.append(i**2)
    myCubic.append(i**3)
    myExponencial.append(1.5**i)
    

plt.plot(mySamples, myLinear)
plt.plot(mySamples, myQuadratic)
plt.plot(mySamples, myCubic)
plt.plot(mySamples, myExponencial)
