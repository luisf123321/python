# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 20:36:40 2021

@author: luisf
"""

#broadcasting

from numpy import array

a = array([1,2,3])

b = 2

c = a + b

print(c)

A = array([[1,2,3],[1,2,3]])

d = A + b

print(d)

e = array([1,2,3])

f = A + e
print(f)


