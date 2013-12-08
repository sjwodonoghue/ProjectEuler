#!/usr/bin/env python

import math




def main():
	ans = 0
	global alph 
	alph = {}
	for i in range(65,91):
		alph[chr(i)] = ord(chr(i)) - 64

	f = open("names.txt", "r")

	line = f.readline()
	line = line.split(",")
	line.sort()

	for i in range(len(line)):
		line[i] = line[i].strip("\"")
		line[i] = line[i].strip("\]")
		ans += wordval(line[i]) * (i + 1)			
	
	f.close()
	print ans

def wordval(s):
	val = 0
	for letter in s:
		val += alph[letter]
	return val
		

main()