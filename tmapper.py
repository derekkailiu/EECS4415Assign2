#!/usr/bin/python

import re
import sys


# Read from stdin
input=sys.stdin
next(input)
for line in input:
    line = re.sub(r'^\W+|\W+$', '', line)
    line = re.split(r'\W+', line)

    for i in range (2,len(line)):
        tup = (line[i-2].lower(),line[i-1].lower(),line[i].lower())
        print(str(tup) + '\t1' )