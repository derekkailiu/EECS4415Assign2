#!/usr/bin/python

import re
import sys

#Vars
sums={}

# Read file
input = sys.stdin
next(input)
for line in input:
    line=re.sub(r'^\W+|\W+$|""".*"""', '', line)
    line = line.split(',')
    words=line[10].split(';')

    for word in words:
        print(word.lower()+"\t"+line[0])