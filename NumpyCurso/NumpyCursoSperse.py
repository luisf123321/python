# -*- coding: utf-8 -*-
"""
Created on Tue Apr  6 19:28:00 2021

@author: luisf
"""

from numpy import array
from scipy.sparse import csr_matrix

A = array ([[1,0,0,1,0,0],[0,0,2,0,0,1],[0,0,0,2,0,0]])

s = csr_matrix(A)

print(s)

B = s.todense()

print(B)

from numpy import count_nonzero
sparsity = 1 - count_nonzero(A)/A.size
print(sparsity)