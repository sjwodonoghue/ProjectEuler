#!/usr/bin/env python




def main(file):
	f = open(file, 'r')
	prevLine = [int(f.readline().strip())]
	i = 0
	while True:
		lineLst = f.readline().split(" ")
		lineLen = len(lineLst)
		newLine = []
		if lineLst[0] == '' :
			break
		elif lineLen > 1:
			newLine.append(prevLine[0] + int(lineLst[0]))
			for i in range(1, lineLen - 1):
				newLine.append(int(lineLst[i]) + max(prevLine[i-1], prevLine[i]))
			newLine.append(int(lineLst[-1]) + prevLine[-1])
		prevLine = newLine
	f.close()
	return prevLine

print main("pe18.txt")
	

