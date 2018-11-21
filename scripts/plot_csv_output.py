import sys
import matplotlib.pyplot as plt

infilename = sys.argv[1]

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
print(str(n))
x = 1

while x <= n:
	print('Collecting data for - ' + str(x) + ' - ' + labels[x])
	values = []
	for dv in data:
		values.append(float(dv[x]))

	plot_num = n*100 + 10 + x

	plt.subplot(plot_num)
	plt.plot(ts, values, 'k-')
	plt.grid(True)
	plt.ylabel(labels[x])

	if x == n:
		plt.xlabel(labels[0])	

	x = x+1

plt.show()
