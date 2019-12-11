#!/usr/bin/python3
import sys

def nextFootprint(footprints, step):
	# Our current location is the last entry in the list of footprints.
	here = footprints[-1].split(',')
	# print('Next step: ' + str(step) + ' from ' + str(here))

	# Split here into x and y coordinates
	x = int(here[0])
	y = int(here[1])

	# Split step into direction and distance
	direction = str(step[:1])
	distance = int(step[1:])

	# Record steps by direction
	for n in range(distance):
		if direction == 'D':
			y -= 1
		if direction == 'L':
			x -= 1
		if direction == 'R':
			x += 1
		if direction == 'U':
			y += 1
		footprints.append(str(x) + ',' + str(y))

	return footprints

def readInputs(filename):
	paths = []
	with open(filename) as file:
		for line in file:
			subset = line.replace('\n','').split(',')
			paths.append(subset)
	file.closed
	return paths

def takeFootprints(steps):
	footprints = []
	footprints.append('0,0')
	for step in steps:
		footprints = nextFootprint(footprints, step)
	# print(str(footprints))
	return footprints

if __name__ == "__main__":
	print('Reading inputs...')
	paths = readInputs(sys.argv[1])
	print('')

	print('Wire paths:')
	print(str(paths))
	print('')

	print('Logging footprints')
	footprints = [takeFootprints(path) for path in paths]
	print('')

	print('Comparing footprints')
	# print(str(footprints))
	pathA = set(footprints[0])
	pathB = set(footprints[1])
	pathsMeet = pathA & pathB
	pathsMeet.remove('0,0') # Don't consider the shared origin
	print('')

	print('Measuring the Manhattan distance to each crossing')
	winner = ''
	winnerDistance = 9999999
	print(str(pathsMeet))
	for intersect in pathsMeet:
		test = intersect.split(',')
		distance = abs(int(test[0])) + abs(int(test[1]))
		print('Intersection ' + str(intersect) + ' at ' + str(test[0]) + ',' + str(test[1]) + ' = ' + str(distance))
		if distance < winnerDistance:
			print('New closest intersection!')
			winnerDistance = distance
			winner = test
	print(str(winner) + ' at distance ' + str(winnerDistance))
	print('')

	print('Measuring fewest steps to an intersection')
	winner = ''
	winnerDistance = len(footprints[0]) + len(footprints[1])
	for intersect in pathsMeet:
		stepsA = footprints[0].index(intersect)
		stepsB = footprints[1].index(intersect)
		distance = stepsA + stepsB
		if distance < winnerDistance:
			print('New fewest steps!')
			winnerDistance = distance
			winner = intersect
	print(str(winner) + ' after ' + str(winnerDistance) + ' combined steps')
	print('')
