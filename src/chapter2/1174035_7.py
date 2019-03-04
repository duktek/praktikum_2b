# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:06:55 2019

@author: Intel
"""

a = 1
b = 1
c = 7
d = 4
e = 0
f = 3
g = 5

arr = []
arr.append(a)
arr.append(b)
arr.append(c)
arr.append(d)
arr.append(e)
arr.append(f)
arr.append(g)
jum = 1
for x in arr:
    jum*=x
print("Hasil : "+str(jum))