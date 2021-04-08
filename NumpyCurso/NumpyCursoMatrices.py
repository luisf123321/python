# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:00:20 2021

@author: luisf
"""

from numpy import array

A = array([[1,2,3],[4,5,6]])

print(A)

#addiction
A = array([[1,2,3],[4,5,6]])

B = array([[1,2,3],[4,5,6]])

C = A + B
print(C)

#subtraction

A = array([[1,2,3],[4,5,6]])

B = array([[0.5,0.5,0.5],[0.5,0.5,0.5]])

C = A - B
print(C)

#multiplication
A = array([[1,2,3],[4,5,6]])

B = array([[1,2,3],[4,5,6]])

C = A * B

print(C)

#division

A = array([[1,2,3],[4,5,6]])

B = array([[1,2,3],[4,5,6]])

C = A / B

print(C)

#matrix-matrix multiplication


A = array([[1,2],[3,4],[5,6]])

B = array([[1,2],[3,4]])

C = A.dot(B)

print(C)

#matrix - vector


A = array([[1,2],[3,4],[5,6]])

B = array([0.5,0.5])

C = A.dot(B)

print(C)

#scalar
A = array([[1,2],[3,4],[5,6]])

b = 0.5

C = A*b

print(C)


















