import sys
import matplotlib.pyplot as plt
import numpy as np

infilename = sys.argv[1]
to_plot = sys.argv[2].split(',')

infile = open(infilename, 'r')
inlines = []

for line in infile:
	inlines.append(line)

infile.close()

outdata = []

for x in to_plot:
	values = []
	for line in inlines:
		if x in line:
			val = line.strip('\n').split(':')[1]
			values.append(val)
	print len(values)

 	outdata.append(values)

	if len(values) >= 200000:
		print("Plotting only starting 200000 values")
		plt.plot(values[:200000], '-k')
		plt.show()
	else:
		plt.plot(values, '-k')
		plt.show()
