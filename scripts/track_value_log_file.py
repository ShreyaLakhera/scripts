import sys
import numpy as np
import matplotlib.pyplot as plt

infile = open(sys.argv[1], 'r')
v = sys.argv[2].split(',')

for x in v:
	val_list = []
	for l in infile:
		if x in l:
			val = float(l.split(':')[1])
			val_list.append(val)

	val_list1 = np.array(val_list)
	print(val_list1)
	plt.plot(val_list1, '-r')
	plt.show()

infile.close()
