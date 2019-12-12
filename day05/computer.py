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

	def execute(self):
		# This kicks off the execution of the commands in memory.
		self.showStatus()
		while self.instruction != 99:
			self.op()
			print('--- Next execution ---')
		print('--- Final status ---')
		self.showStatus()

	def load(self, filename):
		# This reads in a file of instructions, and performs initial setup.
		print('Loading ' + str(filename) + '...')
		with open(filename) as file:
			for line in file:
				self.memory = [int(code) for code in line.split(',')]
		file.closed
		self.instruction = self.memory[self.position]
		print('  ...load complete\n')

	def op(self):
		# Lookup instruction
		self.instruction = self.memory[self.position]
		# Quick status check
		print('Position: ' + str(self.position))
		print('Executing instruction: ' + str(self.instruction))		
		operations = {
			1: self.opAdd,
			2: self.opMultiply,
			99: self.opEnd
		}
		func = operations.get(
			self.instruction,
			lambda: 'Invalid operation'
		)
		return func()

	def opAdd(self):
		print('Adding (instruction ' + str(self.instruction) + ')')
		print('')
		one = self.memory[self.memory[self.position+1]]
		two = self.memory[self.memory[self.position+2]]
		result = one + two
		print('Adding ' + str(one) + ' and ' + str(two) + ' to get ' + str(result))
		print('Storing at position ' + str(self.memory[self.position+3]))
		self.memory[self.memory[self.position+3]] = result
		self.position = self.position + 4

	def opMultiply(self):
		print('Multipling (instruction ' + str(self.instruction) + ')')
		print('')
		one = self.memory[self.memory[self.position+1]]
		two = self.memory[self.memory[self.position+2]]
		result = one * two
		print('Adding ' + str(one) + ' and ' + str(two) + ' to get ' + str(result))
		print('Storing at position ' + str(self.memory[self.position+3]))
		self.memory[self.memory[self.position+3]] = result
		self.position = self.position + 4

	def opEnd(self):
		print('Ending')
		print('')

	def showStatus(self):
		# This prints out the state of defined variables and whatnot.
		print('Memory:')
		print(str(self.memory))
		print('Position:    ' + str(self.position))
		print('Instruction: ' + str(self.instruction))
		print('')
