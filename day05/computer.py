# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys

class computer():

	def __init__(self):
		# This defines any needed variables and whatnot.
		print('Booting computer...')
		self.memory = []
		self.position = 0
		self.instruction = -1
		print('  ...boot complete\n')

	def load(self, filename):
		# This reads in a file of instructions, and performs initial setup.
		print('Loading ' + str(filename) + '...')
		with open(filename) as file:
			for line in file:
				self.memory = [int(code) for code in line.split(',')]
		file.closed
		self.instruction = self.memory[self.position]
		print('  ...load complete\n')

	def showStatus(self):
		# This prints out the state of defined variables and whatnot.
		print('Memory:')
		print(str(self.memory))
		print('Position:    ' + str(self.position))
		print('Instruction: ' + str(self.instruction))
