import sys
import math
import numpy as np

"""
This script will generate an external current file for insilico with currents for different groups of neurons, where for we specify a gaussian distribution of the dc current being given to the population of neurons (like in 50 neurons, n10 gets i=4, (n9 and n11) get i=3, etc.)

Sample command:
If we want to create input for groups of 10 and 20 neurons, with the following:
		g1	g2
max value	5	50
width		3	8
mean		4	11
start time	10 ms	10 ms
end time	50 ms	50 ms
 
python /address/script_name.py /address/outfilename.ecf 2 10,20 5,50 3,8 4,11 10,10 50,50

arg 1 	outfile address
arg 2 	number of types/groups of neurons
arg 3 	number of neurons in each group as a comma separated list (eg 10,20)
arg 4	maximum dc current value (given to the neuron at mean of gaussian) for each gaussian in a group as a comma separated list (eg 5,50)
arg 5 	width of gaussian for each group as a comma separated list (eg 3,8)
arg 6	mean of gaussian (which neuron) for each group as a comma separated list (eg 4,11)
arg 7	start times of dc current for each group as a comma separated list (eg 10,10)
arg 8   end times of dc current for each group as a comma separated list (eg 50,50)
"""

def createIExt(start_time, end_time, start_time_specific, end_time_specific, step, I_val):
	time_list = np.ndarray.tolist(np.arange(start_time, end_time + step, step))
	I_list = []
	for t in time_list:
		if (t >= start_time_specific) or (t <= end_time_specific):
			I = round(float(I_val), 3)
		else:
			I = 0
		I_list.append(I)

	return I_list

outfilename = sys.argv[1]
tNeurons = int(sys.argv[2])

# For each type of neuron, define - number of neurons in it, maximum value of input current, width of the gaussian current input, where the maximum current is placed (mean for the gaussian)

nNeurons = sys.argv[3].split(',')
heights = sys.argv[4].split(',')		# maximum value of current
widths = sys.argv[5].split(',')			# width of gaussian
h_pos = sys.argv[6].split(',')			# mean for gaussian (which neuron)
start_times = sys.argv[7].split(',') 
end_times = sys.argv[8].split(',')

if (tNeurons != len(nNeurons)) or (tNeurons != len(heights)) or (tNeurons != len(widths)) or (tNeurons != len(h_pos)) or (tNeurons != len(start_times)) or (tNeurons != len(end_times)):
	print("The inputs do not correspond to number of neurons. Check the length of the terms being passed.")

total_number_Neurons = sum([int(g) for g in nNeurons])

# Create the super nested list that has all the values from lowest time point to highest time point for all neurons

I_ext_list = []

step = 0.01
start_time = float(min(start_times))
end_time = float(max(end_times))

time_list = np.ndarray.tolist(np.arange(start_time, end_time + step, step))

for t in range(tNeurons):
	type_neuron_list = []
	nNeurons_sp = int(nNeurons[t])

	# Creat Gaussian here, and enter the specific DC value to the function
	h = float(heights[t])
	sigma = float(widths[t])
	mu = float(h_pos[t])

	C = h/(1/(sigma*(math.sqrt(2*math.pi))))

	for idNeuron in range(nNeurons_sp):
		I_val = C * (1/(sigma*(math.sqrt(2*math.pi)))) * np.exp(-((float(idNeuron) - mu)**2)/(2*(sigma**2)))
		print(str(I_val))
		I_ext = createIExt(start_time, end_time, start_times[t], end_times[t], step, I_val) 	# This gives back a list
#		print(I_ext)
		type_neuron_list.append(I_ext)

	I_ext_list.append(type_neuron_list)


# Write this to outfile

outfile = open(outfilename, 'w')
outfile.write('time,' + ','.join([str(g) for g in range(total_number_Neurons)]) + '\n')

for t in time_list:
	t_id = time_list.index(t)
	y =  [[str(I_ext_list[nTypeNeuron][idNeuron][t_id]) for idNeuron in range(len(I_ext_list[nTypeNeuron]) - 1)] for nTypeNeuron in range(tNeurons)]
#	print(y)
	l = str(t) + ','
	for x in y:
		substring = ','.join(x)
		l = l + substring 
	l = l + '\n'
#	print(l)
	outfile.write(l)

outfile.close()	
