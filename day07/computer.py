# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys

class computer():

	def __init__(self):
		# This defines any needed variables and whatnot.
		print('Booting computer...')
		self.memory = []
		self.position = 0
		# input is being used during day 7 for chaining computers together
		self.input = False
		# intcode is the entire first instruction, including parameter values.
		self.intcode = -1
		# instruction is the numeric instruction code only - the right two
		# digits of intcode.
		self.instruction = -1
		# output is being used during day 7 for chaining computers together
		self.output = 0
		# parameters have to do with whether each command's argument is
		# specified in "position" or "immediate" mode.
		self.parameters = ''
		print('  ...boot complete\n')

	def execute(self):
		# This kicks off the execution of the commands in memory.
		self.showStatus()
		while self.instruction != 99:
			print('--- Next execution ---')
			self.op()
		print('--- Final status ---')
		self.showStatus()

	def getOutput(self):
		return self.output

	def load(self, filename):
		# This reads in a file of instructions, and performs initial setup.
		print('Loading ' + str(filename) + '...')
		with open(filename) as file:
			for line in file:
				self.memory = [int(code) for code in line.split(',')]
		file.closed
		self.instruction = self.memory[self.position]
		print('  ...load complete\n')

	def nextInput(self):
		thisInput = self.input[0]
		self.input.pop(0)
		return thisInput

	def op(self):
		# Lookup instruction
		# The first parameter is the intcode, documented at:
		# https://adventofcode.com/2019/day/5
		self.intcode = str(self.memory[self.position])
		self.instruction = int(self.intcode[-2:])
		self.parameters = [char for char in str(self.intcode[:-2]).zfill(3)]
		self.parameters.reverse()
		# Parameters are:
		# 0 (or empty) - positional mode - the argument refers to a memory location
		# 1 - immediate mode - the argument is the number itself
		# Parameters read right to left.
		# 
		# Example:
		# ABCDE
		#  1002
		#
		# DE - two-digit opcode,      02 == opcode 2 (multiply)
		#  C - mode of 1st parameter,  0 == position mode
		#  B - mode of 2nd parameter,  1 == immediate mode
		#  A - mode of 3rd parameter,  0 == position mode,
		#                                   omitted due to being a leading zero
		# Quick status check
		print('  Position: ' + str(self.position))
		print('    Memory excerpt: ' + str(self.memory[self.position:self.position+4]))
		print('  Intcode: ' + str(self.intcode))
		print('    Instruction: ' + str(self.instruction))
		print('    Parameters: ' + str(self.parameters))
		operations = {
			1: self.opAdd,
			2: self.opMultiply,
			3: self.opInput,
			4: self.opOutput,
			5: self.opJumpIfTrue,
			6: self.opJumpIfFalse,
			7: self.opLessThan,
			8: self.opEquals,
			99: self.opEnd
		}
		func = operations.get(
			self.instruction,
			'Invalid operation'
		)
		return func()

	def opAdd(self):
		# Inputs:
		# Number one
		# Number two
		# Result storage location
		print('Adding (instruction ' + str(self.instruction) + ')')
		inputs = self.setInputs(2, self.position+1)
		result = inputs[0] + inputs[1]
		print('Storing at position ' + str(self.memory[self.position+3]))
		self.memory[self.memory[self.position+3]] = result
		self.position = self.position + 4
		print('')

	def opEquals(self):
		# If the first parameter is equal to the second parameter, it stores 1
		# in the position given by the third parameter. Otherwise, it stores 0.
		print('Equals')
		inputs = self.setInputs(3, self.position+1)
		newValue = 1 if inputs[0] == inputs[1] else 0
		self.memory[self.memory[self.position+3]] = newValue
		self.position = self.position + 4
		print('')

	def opInput(self):
		print('Getting input for position ' + str(self.memory[self.position+1]))
		self.memory[self.memory[self.position+1]] = self.nextInput() if len(self.input) > 0 else int(input('Provide your input: '))
		self.position = self.position + 2
		print('')

	def opJumpIfFalse(self):
		# If the first parameter is zero, it sets the instruction pointer to
		# the value from the second parameter. Otherwise, it does nothing.
		print('Jump If False')
		inputs = self.setInputs(2, self.position+1)
		print('Is ' + str(inputs[0]) + ' false?')
		if inputs[0] == 0:
			print('Yes, is false. Jumping...')
			self.position = inputs[1]
		else:
			print('No, is not false. Moving to next instruction...')
			self.position = self.position + 3
		print('')

	def opJumpIfTrue(self):
		# If the first parameter is non-zero, it sets the instruction pointer
		# to the value from the second parameter. Otherwise, it does nothing.
		print('Jump If True')
		inputs = self.setInputs(2, self.position+1)
		print('Is ' + str(inputs[0]) + ' true?')
		if inputs[0] != 0:
			print('Yes, is true. Jumping...')
			self.position = inputs[1]
		else:
			print('No, is not true. Moving to next instruction...')
			self.position = self.position + 3
		print('')

	def opLessThan(self):
		# If the first parameter is less than the second parameter, it stores
		# 1 in the position given by the third parameter. Otherwise, it stores
		# 0.
		print('Less Than')
		inputs = self.setInputs(3, self.position+1)
		newValue = 1 if inputs[0] < inputs[1] else 0
		self.memory[self.memory[self.position+3]] = newValue
		self.position = self.position + 4
		print('')

	def opMultiply(self):
		# Inputs:
		# Number one
		# Number two
		# Result storage location
		print('Multipling (instruction ' + str(self.instruction) + ')')
		inputs = self.setInputs(2, self.position+1)
		result = inputs[0] * inputs[1]
		print('Storing at position ' + str(self.memory[self.position+3]))
		self.memory[self.memory[self.position+3]] = result
		self.position = self.position + 4
		print('')

	def opOutput(self):
		print('Printing output from position ' + str(self.memory[self.position+1]))
		inputs = self.setInputs(1, self.position+1)
		self.output = inputs[0]
		print('\n\n==>')
		print('==> Output: ' + str(inputs[0]))
		print('==>\n\n')
		self.position = self.position + 2
		print('')

	def opEnd(self):
		print('Ending')
		print('')

	def setInput(self, input):
		self.input = input

	def setInputs(self, count, position):
		print('Defining ' + str(count) + ' operation inputs from position ' + str(position))
		inputs = []
		for x in range(count):
			print('  Parameter ' + str(x) + ' (mode ' + str(self.parameters[x]) + ')')
			if 0 == int(self.parameters[x]):
				# Position mode
				print('    Loading from position ' + str(self.memory[position+x]))
				inputs.append(self.memory[self.memory[position+x]])
			else:
				# Immediate mode
				print('    Setting input directly to ' + str(self.memory[position+x]))
				inputs.append(self.memory[position+x])
		print('Inputs set to: ' + str(inputs))
		return inputs

	def showStatus(self):
		# This prints out the state of defined variables and whatnot.
		print('Memory:')
		print(str(self.memory))
		print('Position:    ' + str(self.position))
		print('Instruction: ' + str(self.instruction))
		print('')
