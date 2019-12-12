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
		double = False
		for j in range(len(digits) - 1):
			if digits[j] == digits[j+1]:
				double = True
		if not double:
			#  print('No doubled digits\n')
			continue
		# print('Doubled digits, we continue')

		# From left to right, digits never decrease
		decrease = False
		for j in range(len(digits) - 1):
			if digits[j] > digits[j+1]:
				decrease = True
		if decrease:
			# print('Digits decrease \n')
			continue
		# print('Digits do not decrease, we have a candidate')

		candidates.append(test)
		# print('')

	print(str(len(candidates)) + ' possible passwords')
	print(str(candidates))

