# -*- coding: utf-8 -*-
from __future__ import absolute_import
import sys

class computer():

	verbose = True

	def __init__(self):
		# This defines any needed variables and whatnot.
		self.log('Booting computer...')
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
		self.log('  ...boot complete\n')

	def execute(self):
		# This kicks off the execution of the commands in memory.
		self.showStatus()
		while self.instruction != 99:
			self.log('--- Next execution ---')
			self.op()
		self.log('--- Final status ---')
		self.showStatus()

	def getOutput(self):
		return self.output

	def load(self, filename):
		# This reads in a file of instructions, and performs initial setup.
		self.log('Loading ' + str(filename) + '...')
		with open(filename) as file:
			for line in file:
				self.memory = [int(code) for code in line.split(',')]
		file.closed
		self.instruction = self.memory[self.position]
		self.log('  ...load complete\n')

	def log(self, message):
		if self.verbose:
			print(str(message))

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
		self.log('  Position: ' + str(self.position))
		self.log('    Memory excerpt: ' + str(self.memory[self.position:self.position+4]))
		self.log('  Intcode: ' + str(self.intcode))
		self.log('    Instruction: ' + str(self.instruction))
		self.log('    Parameters: ' + str(self.parameters))
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
		self.log('Adding (instruction ' + str(self.instruction) + ')')
		inputs = self.setInputs(2, self.position+1)
		result = inputs[0] + inputs[1]
		self.log('Storing at position ' + str(self.memory[self.position+3]))
		self.memory[self.memory[self.position+3]] = result
		self.position = self.position + 4
		self.log('')

	def opEquals(self):
		# If the first parameter is equal to the second parameter, it stores 1
		# in the position given by the third parameter. Otherwise, it stores 0.
		self.log('Equals')
		inputs = self.setInputs(3, self.position+1)
		newValue = 1 if inputs[0] == inputs[1] else 0
		self.memory[self.memory[self.position+3]] = newValue
		self.position = self.position + 4
		self.log('')

	def opInput(self):
		self.log('Getting input for position ' + str(self.memory[self.position+1]))
		self.memory[self.memory[self.position+1]] = self.nextInput() if len(self.input) > 0 else int(input('Provide your input: '))
		self.position = self.position + 2
		self.log('')

	def opJumpIfFalse(self):
		# If the first parameter is zero, it sets the instruction pointer to
		# the value from the second parameter. Otherwise, it does nothing.
		self.log('Jump If False')
		inputs = self.setInputs(2, self.position+1)
		self.log('Is ' + str(inputs[0]) + ' false?')
		if inputs[0] == 0:
			self.log('Yes, is false. Jumping...')
			self.position = inputs[1]
		else:
			self.log('No, is not false. Moving to next instruction...')
			self.position = self.position + 3
		self.log('')

	def opJumpIfTrue(self):
		# If the first parameter is non-zero, it sets the instruction pointer
		# to the value from the second parameter. Otherwise, it does nothing.
		self.log('Jump If True')
		inputs = self.setInputs(2, self.position+1)
		self.log('Is ' + str(inputs[0]) + ' true?')
		if inputs[0] != 0:
			self.log('Yes, is true. Jumping...')
			self.position = inputs[1]
		else:
			self.log('No, is not true. Moving to next instruction...')
			self.position = self.position + 3
		self.log('')

	def opLessThan(self):
		# If the first parameter is less than the second parameter, it stores
		# 1 in the position given by the third parameter. Otherwise, it stores
		# 0.
		self.log('Less Than')
		inputs = self.setInputs(3, self.position+1)
		newValue = 1 if inputs[0] < inputs[1] else 0
		self.memory[self.memory[self.position+3]] = newValue
		self.position = self.position + 4
		self.log('')

	def opMultiply(self):
		# Inputs:
		# Number one
		# Number two
		# Result storage location
		self.log('Multipling (instruction ' + str(self.instruction) + ')')
		inputs = self.setInputs(2, self.position+1)
		result = inputs[0] * inputs[1]
		self.log('Storing at position ' + str(self.memory[self.position+3]))
		self.memory[self.memory[self.position+3]] = result
		self.position = self.position + 4
		self.log('')

	def opOutput(self):
		self.log('Printing output from position ' + str(self.memory[self.position+1]))
		inputs = self.setInputs(1, self.position+1)
		self.output = inputs[0]
		print('\n\n==>')
		print('==> Output: ' + str(inputs[0]))
		print('==>\n\n')
		self.position = self.position + 2
		self.log('')

	def opEnd(self):
		self.log('Ending')
		self.log('')

	def setInput(self, input):
		self.input = input

	def setInputs(self, count, position):
		self.log('Defining ' + str(count) + ' operation inputs from position ' + str(position))
		inputs = []
		for x in range(count):
			self.log('  Parameter ' + str(x) + ' (mode ' + str(self.parameters[x]) + ')')
			if 0 == int(self.parameters[x]):
				# Position mode
				self.log('    Loading from position ' + str(self.memory[position+x]))
				inputs.append(self.memory[self.memory[position+x]])
			else:
				# Immediate mode
				self.log('    Setting input directly to ' + str(self.memory[position+x]))
				inputs.append(self.memory[position+x])
		self.log('Inputs set to: ' + str(inputs))
		return inputs

	def showStatus(self):
		# This prints out the state of defined variables and whatnot.
		self.log('Memory:')
		self.log(str(self.memory))
		self.log('Position:    ' + str(self.position))
		self.log('Instruction: ' + str(self.instruction))
		self.log('')
