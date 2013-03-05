#!/usr/bin/env python

"""
PairSort.py originally written by Keith Gilbert - @digital4rensics
www.digital4rensics.com - 3/4/12 - Version 0.2

This script will parse comma separated elements in a file (2 per line) and produce
a full list of matches for each element. Example output is below.

No warranty is implied or expressed, use at your own risk.

usage: PairSort.py [-h] [-c COUNT] source destination

Parse comma separated pairs and output unique matches by element

positional arguments:
  source                Specify the source data file
  destination           Specify the destination data file

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        Set the threshold for minimum number of matches to be
                        included in the output
"""

import sys
import argparse

parser = argparse.ArgumentParser(description="Parse comma separated pairs and output unique matches by element")
parser.add_argument("source", help="Specify the source data file")
parser.add_argument("destination", help="Specify the destination data file")
parser.add_argument("-c", "--count", type=int, help="Set the threshold for minimum number of matches to be included in the output")

args = parser.parse_args()

data = open(args.source, 'r')

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

out = open(args.destination, 'w')
if args.count:
	for key in pairs:
		if len(pairs[key]) >= args.count:
			out.write(key + ":\n")
			for entry in pairs[key]:
				out.write("\t" + entry + "\n")
			out.write("\n")
else:
	for key in pairs:
		out.write(key + ":\n")
		for entry in pairs[key]:
			out.write("\t" + entry + "\n")
		out.write("\n")

out.close()