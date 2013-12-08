#!/usr/bin/env python

import time


def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0)
        return ret
    return wrap
    
@timing
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
	return max(prevLine)

print main("pe67.txt")
	

