# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 19:34:35 2021

@author: luisf
"""

from numpy import array

#crear un array

l = [1.0,2.0,3.0]
a = array(l)

#display

print(a)
#tamaño
print(a.shape)
#tipo de dato
print (a.dtype)

#crear empty
from numpy import empty

b= empty([3,3])
print(b)

#crear zeros
from numpy import zeros
c = zeros([3,5])
print(c)

#crear unos
from numpy import ones
d= ones([3,5])
print(d)

#stack

from numpy import vstack
a1 = array([1,2,3])
a2 = array([4,5,6])
a3 = vstack((a1,a2))
print(a3)

#hstack
from numpy import hstack
a4 = hstack((a1,a2))
print(a4)





















