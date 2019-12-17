#!/usr/bin/python3
# from __future__ import absolute_import
import itertools
import sys
from computer import computer

def runTrial(digits):
	print("Attempting: " + str(digits))

	# Boot up each computer
	c0 = computer()
	c0.load(sys.argv[1])

	c1 = computer()
	c1.load(sys.argv[1])

	c2 = computer()
	c2.load(sys.argv[1])

	c3 = computer()
	c3.load(sys.argv[1])

	c4 = computer()
	c4.load(sys.argv[1])

	print("All computers booted")

	c0.setInput([digits[0], 0])
	c0.execute()
	interim = c0.getOutput()

	print('---')

	c1.setInput([digits[1], interim])
	c1.execute()
	interim = c1.getOutput()

	print('---')

	c2.setInput([digits[2], interim])
	c2.execute()
	interim = c2.getOutput()

	print('---')

	c3.setInput([digits[3], interim])
	c3.execute()
	interim = c3.getOutput()

	print('---')

	c4.setInput([digits[4], interim])
	c4.execute()
	interim = c4.getOutput()

	print('---')

	print('')
	return interim

if __name__ == "__main__":
	print(str(dir()))
	potential = itertools.permutations('56789', 5)
	j = 0
	highscore = 0
	highscorer = ''

	digits = [9,7,8,5,6]

	score = runTrial(digits)

	# for item in potential:
	# 	j += 1
	# 	digits = [int(num) for num in item]
	# 	score = runTrial(digits)
	# 	if score > highscore:
	# 		highscore = score
	# 		highscorer = digits
	print('')
	print('-----')
	print(str(j) + ' trials')
	print('High score:  ' + str(highscore))
	print('Winner:      ' + str(highscorer))
