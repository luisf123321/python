# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:16:30 2021

@author: luisf
"""

from numpy import array

A = array([[1,2],[3,4],[5,6]])

#transpose
C = A.T

print(C)

#inverse

from numpy.linalg import inv
A = array([[1,2],[3,4]])
B = inv(A)
I = A.dot(B)
print(B)
print(I)


#trace

from numpy import trace

A = array([[1,2,3],[4,5,6],[7,8,9]])

B = trace(A)

print(B)

#determinant

from numpy.linalg import det

A = array([[1,2,3],[4,5,6],[7,8,9]])

B = det(A)

print(B)

#rank

from numpy.linalg import matrix_rank

v1 = array([1,2,3])
vr1 = matrix_rank(v1)
v2 = array([0,0,0,0,0])
vr2 = matrix_rank(v2)

print(vr1)
print(vr2)


M0 = array([[0,0],[0,0]])

mr0 = matrix_rank(M0)

M1 = array([[1,2],[1,2]])

mr1 = matrix_rank(M1)

M2 = array([[1,2],[3,4]])

mr2 = matrix_rank(M2)

print(mr0)
print(mr1)
print(mr2)









