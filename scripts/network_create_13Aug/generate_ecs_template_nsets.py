import sys
import math
import numpy as np
import matplotlib.pyplot as plt
"""

Last modified on - 11 September 2018

This script will generate a template for the nsets generator. From this template, nsets generator can read for each neuron these values = [ pulseduration, pulsestart, pulse-end, tau_rise, tau_fall, pulsemax, pulsemin ]

Here we just distribute the data in a gaussian way, depending on the input

This (has been/is being/will be) modified to include multiple gaussian distribution for each group.

Sample command:
If we want to create input for groups of 10 and 20 neurons, with the following (where g1-x is the xth gaussian added in the 1st group/type of neurons) :
		g1-1	g1-2	g2
width		3	6	8                       # This is the number of neurons which get gaussian modulated input (not the sigma for gaussian as was the case earlier)
mean		4	7	11			# This will be taken as index of the neuron in that group eg here it will assign mean position to 5th neuron in group 1, 8th neuron in group 1, and 12th neuron in group 2 (which will be 20 + 12 = 32nd neuron overall)
PulseDuration   30 	30 	30 
PulseStart  	0 ms	10 ms	20 ms
PulseEnd    	30 ms	40 ms	50 ms
tau_rise    	0.4	0.1	0.1
tau_fall     	0.3	0.1	0.2
PulseMax    	30 mV	40 mV	50 mV
min_i_val       5       2       4
PulseMin    	5 mV	0 mV	10 mV
 
python /address/script_name.py /address/outfilename.ecf 2 2,1 10,20 3,4,30,0,30,0.4,0.3,30,5*6,7,30,10,40,0.1,0.1,40,0*8,11,30,20,50,0.1,0.2,50,10  

arg 1 	outfile address
arg 2 	number of types/groups of neurons
arg 3 	number of gaussians in each groups as a comma separated list (eg 2,1) minimum value for each group = 1, see ***
arg 4 	number of neurons in each group as a comma separated list (eg 10,20)
arg 5	width, mean and Pulse parameters for each gaussian (separated by commas) and for all gaussian separated by * (eg 5,3,4,10,50*5,6,7,10*50,8,11,10,50)
	(g1,g2,g3 in this list will given as first 2 to group 1, next 1 to group 2, depending on arg 3)

***Right now, the script does not work if you write number of gaussians (arg 3) as 0,2 and give just two sets of gaussians property in arg 5. You will have to write 1,2 in arg 3 and specify 3 gaussians and set max current value of first gaussian to 0. 

13 November ===== Script now calculates sigma for the gaussian on its own. Entered value for width is now the new width defined below. Two new variables are needed - width and low_val.
Width == the number of neurons in the group which get non-default value (low_val) current that is part of a gaussian
low_val == the default value of external current that all neurons will get regardless of where they are.
******Keep in mind.....low_val (PulseMin) <= min_i_val


"""


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
"""

def getIval(nN, max_i_val, sigma, mu):
	I_val_array = np.zeros(nN)

	C = max_i_val/(1/(sigma*(math.sqrt(2*math.pi))))

	for idNeuron in range(nN):
		I_val = C * (1/(sigma*(math.sqrt(2*math.pi)))) * np.exp(-((float(idNeuron) - mu)**2)/(2*(sigma**2)))
                if I_val < 0.1*max_i_val:
                        I_val = 0
                I_val_array[idNeuron] = I_val


	return I_val_array

def getIval(nN, max_i_val, min_i_val, mu, low_val, width):
	I_val_array = np.zeros(nN)
        
        if max_i_val == 0:
                for idNeuron in range(nN):
                        I_val_array[idNeuron] = 0

        else:   

                sigma = np.sqrt((-1/(2*np.log(min_i_val/max_i_val)))*((width/2)**2))

	        for idNeuron in range(nN):
		        I_val = max_i_val*np.exp(-((float(idNeuron) - mu)**2)/(2*(sigma**2)))
                        if I_val < min_i_val:
                                I_val = low_val
                        I_val_array[idNeuron] = I_val


	return I_val_array




	
# Inputs

outfilename = sys.argv[1]
tN = int(sys.argv[2])							# Types of neurons
nGa = [int(a) for a in sys.argv[3].split(',')]				# Number of gaussian in each type/group
nNa = [int(n) for n in sys.argv[4].split(',')]				# number of neurons in each type/group
Df = sys.argv[5]
#print(Df)
A = sys.argv[5].split('*')
#print(A)
B = [p.split(',') for p in A]
print(B)

allD = []
for t in range(tN):
	print(t)
	allD_t = []
	for nG in range(nGa[t]):
		print(nG)
		i = sum(nGa[:t]) + int(nG)
		print(i)
		D = B[i]
		allD_t.append(D)  
	allD.append(allD_t)

print(allD)

start_time_all = max([float(p[3]) for p in B])
end_time_all = max([float(p[4]) for p in B])
#start_time_all = 10
#end_time_all = 50

#if (tNeurons != len(nNeurons)) or (tNeurons != len(heights)) or (tNeurons != len(widths)) or (tNeurons != len(h_pos)) or (tNeurons != len(start_times)) or (tNeurons != len(end_times)):
#	print("The inputs do not correspond to number of neurons. Check the length of the terms being passed.")







# main

I_ext_list = []

for t in range(tN):
	nN = nNa[t]
	iext_t = []
	I_val = np.zeros(nN)
	for nG in range(nGa[t]):
		width = float(allD[t][nG][0])
		mu = float(allD[t][nG][1])
		h = float(allD[t][nG][7])
                min_i_val = float(allD[t][nG][9])
                low_val = float(allD[t][nG][8])
		I_val += getIval(nNa[t], h, min_i_val, mu, low_val, width)
		print(str(t) + '   ' + str(nG) + '  ' + str(nN))
		print(I_val)
	for n in range(nN):
		t_start = float(allD[t][nG][3])
		t_end = float(allD[t][nG][4])
		#iext_t_n = createIExt(start_time_all, end_time_all, t_start, t_end, step, I_val[n])
                d = [t, n, allD[t][nG][2], allD[t][nG][3], allD[t][nG][4], allD[t][nG][5], allD[t][nG][6], round(I_val[n],3), allD[t][nG][8]]                                                                                          # Need to add - 
		iext_t.append(d)

	I_ext_list.append(iext_t)
	

#print(len(I_ext_list))
#print(str(len(I_ext_list[0])) + '  ' + str(len(I_ext_list[1])))
#print(str(len(I_ext_list[0][1])) + '  ' + str(len(I_ext_list[1][2])))
#print(I_ext_list)




# Write this to outfile

#outfile = open(outfilename, 'w')
#outfile.write('time,' + ','.join([str(g) for g in range(sum(nNa))]) + '\n')
outfile = open(outfilename, 'w')
outfile.write('nNeuron,PulseDuration,PulseStart,PulseEnd,tau_rise,tau_fall,PulseMax,PulseMin\n')

#ime_list = np.ndarray.tolist(np.arange(start_time_all, end_time_all + step, step))

i = 1
pn_ival = []
nzPN = 0
ln_ival = []
nzLN = 0
for nTypeNeuron in range(tN):
        for idNeuron in range(len(I_ext_list[nTypeNeuron])):
                d = I_ext_list[nTypeNeuron][idNeuron]
                d_str = [str(di) for di in d[2:]]
                outfile.write(str(i) + ',' + ','.join(d_str) + '\n')
                if nTypeNeuron == 0:
                        ival = float(d[7])
                        pn_ival.append(float(d[7]))
                        if ival != 0:
                                nzPN += 1
                if nTypeNeuron == 1:
                        ival = float(d[7])
                        ln_ival.append(float(d[7]))
                        if ival != 0:
                                nzLN += 1

outfile.close()


print('\nNon zero Pns are = ' + str(nzPN))
print('\nNon zero Lns are = ' + str(nzLN))

"""
plt.figure(1)
plt.plot(pn_ival)
plt.ylabel('Magnitude of external current (nA)')
plt.xlabel('Neuron ID')
#plt.grid('TRUE')

plt.figure(2)
plt.plot(ln_ival)
plt.ylabel('Magnitude of external current (nA)')
plt.xlabel('Neuron ID')
#plt.grid('TRUE')
plt.show()
"""
"""
for t in time_list:
	t_id = time_list.index(t)
	y =  [[str(I_ext_list[nTypeNeuron][idNeuron][t_id]) for idNeuron in range(len(I_ext_list[nTypeNeuron]))] for nTypeNeuron in range(tN)]
#	print(y)
	l = str(t)
	for x in y:
		substring = ','.join(x)
		l = l + ',' + substring 
	l = l + '\n'
#	print(l)
	outfile.write(l)
"""
