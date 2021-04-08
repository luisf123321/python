# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:54:46 2021

@author: luisf
"""

from numpy import array
from numpy.linalg import eig

A = array([[1,2,3],[4,5,6],[7,8,9]])

values, vectors = eig(A)

print(values)
print(vectors)

B = A.dot(vectors[:,0])

C = vectors[:,0]*values[0]

print(B)
print(C)
from numpy import diag
from numpy.linalg import inv
Q = vectors

R = inv(Q)

L = diag(values)

B = Q.dot(L).dot(R)
print(B)


















