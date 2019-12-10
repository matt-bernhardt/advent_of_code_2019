#!/usr/bin/python3
import sys

def castToInt(string):
	return int(string)

def lookupOp(code, position, data):
	status(code, position, data)
	opList={
		1:opAdd,
		2:opMultiply,
		99:opEnd
	}
	func = opList.get(code, lambda:'Invalid operation')
	return func(code, position, data)

def opAdd(code, position, data):
	print('Adding')
	one = data[data[position+1]]
	two = data[data[position+2]]
	result = one + two
	data[data[position+3]] = result
	code = data[position+4]
	position = position + 4
	print('Result: ' + str(data))
	return code, position, data

def opMultiply(code, position, data):
	print('Multiplying')
	one = data[data[position+1]]
	two = data[data[position+2]]
	result = one * two
	data[data[position+3]] = result
	code = data[position+4]
	position = position + 4
	return code, position, data

def opEnd(code, position, data):
	print('Ending')
	return code, position, data

def readInputs(filename):
	opcodes = []
	with open(filename) as file:
		for line in file:
			opcodes = line.split(',')
	file.closed
	return [castToInt(foo) for foo in opcodes]

def status(code, position, data):
	print('Data: ' + str(data))
	print('Pos:  ' + str(position))
	print('Code: ' + str(data[position]))
	print('')

if __name__ == "__main__":
	print('Reading inputs...')
	intCodes = readInputs(sys.argv[1])
	thisPos = 0
	thisCode = intCodes[thisPos]
	print('')

	print('Initial condition:')
	status(thisCode, thisPos, intCodes)
	print('--- Beginning execution ---')
	print('')

	while thisCode != 99:
		thisCode, thisPos, intCodes = lookupOp(thisCode, thisPos, intCodes)

		print('')
		print('--- Next execution ---')
		print('')

	print('--- Final status ---')
	status(thisCode, thisPos, intCodes)
