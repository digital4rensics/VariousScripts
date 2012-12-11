#!/usr/bin/env python

"""
OpenIOC2CIF.py
Author: Keith Gilbert - www.digital4rensics.com - @digital4rensics
Version: 1.0
Date: December, 2012

This script take a file in the OpenIOC format (.ioc) and parses indicators CIF can handle.
It returns a .tsv file that can be processed as a CIF feed.
"""


import sys
from BeautifulSoup import BeautifulStoneSoup

def populate(file):
	text = open(file).read()
	soup = BeautifulStoneSoup(text)
	
	return soup

def main():
	ioc = sys.argv[1]
	try:
		output = open(ioc + "_Feed.tsv", "w")
		output.write("Indicator" + "\t" + "Type" + "\t" + "Description" + "\n")
	except:
		print "Could not create file"
		
	xml = populate(ioc)
	
	desc = xml.find('short_description').text
	for element in xml.findAll('indicatoritem'):
		if element.find("context", {"search" : "Network/DNS"}):
			output.write(element.text + "\t" + "Domain" + "\t" + desc + "\n")
		elif element.find("context", {"search" : "PortItem/remoteIP"}):
			output.write(element.text + "\t" + "IPv4" + "\t" + desc + "\n")
		elif element.find("context", {"search" : "UrlHistoryItem/URL"}):
			output.write(element.text + "\t" + "URL" + "\t" + desc + "\n")
		elif element.find("context", {"search" : "FileItem/Md5sum"}):
			output.write(element.text + "\t" + "MD5" + "\t" + desc + "\n")
		elif element.find("context", {"search" : "FileItem/FileName"}):
			output.write(element.text + "\t" + "Filename" + "\t" + desc + "\n")
		else:
			pass
			
	output.close()

if __name__ == '__main__':
	main()