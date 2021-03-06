import sys
import matplotlib.pyplot as plt

infilename = sys.argv[1]
plot_these = sys.argv[2].split(',')   # Input the variables that you want to plot, eg: n1v,n2v 

ts = []
data = []

infile = open(infilename, 'r')

for line in infile:
	if 'time' in line:
		labels = line.strip('\n').split(',')
		print(labels)

	elif 'time' not in line:
		l = line.strip('\n').split(',')
		data.append(l)
		ts.append(l[0])


plt.figure(1)

n = len(labels) - 1
p = len(plot_these)

print(str(n))
print(str(p))

color = ['r', 'b', 'g', 'o']

for x in plot_these:
	i = labels.index(x)
	q = plot_these.index(x)
	plot_num = p*100 + 10 + q + 1
	print(str(plot_num))
	#print('Collecting data for - ' + str(q) + ' - ' + x)
	values = []
	for dv in data:
		values.append(float(dv[i]))


	ylab = 'V_LN' + x[1:2]
	plt.subplot(plot_num)
	plt.plot(ts[20000:], values[20000:], color[q], linewidth=2.0)
#	plt.grid(True)
	plt.ylabel(ylab)
	plt.ylim((-70, 10))

	if q == p-1:
		plt.xlabel(labels[0])	


plt.show()
	
	




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
