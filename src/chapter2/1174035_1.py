# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 20:30:07 2019

@author: Intel
"""

NPM = 1174035
char = "#"
if NPM%3==0:
    char = "*"
if NPM%3==1:
    char = "#"
if NPM%3==2:
    char = "+"
line = []
line.append(" ##         ##      ########     ##    ##       #####       #######     ########")
line.append("####       ####      ##    ##    ##    ##      ##   ##     ##     ##    ##      ")
line.append("  ##         ##          ##      ##    ##     ##     ##           ##    ##      ")
line.append("  ##         ##         ##       ##    ##     ##     ##     #######     ####### ")
line.append("  ##         ##        ##        #########    ##     ##           ##          ##")
line.append("  ##         ##        ##              ##      ##   ##     ##     ##    ##    ##")
line.append("######     ######      ##              ##       #####       #######      ###### ")
a=0
for x in line:
    print(line[a].replace("#", char))
    a+=1