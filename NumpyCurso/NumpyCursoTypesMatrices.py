# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:09:03 2021

@author: luisf
"""

from numpy import array

from numpy import tril

from numpy import triu

M = array([[1,2,3],[1,2,3],[1,2,3]])

print(M)

lower = tril(M)
upper = triu(M)

print(lower)
print(upper)

from numpy import diag

M = array([[1,2,3],[1,2,3],[1,2,3]])

d = diag(M)
D = diag(d)

print(d)
print(D)

from numpy import identity

I = identity(3)

print(I)

#orthogonal

from numpy.linalg import inv

Q = array([[1,0],[0,-1]])

V = inv(Q)
print(Q.T)
print(V)
I = Q.dot(Q.T)
print(I)






