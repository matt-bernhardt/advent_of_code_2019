#!/usr/bin/python3
from __future__ import absolute_import
import itertools
import sys
from thing import thing
from computer import computer
# from ..day05 import computer

def runTrial(digits):
	print("Attempting: " + str(digits))
	interim = 0
	for step in digits:
		c = computer()
		c.load(sys.argv[1])
		c.setInput([step, interim])
		c.execute()
		interim = c.getOutput()
		del c
	print('')
	return interim

if __name__ == "__main__":
	print(str(dir()))
	potential = itertools.permutations('01234', 5)
	j = 0
	highscore = 0
	highscorer = ''
	for item in potential:
		j += 1
		digits = [int(num) for num in item]
		score = runTrial(digits)
		if score > highscore:
			highscore = score
			highscorer = digits
	print('')
	print('-----')
	print(str(j) + ' trials')
	print('High score:  ' + str(highscore))
	print('Winner:      ' + str(highscorer))
