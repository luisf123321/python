# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:01:20 2021

@author: luisf
"""

from numpy import array
from scipy.linalg import svd

A = array([[1,2],[3,4],[5,6]])

U,s,V = svd(A)

print(U)
print(s)
print(V)


from numpy import  diag
from numpy import zeros
sigma = zeros((A.shape[0],A.shape[1]))
sigma[:A.shape[1],:A.shape[1]] = diag(s)
B = U.dot(sigma.dot(V))

print(B)


#matrices square
A = array([[1,2,3],[4,5,6],[7,8,9]])

U,s,V = svd(A)

sigma = diag(s)
B = U.dot(sigma.dot(V))

print(B)


from numpy.linalg import pinv

A = array([[0.1,0.2],[0.3,0.4],[0.5,0.6],[0.7,0.8]])

B = pinv(A)
print(B)


U,s,V = svd(A)

d = 1/s
D = zeros(A.shape)
D[:A.shape[1],:A.shape[1]] = diag(d)

B = V.T.dot(D.T).dot(U.T)
print(B)

#dimensionality reduction


A = array([[1,2,3,4,5,6,7,8,9,10],
           [11,12,13,14,15,16,17,18,19,20],
           [21,22,23,24,25,26,27,28,29,30]])

U,s,V = svd(A)

sigma = zeros((A.shape[0],A.shape[1]))

sigma[:A.shape[0],:A.shape[0]] = diag(s)

n_elements = 2

sigma = sigma[:,:n_elements]
V = V[:n_elements,:]

B = U.dot(sigma.dot(V))

T = U.dot(sigma)
print(T)
T = A.dot(V.T)
print(T)

from sklearn.decomposition import TruncatedSVD

A = array([[1,2,3,4,5,6,7,8,9,10],
           [11,12,13,14,15,16,17,18,19,20],
           [21,22,23,24,25,26,27,28,29,30]])

svd = TruncatedSVD(n_components=2)
svd.fit(A)
result = svd.transform(A)
print(result)

























