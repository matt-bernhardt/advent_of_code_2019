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

	# Determine size of area

	# Initialize playing field to all '.'

	# Loop over wire paths, marking area for each with a character
	  # First wire sets '.' to '1'
	  # Second wire sets '.' to '2' - check if any attempted locations were actually '1'

	# How many collisions were there?
	  # For each collision, calculate manhattan distance to the origin
	  # Smallest manhattan distance wins
