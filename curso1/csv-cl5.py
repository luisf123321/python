#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:57:22 2021

@author: luis
"""

import csv
import numpy
filename = 'pima-indians-diabetes.csv'
raw_data = open(filename, "r" )
reader = csv.reader(raw_data, delimiter= "," , quoting=csv.QUOTE_NONE)
x = list(reader)
data = numpy.array(x).astype( 'float' )
print(data.shape)

import pandas
filename = 'pima-indians-diabetes.csv'
names = [ 'preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
data = pandas.read_csv(filename, names=names)
print(data.shape)