T = 10

def controller(error, Kp, Ki, prev, i):
	"""Kp is proportional gain
	Ki is integral gain
	prev is the previous error
	i is the integral term"""
	i += prev
	i_ = Ki*i*error
	p_ = Kp*error
	print i_
	print p_
	total = Kp*error + Ki*i*error

	"""This is just dummy code for now to convert to Volts.
	This implementation can be improved"""
	max_error = 50.0
	v = error / max_error
	if v > 1:
		v = 1
	voltage = v * 5
	return voltage, i

def heat(voltage):
	"""Assuming that s in the transfer function is voltage,
	then the change made by the actuator is smaller as the voltage
	increases, so clearly I'm using the transfer function wrong"""
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
	prev = 0
	i = 0
	while (1):
		error = setpoint - actual
		voltage, i = controller(error, .5, 0.05, prev, i)
		delta = plant(voltage)
		actual += delta
		print actual
		prev = error
		raw_input()

main()
