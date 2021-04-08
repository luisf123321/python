# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:02:06 2021

@author: luisf
"""

from numpy import array

data = [11,22,33,44,55]

data = array(data)

print(data)

print(type(data))

data2 = [[11,22],[33,44],[55,66]]
data2 = array(data2)
print(data2)
print(type(data2))

#index
print(data[0])
print(data[4])

print(data[-1])
print(data[-5])

print(data2[0,0])
print (data2[0,])

#slicing

print(data[:3])

print(data[-2:])

data3 = array([[11,22,33],[44,55,66],[77,88,99]])

X, y = data3[:,:-1],data3[:,-1]
print(X)
print(y)

print(data.shape)
print(data2.shape)
print(data.shape[0])
print(data2.shape[1])

#reshape
data5 = data.reshape((data.shape[0],1))
print(data5)
print(data5.shape)


data6 = data2.reshape((data2.shape[0],data2.shape[1],1))
print(data6)
print(data6.shape)








