#!/usr/bin/python3
import sys

def castToInt(string):
	return int(string)

def readInputs(filename):
	opcodes = []
	with open(filename) as file:
		for line in file:
			opcodes = line.split(',')
	file.closed
	return [castToInt(foo) for foo in opcodes]

if __name__ == "__main__":
	inputs = readInputs(sys.argv[1])
	print(str(inputs))