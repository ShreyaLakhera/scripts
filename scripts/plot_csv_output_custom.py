import sys
import matplotlib.pyplot as plt
import numpy as np

infilename = sys.argv[1]
plot_these = sys.argv[2].split(',')     # Input the variables that you want to plot, eg: n1v,n2v 
savefigname = sys.argv[3]               # Input the name of file to save


ts = []
data = []

infile = open(infilename, 'r')

plot_ids = []
ln = 1
for line in infile:
	if 'time' in line:
		labels = line.strip('\n').split(',')
		print(labels)

		i = 0
		for x in labels:
			if x in plot_these:
				plot_ids.append(i)

			i +=1		

		print(plot_ids)

	elif ('time' not in line) and (line != '\n'):
		l1 = line.strip('\n').split(',')
		if len(l1) <= len(plot_ids):
			print(ln)
			print(line)
		else:
			l = [float(l1[j]) for j in plot_ids]
			data.append(l)
			ts.append(float(l1[0]))
	ln += 1

infile.close()
plt.rcParams['figure.figsize'] = (20,20)
plt.figure(1)

p = len(plot_these)

print(str(p))
print(data[50])

data1 = np.array(data)


j = 1
for x in range(p):
	plot_num = p*100 + 10 + j
	print(str(plot_num))
	#print('Collecting data for - ' + str(q) + ' - ' + x)
	values = [float(dv[x]) for dv in data]
	plt.subplot(plot_num)
	plt.plot(ts, values, 'k-')
	plt.grid(True)
	plt.ylabel(labels[plot_ids[x]])

	if j == p:
		plt.xlabel(labels[0])	
	j += 1


plt.savefig(savefigname)
print('Saved')
#plt.show()
#x = 1

#while x <= n:
#	print('Collecting data for - ' + str(x) + ' - ' + labels[x])
#	values = []
#	for dv in data:
#		values.append(float(dv[x]))

#	plot_num = n*100 + 10 + x

#	plt.subplot(plot_num)
#	plt.plot(ts, values, 'k-')
#	plt.grid(True)
#	plt.ylabel(labels[x])

#	if x == n:
#		plt.xlabel(labels[0])	

#	x = x+1

#plt.show()
