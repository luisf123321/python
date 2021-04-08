#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:30:46 2021

@author: luis
"""

import pandas
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
names = [ 'preg' , 'plas' , 'pres' , 'skin' , 'test' , 'mass' , 'pedi' , 'age' , 'class' ]
data = pandas.read_csv(url, names=names)
peek = data.head(20)
print(peek)

shape = data.shape
print(shape)

types = data.dtypes
print(types)

pandas.set_option( 'display.width' , 100)
pandas.set_option( 'precision' , 3)
description = data.describe()
print(description)


class_counts = data.groupby( 'class' ).size()
print(class_counts)


pandas.set_option( 'display.width' , 100)
pandas.set_option( 'precision' , 3)
correlations = data.corr(method= 'pearson' )
print(correlations)

skew = data.skew()
print(skew)