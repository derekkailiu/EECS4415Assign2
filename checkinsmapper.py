#!/usr/bin/python

import re
import sys


# Read from stdin
input = sys.stdin;
next(input)
for line in input:
    line = re.sub(r'^\W+|\W+$', '', line)
    line = line.split(',')
    print(line[0] + ', ' + line[1] + ',' + '\t'+ line[3])
