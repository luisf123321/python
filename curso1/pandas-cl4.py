#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:47:40 2021

@author: luis
"""

# series
import numpy
import pandas
myarray = numpy.array([1, 2, 3])
rownames = [ ' a ' , ' b ' , ' c ' ]
myseries = pandas.Series(myarray, index=rownames)
print(myseries)

print(myseries[0])
print(myseries[ ' a ' ])


#datframe
myarray = numpy.array([[1, 2, 3], [4, 5, 6]])
rownames = [ 'a' , 'b' ]
colnames = [ 'one' , 'two' , 'three' ]
mydataframe = pandas.DataFrame(myarray, index=rownames, columns=colnames)
print(mydataframe)

print("method 1:")
print(("one column: %s") % mydataframe[ 'one' ])
print(("method 2:"))
print(("one column: %s") % mydataframe.one)