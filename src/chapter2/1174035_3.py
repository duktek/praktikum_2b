# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:40:11 2019

@author: Intel
"""
print("Input : ")
NPM = input()
jumlah = len(NPM)
a = int(NPM[jumlah-3])
b = int(NPM[jumlah-2])
c = int(NPM[jumlah-1])
x=1
while x <= (a+b+c):
    print("Output : "+NPM[jumlah-3:])
    x+=1