T = 10

def controller(error):
	max_error = 50.0
	v = error / max_error
	if v > 1:
		v = 1
	voltage = v * 5
	return voltage

def heat(voltage):
	delta = T / float((1+voltage*T))
	return delta

def cool(voltage):
	delta = -T / float((1+voltage*T))
	return delta

def plant(voltage):
	if voltage > 0:
		delta = heat(voltage)
	else:
		delta = cool(abs(voltage))
	return delta

def main():
	setpoint = 100
	actual = 20
	while (1):
		error = setpoint - actual
		voltage = controller(error)
		delta = plant(voltage)
		actual += delta
		print actual
		raw_input()

main()
