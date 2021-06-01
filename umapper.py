#!/usr/bin/python

import re
import sys

#Vars
sums={}

# Read file
input=sys.stdin
next(input)
for line in input:
    line=re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r'\W+', line)

    for word in words:
        print(word.lower()+"\t1")
