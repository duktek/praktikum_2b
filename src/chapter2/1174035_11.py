# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:18:25 2019

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
for x in arr:
    if x!=0:
        i = 1
        bil = 0
        while i <= x:
            if x%i==0:
                bil+=1
            i+=1
        if bil == 2:
            print(x)