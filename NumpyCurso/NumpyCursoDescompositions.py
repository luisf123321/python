# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 17:45:32 2021

@author: luisf
"""

#LU descompositions
# A = LU

from numpy import array

from scipy.linalg import lu

A = array([[1,2,3],[4,5,6],[7,8,9]])

print(A)

P,L,U = lu(A)

print(P)
print(L)
print(U)

B = P.dot(L).dot(U)
print(B)

#QR descomposition
#A = QR

from numpy.linalg import qr

A = array([[1,2],[3,4],[5,6]])
print(A)

Q,R = qr(A,'complete')

print(Q)
print(R)

B = Q.dot(R)
print(B)

#cholesky descomposition
# A = L(L.T) transpose

from numpy.linalg import cholesky

A = array([[2,1,1],[1,2,1],[1,1,2]])

L = cholesky(A)
print(L)

B = L.dot(L.T)

print(B)






















 