import sys
import matplotlib.pyplot as plt

infilename = sys.argv[1]
plot_these = sys.argv[2].split(',')   	# Input the variables that you want to plot, eg: n1v,n2v 
outfilename = sys.argv[3] 		# Input the address of the output file to save without '.png' or '.pdf' at the end
show_val = sys.argv[4]			# Enter 'TRUE' to show the plots, any other string to not show it

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


fig = plt.figure(1)

n = len(labels) - 1
p = len(plot_these)

print(str(n))
print(str(p))

colour_list = ['k-', 'r-', 'b-', 'g-', 'r--', 'b--', 'y-']

for x in plot_these:
	i = labels.index(x)
	q = plot_these.index(x)
	print('Collecting data for - ' + str(q) + ' - ' + x)
	values = []
	
	for dv in data:
		values.append(float(dv[i]))
	
	plt.plot(ts, values, colour_list[q], label=x)


plt.legend()
plt.grid(True)
plt.ylabel('V')
plt.xlabel(labels[0])	
fig.savefig(outfilename + '.png')	
fig.savefig(outfilename + '.pdf')	

if show_val == 'TRUE':
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
