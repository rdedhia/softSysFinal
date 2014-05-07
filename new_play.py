import numpy
import matplotlib.pyplot as plot

T = 10

def controller(error, Kp, Ki, prev, i):
	"""Kp is proportional gain
	Ki is integral gain
	prev is the previous error
	i is the integral term"""
	i += prev
	i_ = Ki*i*error
	p_ = Kp*error
	print 'i', i
	print 'i_', i_
	print 'p_', p_
	print '\n'
	#print i_
	#print p_

	total = Kp*error + Ki*abs(i)*error
	print total

	"""This is just dummy code for now to convert to Volts.
	This implementation can be improved"""

	"""I think the problem with this implementation was that we were returning voltage linearly proportional to the error. 
	The controller takes in error, but what we want it to output is a scaled version of total"""
	#max_error = 50.0
	#v = error / max_error
	max_correction = 1000.0
	v = float(total)/float(max_correction)
	if v > 1:
		v = 1
	if v < -1:
		v = -1

	return v, i

def heat(voltage):
	"""Assuming that s in the transfer function is voltage,
	then the change made by the actuator is smaller as the voltage
	increases, so clearly I'm using the transfer function wrong"""

	"""The fact that we were using purely error with no gain or control action for voltage may explain this"""
	delta = T / float((1+(1-voltage)*T))
	return delta

def cool(voltage):
	delta = -T / float((1+(1-voltage)*T))
	return delta

def plant(voltage):
	if voltage > 0:
		delta = heat(voltage)
		print "heat"
	else:
		delta = cool(abs(voltage))
		print "cool"
	return delta

def main():
	setpoint = 60
	startVal = 80
	actual = startVal
	prev = 0
	i = 0

	#plotting

	output = []
	escape = 0
	plotError = []
	plotI = []
	plotV =[]
	plotSP = []

	while escape != 'graph':
		if escape:
			setpoint = float(escape)
		error = setpoint - actual
		voltage, i = controller(error, .8, 0, prev, i)
		delta = plant(voltage)
		actual += delta
		print actual
		prev = error

		#printVars
		output.append(actual)
		plotI.append(i)
		plotSP.append(setpoint)
		plotError.append(error)
		plotV.append(voltage)
		escape = raw_input()
	#plotting
	plot.figure(1)
	plot.title('System Output Over Time')
	plot.xlabel('Iterations')
	plot.ylabel('Output')
	plot.plot(plotSP)
	plot.plot(output)
	plot.legend(['setpoint', 'output'])
	#plot.axis([0, len(output), startVal, setpoint + 5])
	plot.figure(2)
	plot.title('Error Over Time')
	plot.xlabel('Iterations')
	plot.ylabel('Error')
	plot.plot(plotI)
	plot.plot(plotError)
	#plot.plot(plotV)
	plot.legend(['Cumulative Error', 'Error'])
	plot.show()

main()