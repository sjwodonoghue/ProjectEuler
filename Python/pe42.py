#!/usr/bin/env python

import math




def main():
	ans = 0
	ans2 = 0
	nums = triNums(100)
	print nums
	global alph 
	alph = {}
	for i in range(65,91):
		alph[chr(i)] = ord(chr(i)) - 64

	f = open("words.txt", "r")

	line = f.readline()
	line = line.split(",")


	for i in range(len(line)):
		line[i] = line[i].strip("\"")
		line[i] = line[i].strip("\]")
		if (wordval(line[i]) in nums):
			print line[i]
			ans2 += 1
			
		if (isTri(wordval(line[i]))):
			#print line[i]
			#print wordval(line[i])
			ans += 1
			
		
	f.close()
	print ans
	print ans2

def wordval(s):
	val = 0
	for letter in s:
		val += alph[letter]
	return val
		
def isTri(n):
	x = math.sqrt((8 * n) + 1)
	#print x
	if isInt(x):
		return True
	else:
		return False
	
def isInt(n):
	if ((math.floor(n) - n) == 0 ):
		return True
	else:
		return False
		
def triNums(n):
	ans = []
	for i in range(1,n):
		ans.append((i * (i + 1)) / 2)
	return ans

main()