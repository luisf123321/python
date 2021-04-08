# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 18:59:34 2021

@author: luisf
"""

from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig

A = array([[1,2],[3,4],[5,6]])

M = mean(A.T, axis=1)

C = A - M 

V = cov(C.T)

values, vectors = eig(V)

print(vectors)
print(values)

P = vectors.T.dot(C.T)
print(P.T)


from sklearn.decomposition import PCA

A = array([[1,2],[3,4],[5,6]])

pca = PCA(2)
pca.fit(A)
print(pca.components_)
print(pca.explained_variance_)
B = pca.transform(A)
print(B)






