#!/usr/bin/python3
import sys

def readInputs(filename):
	ranges = []
	with open(filename) as file:
		for line in file:
			ranges = line.split('-')
	file.closed
	return ranges

if __name__ == "__main__":
	print('Reading range')
	ranges = readInputs(sys.argv[1])
	minimum = int(ranges[0])
	maximum = int(ranges[1])
	print(str(ranges))
	print('')

	for test in range(minimum, maximum):
		print(str(test))
