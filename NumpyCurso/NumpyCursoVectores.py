# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 18:49:54 2021

@author: luisf
"""

from numpy import array

v = array([1,2,3])

print(v)

#addiction

a = array([1,2,3])

b = array([1,2,3])

c = a + b

print (c)

#subtraction

a = array([1,2,3])

b = array([0.5,0.5,0.5])

c = a - b

print(c)

#multiplication

a = array([1,2,3])

b = array([1,2,3])

c = a * b

print(c)

#division

a = array([1,2,3])

b = array([1,2,3])

c = a / b

print(c)

# dot product

a = array([1,2,3])

b = array([1,2,3])

c = a.dot(b)

print(c)

#scalar multiplication

a = array([1,2,3])

s = 0.5

c = s*a

print(c)

#vector norms
#norm l1

from numpy.linalg import norm


a = array([1,2,3])

l1 = norm(a,1)

print(l1)

#norm l2

a = array([1,2,3])

l2 = norm(a)

print(l2)


#vector max norm

from math import inf
a = array([1,2,3])

maxnorm = norm(a,inf)

print(maxnorm)



























