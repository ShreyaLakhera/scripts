import sys
import numpy as np

"""
This script writes an external current file for given neurons and a given form (to all of these neurons)
"""

def f(x, V):
	"""This is the function describing what form the external current takes. It can be set to return the values you want, default is a DC current of some magnitude.
	"""
	y = float(V)
	return y


outfilename = sys.argv[1]		# Enter the name of the External Current File that you want to write
start_time = float(sys.argv[2])		# Enter the time when the external current starts
end_time = float(sys.argv[3])		# Enter the time when the external current stops
I_value = float(sys.argv[4])		# Enter the value of DC current that you want
whichNeurons = sys.argv[5].split(',')	# Enter the comma separated indices of neurons that you want to give the external current to, eg: 0,1,5,6 
step = 0.01

nNeuron_ext_curr = len(whichNeurons)

time_list = np.ndarray.tolist(np.arange(start_time, end_time + step, step))

I_ext_list = []

for x in time_list:
	y = f(x, I_value)
	I_ext_list.append(y)

outfile = open(outfilename, 'w')
outfile.write('time,' + sys.argv[5] + '\n')

for x in time_list:
	y = float(I_ext_list[time_list.index(x)])
	l = str(x) + (',' + str(y))*nNeuron_ext_curr + '\n'
	outfile.write(l)

outfile.close()	
