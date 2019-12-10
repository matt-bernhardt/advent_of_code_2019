def calculateFuel(mass):
	return int( mass / 3 ) - 2

def calculateFuelTotal(mass):
	fuellist = []
	while mass > 0:
		fuel = calculateFuel(mass)
		if fuel > 0:
			fuellist.append(fuel)
		mass = fuel
	return sum(fuellist)

def getData(filename):
	data = []
	with open(filename) as file:
		for line in file:
			data.append(int(line))
	file.closed
	return data

if __name__ == "__main__":
	inputs = getData('fuel.txt')
	# inputs = [12, 14, 1969, 100756]

	output = [calculateFuelTotal(item) for item in inputs]

	print(str(sum(output)))
