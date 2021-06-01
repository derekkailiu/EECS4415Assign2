#!/usr/bin/python

import sys
import re

previous=None
sum=[]

for line in sys.stdin:
    line=re.sub(r'^\W+|\W+$', '', line)
    key, value = line.split('\t')

    if key != previous:
        if previous is not None:
            print (previous + '\t' + str(sum))
        previous = key
        sum = []

    sum.append(value)

print (previous + 't' + str(sum))