import matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import numpy as np
import sys

"""
"""
# Collect the voltages
infilename = sys.argv[1]
plot_these1 = sys.argv[2].split(',')	# Give the range or number separated by * and commas
outfig = sys.argv[3]                    # Write the address where to save the figure

plot_these = []
for n in plot_these1:
	if '*' in n:
		nr = n.split('*')
		ns = range(int(nr[0]), int(nr[1])+1)
		plot_these += ns
	else:
		plot_these += [int(n)]

print('\nThese are all the values to plot ---\n')
print(plot_these)

ts = []
data = []
volt_ids = []

infile = open(infilename, 'r')

ln = 1
for line in infile:
	if 'time' in line:
		labels = line.strip('\n').split(',')
		#print('\nThese are all the labels ---\n')
		#print(labels)

		i = 0
		for x in labels:
			if (x[0] == 'n') and (x[-1] == 'v') and (int(x[1:-1]) in plot_these):
				volt_ids.append(i)
			i +=1		
		print(volt_ids)

	elif ('time' not in line) and (line != '\n'):
		l1 = line.strip('\n').split(',')
		l = [float(l1[j]) for j in volt_ids]
		data.append(l)
		ts.append(float(l1[0]))
	ln += 1

infile.close()
data1 = np.transpose(np.array(data))
#print(len(data1))
#print(len(data1[1]))
#print(len(volt_ids))

# make these smaller to increase the resolution
dx, dy = 0.01, 1

# generate 2 2d grids for the x & y bounds
# y = number of neurons (), x = timesteps
ymax = len(volt_ids) + dy
ymin = 1
xmax = ts[-1] + dx
xmin = 0
y, x = np.mgrid[ymin:ymax+dy:dy,xmin:xmax+dx:dx]
z = data1
levels = MaxNLocator(nbins=100).tick_values(z.min(), z.max())


# pick the desired colormap, sensible levels, and define a normalization
# instance which takes data values and translates those into levels.
cmap = plt.get_cmap('binary')
norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

#plt.rcParams['figure.figsize'] = (20,20)
fig = plt.figure(1)
ax0 = plt.axes()
im = ax0.pcolormesh(x, y, z, cmap=cmap)
fig.colorbar(im, ax=ax0)
ax0.set_title('pcolormesh with levels')

"""
# contours are *point* based plots, so convert our bound into point
# centers
cf = ax1.contourf(x[:-1, :-1] + dx/2.,
                  y[:-1, :-1] + dy/2., z, levels=levels,
                  cmap=cmap)
fig.colorbar(cf, ax=ax1)
ax1.set_title('contourf with levels')
"""
# adjust spacing between subplots so `ax1` title and `ax0` tick labels
# don't overlap
fig.tight_layout()

plt.savefig(outfig)
print('Saved')
plt.show()
