# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 19:28:47 2019

@author: Intel
"""
a = 2
b = 'Coba'
try:
    print(a + b)
except TypeError:
    print("Integer dan String Tidak Dapat Dijumlah Karena Berbeda Tipe")