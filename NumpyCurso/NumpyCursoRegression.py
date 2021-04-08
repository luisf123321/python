# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 19:07:16 2021

@author: luisf
"""

from numpy import array 
from matplotlib import pyplot

data = array([[0.05, 0.12],[0.18,0.22],[0.31,0.35],[0.42,0.38],[0.5,0.49]])

X, y = data[:,0],data[:,1]
X = X.reshape((len(X),1))

pyplot.scatter(X,y)
pyplot.show()

#solve via inverse
from numpy.linalg import inv

b = inv(X.T.dot(X)).dot(X.T).dot(y)
print(b)

yhat = X.dot(b)

pyplot.scatter(X,y)
pyplot.plot(X,yhat,color='red')
pyplot.show()

#solve via QR

from numpy.linalg import qr

Q,R = qr(X)
b = inv(R).dot(Q.T).dot(y)
print(b)
yhat = X.dot(b)

pyplot.scatter(X,y)
pyplot.plot(X,yhat,color='red')
pyplot.show()

#solve via SVD

from numpy.linalg import pinv

b = pinv(X).dot(y)
print(b)
yhat = X.dot(b)

pyplot.scatter(X,y)
pyplot.plot(X,yhat,color='red')
pyplot.show()

#solve va convenience function

from numpy.linalg import lstsq


b, residuals, rank, s = lstsq(X, y,rcond=-1)
print(b)

yhat = X.dot(b)

pyplot.scatter(X,y)
pyplot.plot(X,yhat,color='red')
pyplot.show()
















