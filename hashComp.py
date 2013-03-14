#!/usr/bin/env python

"""
hashComp.py originally written by Keith Gilbert - @digital4rensics
www.digital4rensics.com - March, 2013 - Version 1.0

This script will take an arbitrary number of directories as arguments.
It then processes each file in each directory and stores MD5 hashes of the files.
Only matching files are printed.

No warranty is implied or expressed, use at your own risk.
"""

import hashlib
import sys
import os

matches = {}

for dir in sys.argv[1:]:
	for fname in os.listdir(dir):
		full = dir+fname
		holder = []
		content = open(full, 'r')
		md = hashlib.md5()
		while True:
			data = content.read(128*4096)
			if len(data) == 0:
				break
			md.update(data)
			
		if md.hexdigest() in matches:
			matches[md.hexdigest()].append(fname)
		else:
			holder.append(fname)
			matches[md.hexdigest()] = holder
			
for key in matches:
	if len(matches[key]) >= 2:
		print "\n"
		print key
		for value in matches[key]:
			print value