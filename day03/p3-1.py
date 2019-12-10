#!/usr/bin/python3
import sys

def readInputs(filename):
	paths = []
	with open(filename) as file:
		for line in file:
			subset = line.replace('\n','').split(',')
			paths.append(subset)
	file.closed
	return paths

if __name__ == "__main__":
	print('Reading inputs...')
	paths = readInputs(sys.argv[1])
	print('')

	print('Wire paths:')
	print(str(paths))
