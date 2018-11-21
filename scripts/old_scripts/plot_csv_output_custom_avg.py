import sys
import matplotlib.pyplot as plt

"""
Script to plot the average of all voltage values in the network output file.
Uses the format nxv as the label for voltage reading (where x is an integer)
"""

# Collect the voltages

infilename = sys.argv[1] 	# The csv file in which it reads the ouutput voltage readings

ts = []
data = []
volt_ids = []

infile = open(infilename, 'r')

ln = 1
for line in infile:
	if 'time' in line:
		labels = line.strip('\n').split(',')
		print('\nThese are all the labels ---\n')
		print(labels)

		i = 0
		for x in labels:
			if x[0] == 'n' and x[-1] == 'v':
				volt_ids.append(i)
			i +=1		
		print('\nThese indices from above list are being averaged ---\n')
		print(volt_ids)

	elif ('time' not in line) and (line != '\n'):
		l1 = line.strip('\n').split(',')
		l = [float(l1[j]) for j in volt_ids]
		l_avg = sum(l)/len(l)
		data.append(l_avg)
		ts.append(float(l1[0]))
	ln += 1

infile.close()

# Plotting the average voltage

plt.figure(1)

plt.plot(ts, data, 'k-')
#plt.grid(True)
plt.ylabel('Average of all voltage readings')
plt.xlabel(labels[0])	

plt.show()

