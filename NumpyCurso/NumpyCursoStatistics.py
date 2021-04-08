# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:35:20 2021

@author: luisf
"""

from numpy import array
from numpy import mean

V = array([1,2,3,4,5,6])

result = mean(V)

print(result)

M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])

print(M)

col_mean = mean(M,axis=0)
row_mean = mean(M, axis=1)
print(col_mean)
print(row_mean)

# variance and standard deviation

from numpy import var

v = array([1,2,3,4,5,6])

print(v)

result = var(v,ddof=1)
print(result)

M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])


col_var = var(M,ddof=1,axis=0)
row_var = var(M, ddof=1 ,axis=1)

print(col_var)
print(row_var)


from numpy import std


M = array([[1,2,3,4,5,6],[1,2,3,4,5,6]])

col_std = std(M,ddof=1,axis=0)
row_std = std(M, ddof=1,axis=1)

print(col_std)
print(row_std)

#covariance and correlation

from numpy import cov

X = array([1,2,3,4,5,6,7,8,9])
y = array([9,8,7,6,5,4,3,2,1])

sigma = cov(X,y)[0,1]
print(sigma)

from numpy import corrcoef 

corr = corrcoef(X,y)[0,1]
print(corr)



X = array([[1,5,8],
           [3,5,11],
           [2,4,9],
           [3,6,10],
           [1,5,10]])

sigma = cov(X.T)

print(sigma)



























