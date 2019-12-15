#!/usr/bin/python3
import sys

def findCenter(start, orbits):
	print('Finding COM from ' + str(start))
	path = {}
	target = orbits.get(start)
	path[start] = target
	while target != 'COM':
		old_target = target
		target = orbits.get(target)
		path[old_target] = target
	print('  ' + str(len(path)) + ' steps')
	print('  ' + str(path))
	print('')
	return path

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

def puzzleOne():
	print('Solving puzzle one\n')
	# Assemble list of planets
	print('Orbiting places')
	places = orbits.keys()
	print(str(places))
	print('')
	# For each list of places, drill back to the center of mass
	total_orbits = 0
	for body in places:

		path = findCenter(body, orbits)
		total_orbits += len(path)

		print('')
	print('Total orbits: ' + str(total_orbits))

def puzzleTwo():
	print('Solving puzzle two\n')
	you = findCenter('YOU', orbits)
	san = findCenter('SAN', orbits)
	joint = set(you.keys()) & set(san.keys())

	print(str(set(you.keys())))
	print(str(set(san.keys())))
	print(str( set(you.keys()) & set(san.keys()) ))

	joint_you = len(you) - len(joint) - 1
	joint_san = len(san) - len(joint) - 1

	print(str(joint_you + joint_san))

def puzzleSwitcher(switch):
	puzzles = {
		"one": puzzleOne,
		"two": puzzleTwo
	}
	func = puzzles.get(switch, 'Invalid choice')
	return func()

if __name__ == "__main__":
	# Load orbital data
	orbits = loadOrbits(sys.argv[1])
	print('Orbits loaded')
	print(str(orbits))
	print('')

	# Identify what puzzle part we're solving
	puzzle = "two" if (len(sys.argv) > 2 and sys.argv[2] == "part2") else "one"
	puzzleSwitcher(puzzle)
