#!/usr/bin/python3
import sys
import copy

def checkDecrease(digits):
	# Check that from left to right, digits never decrease
	decrease = False
	for j in range(len(digits) - 1):
		if digits[j] > digits[j+1]:
			decrease = True
	return decrease

def checkDouble(digits):
	# Check that two adjacent digits are the same.
	# We append a letter to the list because we need to exclude three
	# consecutive digits, so we need j, j+1, and j+2 - so j+2 needs to exist.
	# We manipulate a copy of the original list.
	test = copy.deepcopy(digits)
	test.insert(0,'a')
	test.append('z')
	double = False
	for j in range(1, len(test) - 2):
		if (test[j] == test[j+1]) and (test[j+1] != test[j+2]) and (test[j-1] != test[j]):
			double = True
	return double

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

	candidates = []
	for test in range(minimum, maximum):
		#Set up a list of each digit, in order
		digits = list(str(test))
		# print(str(test) + ': ' + str(digits))

		# Six digit number
		# (this is guaranteed with the range we have)

		# Within the specified range
		# (this is guaranteed by how we set up the loop)

		# Two adjacent digits are the same
		if checkDouble(digits) != True:
			continue
		# print('Doubled digits, we continue')

		# From left to right, digits never decrease
		if checkDecrease(digits):
			continue
		# print('Digits do not decrease, we have a candidate')

		candidates.append(test)
		print('')

	print(str(len(candidates)) + ' possible passwords')
	print(str(candidates))

