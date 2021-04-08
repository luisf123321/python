# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 21:40:34 2021

@author: luisf
"""

from numpy import array

T = array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]],
           [[21,22,23],[24,25,26],[27,28,29]]])

print(T.shape)
print(T)


#addition

A = array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]],
           [[21,22,23],[24,25,26],[27,28,29]]])
B = array([[[1,2,3],[4,5,6],[7,8,9]],[[11,12,13],[14,15,16],[17,18,19]],
           [[21,22,23],[24,25,26],[27,28,29]]])
C = A + B

print(C)

C = A + B

print(C)

C = A*B

print(C)

C = A / B

print(C)

from numpy import tensordot

A = array([1,2])
B = array([3,4])

C = tensordot(A, B,axes=0)

print(C)




 