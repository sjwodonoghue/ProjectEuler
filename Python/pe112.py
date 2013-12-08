#!/usr/bin/env python

def isBouncy(n):
	s = str(n);
	for i in range(len(s) - 3):
		inner = int(s[i])
		mid = int(s[i+1])
		outer = int(s[i+2])
		if ((inner < mid & outer < mid) | (inner > mid & outer > mid)):
			return True;
	return False


def main():
	proportion = 0.0;
	i = 1;
	myCount = 0.0;
	while (proportion < 0.5):
		if (isBouncy(i)):
			myCount += 1
		proportion = myCount / i
		print i
		print proportion
		i += 1

main()
