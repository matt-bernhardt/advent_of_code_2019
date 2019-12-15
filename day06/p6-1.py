#!/usr/bin/python3
import sys

def loadOrbits(filename):
	# This returns a list of two-item lists, e.g.
	# [['COM', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']]
	data = {}
	with open(filename) as file:
		for line in file:
			entry = line.replace('\n','').split(')')
			data[entry[1]] = entry[0]
			#data.append(line.replace('\n','').split(')'))
	file.closed
	return data

if __name__ == "__main__":
	# Load orbital data
	orbits = loadOrbits(sys.argv[1])
	print('Orbits loaded')
	print(str(orbits))
	print('')
	# Assemble list of planets
	print('Orbiting places')
	places = orbits.keys()
	print(str(places))
	print('')
	# For each list of places, drill back to the center of mass
	total_orbits = 0
	for body in places:
		print(str(body))
		target = orbits.get(body)
		print('Starting with ' + str(target))
		count = 1
		while target != 'COM':
			target = orbits.get(target)
			count += 1
			print('Found ' + str(target))
		print('Orbit count: ' + str(count))
		total_orbits += count
		print('')
	print('Total orbits: ' + str(total_orbits))
