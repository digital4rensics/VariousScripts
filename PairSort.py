#!/usr/bin/env python

"""
This script will parse comma separated elements in a file (2 per line) and produce
a full list of matches for each element. Example output is below.

No warranty is implied or expressed, use at your own risk.

USAGE: python PairSort.py <INPUT FILE> <OUTPUT FILE>

Input:
	a,b
	b,c
	b,a
	c,d
Output:
	a: b
	b: c,a
	c: b,d
	d: c
"""

import sys

target = sys.argv[1]
dest = sys.argv[2]

data = open(target, 'r')

pairs = {}

for line in data:
	holder = []
	elems = line.split(',')
	if elems[0].strip() in pairs:
		if elems[1].strip() not in pairs[elems[0].strip()]:
			pairs[elems[0].strip()].append(elems[1].strip())
	else:
		holder.append(elems[1].strip())
		pairs[elems[0].strip()] = holder
	
	holder = []
	if elems[1].strip() in pairs:
		if elems[0].strip() not in pairs[elems[1].strip()]:
			pairs[elems[1].strip()].append(elems[0].strip())
	else:
		holder.append(elems[0].strip())
		pairs[elems[1].strip()] = holder

data.close()

out = open(dest, 'w')

for key in pairs:
	out.write(key + ":\n")
	for entry in pairs[key]:
		out.write("\t" + entry + "\n")
	out.write("\n")

out.close()