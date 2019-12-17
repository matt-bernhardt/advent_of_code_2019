#!/usr/bin/python3
import sys

def chunkLine(data, rowlength):
	rowlength = int(rowlength)
	print('Starting to chunk line of length ' + str(len(data)))
	print('  into chunks of size ' + str(rowlength))
	result = []
	while len(data) > 0:
		print('Chunk: ' + str(data[:rowlength]))
		result.append(data[:rowlength])
		data = data[rowlength:]
	print('')
	return result

def loadImage(filename, rowlength):
	# This returns a list of pixel values, split by the number of pixels in
	# each row. For an image that is 3 pixels wide by 2 high (in 2 layers),
	# this results in:
	#
	# 123
	# 456
	#
	# 789
	# 012
	data = ''
	with open(filename) as file:
		for line in file:
			data = line
	file.closed
	print(str(data))
	# We now have one long list of pixels
	# Need to split this over rowlength
	data = chunkLine(data, rowlength)
	return data

def outputLayer(layer):
	print(str(layer.replace('',' ')))
	# [print(str(char) + ' ') for char in layer]

def summarizeLayer(layer):
	result = {}
	result['zeros'] = layer.count('0')
	result['ones'] = layer.count('1')
	result['twos'] = layer.count('2')
	print(str(result))
	return result

if __name__ == "__main__":
	# Load image data
	sample = loadImage(sys.argv[1], sys.argv[2])
	print('Image loaded')
	print(str(sample))
	print('')

	foo = [summarizeLayer(line) for line in sample]
	print(str(foo))

	[outputLayer(line) for line in sample]
