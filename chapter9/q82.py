#!/usr/bin/python3
import sys
import random
if __name__ == "__main__":
	for line in open(sys.argv[1],"r"):
		words = line.strip().split(" ")
		N = len(words)
		for i in range(N):
			d = random.randrange(5)+1
			for j in range(d):
				pos = (i-1)-j
				if pos > 0:
					print(words[i],words[pos],sep="\t")
			for j in range(d):
				pos = (i+1)+j
				if pos < N:
					print(words[i],words[pos],sep="\t")
